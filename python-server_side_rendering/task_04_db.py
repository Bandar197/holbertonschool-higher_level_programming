#!/usr/bin/python3
"""Display product records from JSON, CSV, or a SQLite database."""

import csv
import json
import sqlite3
from pathlib import Path

from flask import Flask, render_template, request

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent


def read_json_products():
    """Load products stored as JSON objects."""
    with (BASE_DIR / 'products.json').open(encoding='utf-8') as source:
        return json.load(source)


def read_csv_products():
    """Load products stored as CSV rows."""
    with (BASE_DIR / 'products.csv').open(newline='',
                                         encoding='utf-8') as source:
        return list(csv.DictReader(source))


def read_sql_products():
    """Return SQLite rows as dictionaries usable by the Jinja template."""
    database = BASE_DIR / 'products.db'
    with sqlite3.connect(database) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(
            'SELECT id, name, category, price FROM Products ORDER BY id'
        ).fetchall()
    return [dict(row) for row in rows]


@app.route('/products')
def products():
    """Render products selected by source and, optionally, a product ID."""
    source = request.args.get('source')
    product_id = request.args.get('id')
    readers = {
        'json': read_json_products,
        'csv': read_csv_products,
        'sql': read_sql_products
    }
    if source not in readers:
        return render_template('product_display.html', products=[],
                               error='Wrong source')

    try:
        product_list = readers[source]()
    except (sqlite3.Error, OSError, ValueError, json.JSONDecodeError) as error:
        app.logger.error('Error loading products: %s', error)
        return render_template('product_display.html', products=[],
                               error='Error reading product data')

    if product_id is not None:
        product_list = [product for product in product_list
                        if str(product['id']) == product_id]
        if not product_list:
            return render_template('product_display.html', products=[],
                                   error='Product not found')

    return render_template('product_display.html', products=product_list,
                           error=None)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
