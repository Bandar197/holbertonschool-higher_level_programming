#!/usr/bin/python3
"""Display JSON or CSV products with optional ID filtering."""

import csv
import json
from pathlib import Path

from flask import Flask, render_template, request

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent


def read_json_products():
    """Read the products in the JSON file."""
    with (BASE_DIR / 'products.json').open(encoding='utf-8') as source:
        return json.load(source)


def read_csv_products():
    """Read the products in the CSV file."""
    with (BASE_DIR / 'products.csv').open(newline='',
                                         encoding='utf-8') as source:
        return list(csv.DictReader(source))


@app.route('/products')
def products():
    """Render products from the chosen source and optional product ID."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        product_list = read_json_products()
    elif source == 'csv':
        product_list = read_csv_products()
    else:
        return render_template('product_display.html', products=[],
                               error='Wrong source')

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
