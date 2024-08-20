#!/usr/bin/python3
""" Python script to list all cities from the hbtn_0e_4_usa database """

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("usage: {} <username> <password> <db_name>".format(
            sys.argv[0]))
        sys.exit(1)

    username, password, db_name = sys.argv[1:4]

    db = MySQLdb.connect(
            user=username,
            passwd=password,
            db=db_name,
            host='localhost',
            port=3306)

    cur = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities\
    JOIN states ON cities.state_id = states.id ORDER by cities.id"
    cur.execute(query)
    results = cur.fetchall()

    for rows in results:
        print(rows)

    cur.close()
    db.close()
