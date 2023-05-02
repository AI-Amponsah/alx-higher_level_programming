#!/usr/bin/python3

""" This scripts prints states from a DB"""
import MySQLdb

from sys import argv
if __name__ == "__main__":
    con = MySQLdb.connect(user=argv[1], passwd=argv[2], port=3306, db=argv[3])
    cursor = con.cursor()
    cursor.execute("SELECT * FROM states  WHERE name LIKE 'N%';")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    con.close()
