# Python - Object-relational mapping

Python scripts that interact with MySQL using MySQLdb (tasks 0-5) and
SQLAlchemy ORM (tasks 6-14).

## Requirements

Python 3.8.5, MySQLdb 2.0.x and SQLAlchemy 1.4.x are the versions used by
the Holberton checker. Every executable script uses three database arguments:
username, password and database. Tasks 2, 3, 5 and 10 accept an extra search
argument.

## Usage

```bash
./0-select_states.py root password hbtn_0e_0_usa
./3-my_safe_filter_states.py root password hbtn_0e_0_usa Arizona
./7-model_state_fetch_all.py root password hbtn_0e_6_usa
```

Task 2 intentionally demonstrates insecure SQL string formatting for the
SQL injection lesson; never reuse this pattern in production. Task 3
uses SQL parameters to prevent SQL injection.
