#!/usr/bin/python3
"""List cities with the names of their states in city ID order."""
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
        rows = session.query(City).options(joinedload(City.state))
        for city in rows.order_by(City.id):
            print('{}: {} -> {}'.format(city.id, city.name, city.state.name))
    finally:
        session.close()
