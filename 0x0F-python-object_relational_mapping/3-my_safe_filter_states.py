#!/usr/bin/python3
"""
Displays all values in the states table of the database hbtn_0e_0_usa
whose name matches that supplied as argument.
Safe from SQL injections
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    dtbconnectn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursr = dtbconnectn.cursor()
    cursr.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
                   (argv[4],))
    rows = cursr.fetchall()
    for row in rows:
        print(row)
    cursr.close()
    dtbconnectn.close()
