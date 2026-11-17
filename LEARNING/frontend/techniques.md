# CSS/JS-техніки

Конкретні прийоми з готовим кодом — копіюй і адаптуй під свій проєкт.

---

## CSS Scroll Snap — прокрутка, що «прилипає» до секцій

Джерело: відео @junior365day.

Ефект: односторінковий сайт (лендинг), де прокрутка колесом миші чи свайпом
завжди зупиняється точно на межі секції (Hero, Services, About тощо), а не
десь посередині — як у сучасних односторінкових лендингах.

```css
html, body {
  /* overflow: hidden; — за потреби прибрати стандартний скрол сторінки */
}

.sections {
  height: 100vh;
  overflow-y: scroll;
  scroll-snap-type: y mandatory;
}

.section {
  height: 100vh;
  scroll-snap-align: start;
}
```

Розмітка:

```html
<div class="sections">
  <section class="section">Hero</section>
  <section class="section">Services</section>
  <section class="section">About</section>
</div>
```

**Як працює:**
- `.sections` — контейнер-обгортка, сам прокручується (`overflow-y: scroll`) і
  оголошує, що прокрутка має «прилипати» по вертикалі (`scroll-snap-type: y
  mandatory`).
- Кожна `.section` каже, що саме її верхній край — точка прилипання
  (`scroll-snap-align: start`).
- `mandatory` — прокрутка завжди долітає до найближчої секції; якщо замінити
  на `proximity`, прилипання буде м'якшим (тільки коли скрол зупинився
  близько до межі).

**Де спробувати:** підходить для лендингів у цьому ж репозиторії (`WEB/`).
