#!/usr/bin/python3

""" This scripts prints states from a DB"""
import MySQLdb

from sys import argv
if __name__ == "__main__":
    con = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = con.cursor()
    search = "SELECT * FROM states  WHERE BINARY name = %s"
    cursor.execute(search, (argv[4],))
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    con.close()
