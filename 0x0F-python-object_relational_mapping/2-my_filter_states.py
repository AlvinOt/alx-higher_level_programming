#!/usr/bin/python3
"""
Displays all values in the states table of the hbtn_0e_0_usa database
whose name matches the supplied argument.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    dtbconnectn = MySQLdb.connect(user=sys.argv[1], port=3306, host="localhost",
                         passwd=sys.argv[2], db=sys.argv[3])
    cursr = dtbconnectn.cursor()
    cursr.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
    id ASC".format(sys.argv[4]))
    us_states = cursr.fetchall()
    for state in us_states:
        if state[1] == sys.argv[4]:
            print(state)
    cursr.close()
    dtbconnectn.close()
