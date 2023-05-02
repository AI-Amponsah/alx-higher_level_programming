#!/usr/bin/python3

""" This scripts prints states from a DB"""
import MySQLdb

from sys import argv
if __name__ == "__main__":
    con = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = con.cursor()
    cursor.execute("SELECT c.id, c.name, s.name FROM cities as c\
		    INNER JOIN states as s\
		    ON c.state_id = s.id ORDER BY c.id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    con.close()
