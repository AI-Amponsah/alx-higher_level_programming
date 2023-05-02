#!/usr/bin/python3

""" This scripts prints states from a DB"""
import MySQLdb

from sys import argv

if __name__ == "__main__":
	conn_db = MySQLdb.connect( user = argv[1], passwd = argv[2], port = 3306, database = argv[3])
	cursor = conn_db.cursor()
	cursor.execute("SELECT * FROM states")
	states = cursor.fetchall()

	for state in states:
		print(state)
	cursor.close()
	conn_db.close()
