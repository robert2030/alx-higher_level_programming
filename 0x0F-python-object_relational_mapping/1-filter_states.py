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
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    for rows in cur.fetchall():
        if rows[1][0] == 'N':
            print(rows)

    cur.close()
    db.close()
