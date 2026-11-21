#!/usr/bin/python3
"""List each state followed by its cities in ID order."""
import sys
from sqlalchemy import create_engine
from urllib.parse import quote
from sqlalchemy.orm import joinedload, sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == '__main__':
    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        quote(sys.argv[1]), quote(sys.argv[2]), sys.argv[3])
    engine = create_engine(url)
    session = sessionmaker(bind=engine)()
    try:
        rows = session.query(State).options(joinedload(State.cities))
        for state in rows.order_by(State.id):
            print('{}: {}'.format(state.id, state.name))
            for city in state.cities:
                print('\t{}: {}'.format(city.id, city.name))
    finally:
        session.close()
