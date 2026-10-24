#!/usr/bin/python3
"""Display states whose names begin with uppercase N."""

import MySQLdb
import sys


if __name__ == "__main__":
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM states "
        "WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    )
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    connection.close()
