#!/usr/bin/python3

"""lists first State from the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State.id).filter(
        State.name == sys.argv[4]).order_by(State.id)
    if (states):
        for state in states:
            tuple_elements = [str(element) for element in state]
            result = "\n".join(tuple_elements)

            print(result)
    else:
        print("Not found")
