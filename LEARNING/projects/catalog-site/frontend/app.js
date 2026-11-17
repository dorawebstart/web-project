// ---------------------------------------------------------------
// Каталог товарів/послуг — навчальний проєкт.
// Один фронтенд, три джерела даних:
//   demo   — локальний data/demo.json (без налаштувань)
//   sheets — публічна Google Таблиця (через gviz JSON endpoint)
//   api    — локальний Telegram-бот + Flask API (telegram-bot/)
//
// Кожне джерело повертає масив об'єктів однакової форми:
//   { name, category, price, description, image_url, available }
// ---------------------------------------------------------------

let allProducts = [];
let currentSource = "demo";

const els = {
  statusBox: document.getElementById("status"),
  grid: document.getElementById("catalog"),
  search: document.getElementById("search"),
  categoryFilter: document.getElementById("category-filter"),
  sheetsConfig: document.getElementById("sheets-config"),
  apiConfig: document.getElementById("api-config"),
};

function setStatus(message, isError = false) {
  els.statusBox.textContent = message || "";
  els.statusBox.classList.toggle("error", isError);
}

// ---------- Джерело 1: локальний demo.json ----------
async function fetchDemo() {
  const res = await fetch("data/demo.json");
  if (!res.ok) throw new Error("Не вдалося завантажити demo.json");
  return await res.json();
}

// ---------- Джерело 2: Google Таблиця (gviz JSON) ----------
// Очікуваний порядок колонок у таблиці (з заголовком у першому рядку):
// name | category | price | description | image_url | available
//
// Публічна таблиця (Файл → Поділитися → "Усі, хто має посилання")
// віддає дані через службовий ендпоінт без потреби в API-ключі:
//   https://docs.google.com/spreadsheets/d/<ID>/gviz/tq?tqx=out:json
async function fetchGoogleSheet(sheetId) {
  if (!sheetId) throw new Error("Вкажи ID Google Таблиці");

  const url = `https://docs.google.com/spreadsheets/d/${encodeURIComponent(sheetId)}/gviz/tq?tqx=out:json`;
  const res = await fetch(url);
  if (!res.ok) throw new Error("Таблиця недоступна. Перевір ID і що доступ відкрито всім за посиланням.");

  const text = await res.text();
  const rows = parseGvizResponse(text);
  return rows;
}

// gviz повертає не чистий JSON, а JS-обгортку на кшталт:
//   /*O_o*/
//   google.visualization.Query.setResponse({...});
// тому витягуємо об'єкт регуляркою й розбираємо вручну.
function parseGvizResponse(text) {
  const match = text.match(/setResponse\(([\s\S]+)\);?\s*$/);
  if (!match) throw new Error("Не вдалося розпізнати відповідь Google Таблиці");

  const data = JSON.parse(match[1]);
  const cols = data.table.cols.map((c) => (c.label || "").trim().toLowerCase());
  const rows = data.table.rows || [];

  // якщо в таблиці немає заголовків-лейблів (буває на порожніх колонках),
  // підставляємо очікуваний порядок полів
  const fallbackOrder = ["name", "category", "price", "description", "image_url", "available"];

  return rows.map((row) => {
    const obj = {};
    row.c.forEach((cell, i) => {
      const key = cols[i] || fallbackOrder[i] || `col${i}`;
      let value = cell ? cell.v : "";
      if (key === "price") value = Number(value) || 0;
      if (key === "available") {
        value = String(value).trim().toLowerCase();
        value = value === "true" || value === "так" || value === "yes" || value === "1";
      }
      obj[key] = value;
    });
    return obj;
  }).filter((p) => p.name); // прибираємо порожні рядки
}

// ---------- Джерело 3: Telegram-бот через локальний API ----------
async function fetchBotApi(apiUrl) {
  if (!apiUrl) throw new Error("Вкажи адресу API");
  const res = await fetch(apiUrl.replace(/\/$/, "") + "/api/products");
  if (!res.ok) throw new Error("API бота не відповідає. Чи запущений telegram-bot/api_server.py?");
  return await res.json();
}

