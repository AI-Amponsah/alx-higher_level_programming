#!/usr/bin/python3

import MySQLdb
from sys import argv

"""Script lists all states in a database"""

if __name__ == "__main__":
    conn = MySQLdb.connect
    (
     host="localhost",
     port=3306,
     user=argv[1],
     password=argv[2],
     database=argv[3]
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    all_query = cursor.fetchall()
    for i in all_query:
        print(i)
    cursor.close()
    conn.close()
