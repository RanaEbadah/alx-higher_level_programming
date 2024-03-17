#!/usr/bin/python3
"""python file that contains the class definition of a State
and an instance Base = declarative_base()"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import ForeignKey
from model_state import Base, State
from sqlalchemy.orm import relationship


class City(Base):
    """State class with id and name"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=False)
    state = relationship("State", back_populates="cities")
