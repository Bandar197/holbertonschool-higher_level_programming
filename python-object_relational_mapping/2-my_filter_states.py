#!/usr/bin/python3
"""Filter states using the user input in an SQL string."""

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
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
    cursor.execute(query, (sys.argv[4],))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    connection.close()