// ---------- Рендер ----------
function renderCategoryOptions(products) {
  const categories = [...new Set(products.map((p) => p.category).filter(Boolean))].sort();
  const current = els.categoryFilter.value;
  els.categoryFilter.innerHTML = '<option value="">Усі категорії</option>' +
    categories.map((c) => `<option value="${escapeHtml(c)}">${escapeHtml(c)}</option>`).join("");
  els.categoryFilter.value = categories.includes(current) ? current : "";
}

function escapeHtml(str) {
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function renderGrid() {
  const query = els.search.value.trim().toLowerCase();
  const category = els.categoryFilter.value;

  const filtered = allProducts.filter((p) => {
    const matchesQuery = !query || (p.name || "").toLowerCase().includes(query);
    const matchesCategory = !category || p.category === category;
    return matchesQuery && matchesCategory;
  });

  if (filtered.length === 0) {
    els.grid.innerHTML = "";
    setStatus("Нічого не знайдено за цими умовами.");
    return;
  }

  setStatus(`Показано: ${filtered.length} із ${allProducts.length}`);

  els.grid.innerHTML = filtered.map((p) => `
    <div class="card">
      ${p.image_url
        ? `<img src="${escapeHtml(p.image_url)}" alt="${escapeHtml(p.name)}" onerror="this.outerHTML='<div class=&quot;placeholder-img&quot;>без фото</div>'">`
        : `<div class="placeholder-img">без фото</div>`}
      ${p.category ? `<span class="category">${escapeHtml(p.category)}</span>` : ""}
      <h3>${escapeHtml(p.name)}</h3>
      <div class="price">${Number(p.price || 0).toLocaleString("uk-UA")}</div>
      <p class="description">${escapeHtml(p.description || "")}</p>
      <span class="badge ${p.available ? "ok" : "no"}">${p.available ? "Доступно" : "Недоступно"}</span>
    </div>
  `).join("");
}

// ---------- Завантаження за обраним джерелом ----------
async function loadFrom(source) {
  setStatus("Завантаження...");
  try {
    let data;
    if (source === "demo") {
      data = await fetchDemo();
    } else if (source === "sheets") {
      const sheetId = document.getElementById("sheet-id").value.trim();
      data = await fetchGoogleSheet(sheetId);
    } else if (source === "api") {
      const apiUrl = document.getElementById("api-url").value.trim();
      data = await fetchBotApi(apiUrl);
    }
    allProducts = data;
    renderCategoryOptions(allProducts);
    renderGrid();
    setStatus(`Завантажено ${allProducts.length} позицій із джерела "${source}".`);
  } catch (err) {
    console.error(err);
    setStatus(err.message || "Сталася помилка", true);
    allProducts = [];
    els.grid.innerHTML = "";
  }
}

// ---------- UI: перемикання джерел ----------
document.querySelectorAll(".source-btn").forEach((btn) => {
  btn.addEventListener("click", () => {
    document.querySelectorAll(".source-btn").forEach((b) => b.classList.remove("active"));
    btn.classList.add("active");
    currentSource = btn.dataset.source;

    els.sheetsConfig.classList.toggle("hidden", currentSource !== "sheets");
    els.apiConfig.classList.toggle("hidden", currentSource !== "api");

    if (currentSource === "demo") loadFrom("demo");
  });
});

document.getElementById("sheet-load").addEventListener("click", () => loadFrom("sheets"));
document.getElementById("api-load").addEventListener("click", () => loadFrom("api"));
els.search.addEventListener("input", renderGrid);
els.categoryFilter.addEventListener("change", renderGrid);

// старт — демо-дані, щоб сторінка працювала одразу без налаштувань
loadFrom("demo");
