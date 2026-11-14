# Python - Server-Side Rendering

Holberton School project 3143: server-side rendered pages and templates in Python with Flask and Jinja.

## Tasks

- **Task 0** (`task_00_intro.py`): `generate_invitations(template, attendees)` creates numbered invitation text files, replacing unavailable attendee fields with `N/A`.
- **Task 1** (`task_01_jinja.py`): `/`, `/about`, and `/contact` display Jinja templates with reusable headers and footers.
- **Task 2** (`task_02_logic.py`): `/items` displays an unordered list loaded from `items.json`, or a fallback for an empty list.
- **Task 3** (`task_03_files.py`): `/products?source=json` and `/products?source=csv` display products, with optional `id` filtering.
- **Task 4** (`task_04_db.py`): adds `/products?source=sql` with the same filtering and error messages.

## Set up

```bash
python3 -m pip install -r requirements.txt
python3 setup_db.py
```

The repository also includes a pre-populated `products.db`. Running `setup_db.py` again is safe.

## Run examples

Launch the app for the desired task:

```bash
python3 task_01_jinja.py  # http://127.0.0.1:5000/
python3 task_02_logic.py  # http://127.0.0.1:5000/items
python3 task_03_files.py  # http://127.0.0.1:5000/products?source=csv&id=1
python3 task_04_db.py     # http://127.0.0.1:5000/products?source=sql&id=2
```

Run one server at a time, as they all listen on port 5000.

To generate invitations from the provided example template:

```python
from task_00_intro import generate_invitations

with open('template.txt', encoding='utf-8') as source:
    template = source.read()

generate_invitations(template, [
    {'name': 'Alice', 'event_title': 'Python Conference',
     'event_date': '2023-07-15', 'event_location': 'New York'}
])
```
