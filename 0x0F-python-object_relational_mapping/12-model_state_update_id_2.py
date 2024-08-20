#!/usr/bin/python3
"""
Script that changes the name of a State object in the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <db_name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, db_name = sys.argv[1:4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, db_name),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    state_to_change = session.query(State).filter(State.id == 2).first()

    if state_to_change:
        state_to_change.name = 'New Mexico'
        session.commit()
    else:
        print("Not found")

    session.close()
