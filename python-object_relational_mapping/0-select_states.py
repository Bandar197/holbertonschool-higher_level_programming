#!/usr/bin/python3
"""This is code link with database and read all states"""

import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database)

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()
