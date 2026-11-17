"""
Маленький Flask-сервер, що віддає каталог у форматі JSON для фронтенду.

Запуск:
    python api_server.py

Сайт (frontend/) звертається сюди за адресою:
    http://localhost:5000/api/products
"""

from flask import Flask, jsonify
from flask_cors import CORS

import db

app = Flask(__name__)
CORS(app)  # дозволяємо фронтенду (інший origin / file://) робити запити сюди


@app.route("/api/products")
def get_products():
    db.init_db()  # на випадок, якщо сервер запустили раніше за бота
    products = db.list_products()

    # приводимо до тієї ж форми, що й інші джерела (demo.json, Google Sheets)
    result = [
        {
            "name": p["name"],
            "category": p["category"],
            "price": p["price"],
            "description": p["description"],
            "image_url": p["image_url"],
            "available": bool(p["available"]),
        }
        for p in products
    ]
    return jsonify(result)


@app.route("/")
def index():
    return "API каталогу працює. Дані тут: /api/products"


if __name__ == "__main__":
    db.init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
