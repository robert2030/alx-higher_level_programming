#!/usr/bin/python3
""" Python scripte to list states from MySQL"""


import sys
import MySQLdb

if __name__ == "__main__":

    if len(sys.argv) < 4:
        print("Usage: {} <username> <password> <db_name>".format(sys.argv[0]))
        sys.exit(1)

    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)

    cur = db.cursor()

    cur.execute("SELECT id, name FROM states")

    for state in cur.fetchall():
        print(state)

    cur.close()
    db.close()
