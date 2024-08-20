#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
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
    query = ("SELECT cities.name FROM states INNER JOIN cities\
             ON states.id = cities.state_id WHERE states.name=%s\
             ORDER BY cities.id ASC")

    cur.execute(query, (state_name,))
    results = cur.fetchall()

    print(", ".join(str(city[0]) for city in results))

    cur.close()
    db.close()
