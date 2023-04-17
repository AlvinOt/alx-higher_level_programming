#!/usr/bin/python3
"""
Prints all states from the database `hbtn_0e_0_usa` sorted in ascending order by id.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states` ORDER BY id ASC")
    [print(state) for state in c.fetchall()]

