#!/usr/bin/python3
"""Define cities belonging to a state."""
from sqlalchemy import Column, ForeignKey, Integer, String
from relationship_state import Base


class City(Base):
    """A named city in exactly one state."""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
