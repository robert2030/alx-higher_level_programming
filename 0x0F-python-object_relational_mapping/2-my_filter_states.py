#!/usr/bin/python3
""" Python script to display values
in the states table based on a search argument
"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <db_name> <state_name>".format(
            sys.argv[0]))
        sys.exit(1)

    username, password, db_name, state_name = sys.argv[1:5]

    db = MySQLdb.connect(user=username,
                         passwd=password,
                         db=db_name,
                         host='localhost',
                         port=3306)

    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY\
            id ASC".format(state_name)
    cur.execute(query)

    results = cur.fetchall()

    for row in results:
        print(row)

    cur.close()
    db.close()
