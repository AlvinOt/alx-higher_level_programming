#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa, including their
associated cities.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    dtbconnectn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                                  passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursr = dtbconnectn.cursor()
    cursr.execute("""SELECT cities.id, cities.name, states.name FROM
                    cities INNER JOIN states ON states.id=cities.state_id""")
    rows = cursr.fetchall()
    for row in rows:
        print(row)
    cursr.close()
    dtbconnectn.close()
