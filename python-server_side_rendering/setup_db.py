#!/usr/bin/python3
"""Create and seed the SQLite database used by task_04_db.py."""

import sqlite3
from pathlib import Path

DB_FILE = Path(__file__).resolve().parent / 'products.db'


def create_database():
    """Create the products table and insert the example records safely."""
    with sqlite3.connect(DB_FILE) as connection:
        connection.execute('''
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        connection.executemany('''
            INSERT OR IGNORE INTO Products (id, name, category, price)
            VALUES (?, ?, ?, ?)
        ''', [
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
        ])


if __name__ == '__main__':
    create_database()
