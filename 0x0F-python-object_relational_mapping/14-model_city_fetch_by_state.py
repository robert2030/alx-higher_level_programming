#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <db_name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, db_name = sys.argv[1:4]

    # Connect to MySQL server running on localhost at port 3306
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, db_name),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    cities = session.query(City).order_by(City.id).all()

    for city in session.query(State, City).filter(State.id == City.state_id):
        print("{}: ({}) {}".format(
            city.State.name, city.City.id, city.City.name))

    session.close()
