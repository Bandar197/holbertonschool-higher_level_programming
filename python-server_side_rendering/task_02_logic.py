#!/usr/bin/python3
"""Render a collection of JSON-backed items using Jinja loops."""

import json
from pathlib import Path

from flask import Flask, render_template

app = Flask(__name__)
DATA_FILE = Path(__file__).resolve().parent / 'items.json'


@app.route('/items')
def items():
    """Display the items in items.json, or an empty-list message."""
    with DATA_FILE.open(encoding='utf-8') as source:
        data = json.load(source)
    return render_template('items.html', items=data.get('items', []))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
