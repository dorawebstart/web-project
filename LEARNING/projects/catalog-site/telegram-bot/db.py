"""
Проста обгортка над SQLite для каталогу.
Одна таблиця products — і бот, і API-сервер працюють з однією й тією ж базою.
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "products.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # щоб рядки можна було перетворити в dict
    return conn


def init_db():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT,
            price REAL DEFAULT 0,
            description TEXT,
            image_url TEXT,
            available INTEGER DEFAULT 1
        )
    """)
    conn.commit()
    conn.close()


def add_product(name, category, price, description, image_url):
    conn = get_connection()
    conn.execute(
        "INSERT INTO products (name, category, price, description, image_url, available) "
        "VALUES (?, ?, ?, ?, ?, 1)",
        (name, category, price, description, image_url),
    )
    conn.commit()
    new_id = conn.execute("SELECT last_insert_rowid() AS id").fetchone()["id"]
    conn.close()
    return new_id


def list_products(only_available=False):
    conn = get_connection()
    query = "SELECT * FROM products"
    if only_available:
        query += " WHERE available = 1"
    query += " ORDER BY id DESC"
    rows = conn.execute(query).fetchall()
    conn.close()
    return [dict(row) for row in rows]


def get_product(product_id):
    conn = get_connection()
    row = conn.execute("SELECT * FROM products WHERE id = ?", (product_id,)).fetchone()
    conn.close()
    return dict(row) if row else None


def remove_product(product_id):
    conn = get_connection()
    cur = conn.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    deleted = cur.rowcount > 0
    conn.close()
    return deleted


def set_availability(product_id, available: bool):
    conn = get_connection()
    cur = conn.execute(
        "UPDATE products SET available = ? WHERE id = ?",
        (1 if available else 0, product_id),
    )
    conn.commit()
    updated = cur.rowcount > 0
    conn.close()
    return updated
