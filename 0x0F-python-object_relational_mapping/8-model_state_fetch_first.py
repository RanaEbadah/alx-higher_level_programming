#!/usr/bin/python3

"""lists first State from the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    fState = session.query(State).first()
    if fState:
        print(fState.id, fState.name, sep=": ")
    else:
        print("Nothing")
