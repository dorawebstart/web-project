"""
Telegram-бот для керування каталогом сайту.

Власник пише боту команди — дані зберігаються в products.db (SQLite).
Сайт (frontend/) читає ці ж дані через api_server.py.

Запуск:
    export BOT_TOKEN="токен_від_BotFather"   (Windows: set BOT_TOKEN=...)
    python bot.py

Як отримати токен: напиши @BotFather в Telegram → /newbot → слідуй інструкціям.
"""

import logging
import os

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

import db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

HELP_TEXT = (
    "Команди для керування каталогом:\n\n"
    "/add Назва | Категорія | Ціна | Опис | URL_фото\n"
    "   — додати позицію (URL_фото можна залишити порожнім)\n"
    "   приклад: /add Пиріг з вишнею | Випічка | 4600 | Смачний пиріг | \n\n"
    "/list — показати всі позиції з їхніми ID\n"
    "/remove ID — видалити позицію\n"
    "/available ID так — зробити доступною\n"
    "/available ID ні — зробити недоступною\n"
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привіт! Це бот керування каталогом.\n\n" + HELP_TEXT)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(HELP_TEXT)


async def add_product(update: Update, context: ContextTypes.DEFAULT_TYPE):
    raw = " ".join(context.args)
    parts = [p.strip() for p in raw.split("|")]

    if len(parts) < 3 or not parts[0]:
        await update.message.reply_text(
            "Формат: /add Назва | Категорія | Ціна | Опис | URL_фото\n"
            "Потрібні хоча б назва, категорія і ціна."
        )
        return

    name = parts[0]
    category = parts[1] if len(parts) > 1 else ""
    try:
        price = float(parts[2]) if len(parts) > 2 else 0
    except ValueError:
        await update.message.reply_text("Ціна має бути числом, напр. 5000")
        return
    description = parts[3] if len(parts) > 3 else ""
    image_url = parts[4] if len(parts) > 4 else ""

    new_id = db.add_product(name, category, price, description, image_url)
    await update.message.reply_text(f"Додано позицію #{new_id}: {name}")


async def list_products(update: Update, context: ContextTypes.DEFAULT_TYPE):
    products = db.list_products()
    if not products:
        await update.message.reply_text("Каталог поки порожній. Додай позицію через /add.")
        return

    lines = []
    for p in products:
        status = "✅" if p["available"] else "❌"
        lines.append(f"#{p['id']} {status} {p['name']} — {p['price']} ({p['category']})")
    await update.message.reply_text("\n".join(lines))


async def remove_product(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args or not context.args[0].isdigit():
        await update.message.reply_text("Формат: /remove ID (число з /list)")
        return

    product_id = int(context.args[0])
    if db.remove_product(product_id):
        await update.message.reply_text(f"Позицію #{product_id} видалено.")
    else:
        await update.message.reply_text(f"Позиції #{product_id} не знайдено.")


async def set_availability(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 2 or not context.args[0].isdigit():
        await update.message.reply_text("Формат: /available ID так (або ні)")
        return

    product_id = int(context.args[0])
    value = context.args[1].strip().lower()
    available = value in ("так", "yes", "true", "1")

    if db.set_availability(product_id, available):
        await update.message.reply_text(
            f"Позицію #{product_id} позначено як {'доступну' if available else 'недоступну'}."
        )
    else:
        await update.message.reply_text(f"Позиції #{product_id} не знайдено.")


def main():
    token = os.environ.get("BOT_TOKEN")
    if not token:
        raise SystemExit(
            "Не знайдено BOT_TOKEN. Встанови змінну середовища:\n"
            "  export BOT_TOKEN=твій_токен_від_BotFather"
        )

    db.init_db()

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("add", add_product))
    app.add_handler(CommandHandler("list", list_products))
    app.add_handler(CommandHandler("remove", remove_product))
    app.add_handler(CommandHandler("available", set_availability))

    logger.info("Бот запущено. Натисни Ctrl+C щоб зупинити.")
    app.run_polling()


if __name__ == "__main__":
    main()
