
#!/usr/bin/env python3
"""Serialize and deserialize JSON data."""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize data and save it to a JSON file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load JSON data from a file and return it."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
