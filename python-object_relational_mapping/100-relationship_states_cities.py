#!/usr/bin/python3
"""Create California and San Francisco through their relationship."""
import sys
from sqlalchemy import create_engine
from urllib.parse import quote
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == '__main__':
    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        quote(sys.argv[1]), quote(sys.argv[2]), sys.argv[3])
    engine = create_engine(url)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    try:
        state = State(name='California')
        city = City(name='San Francisco')
        state.cities.append(city)
        session.add(state)
        session.commit()
    finally:
        session.close()
