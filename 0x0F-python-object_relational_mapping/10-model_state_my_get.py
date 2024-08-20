#!/usr/bin/python3
"""
Script that prints the State object with the name passed as an argument
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <db_name> <state_name>".format(
            sys.argv[0]))
        sys.exit(1)

    username, password, db_name, state_name = sys.argv[1:5]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, db_name),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State.id).filter(State.name == sys.argv[4])

    if (state.first() is None):
        print("Not found")
    else:
        print(state[0][0])
