# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
import os
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()  # declarative_base is a function call so it should have been declarative_base() as I updated here

class Restaurant(Base):
    __tablename__ = 'restaurant'

    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)

class MenuItem(Base):
    __tablename__ = 'menu_item'
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    course = Column(String(250))
    price = Column(String(8))
    description = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))  # You want to reference the column from restaurant table so it should have been restaurant.id whereas your code had restaurant_id which is not recognized
    restaurant = relationship(Restaurant)

#We added this serialize function to be able to send JSON objects in a serializable format
    @property
    def serialize(self):

       return {
           'name'         : self.name,
           'description'         : self.description,
           'id'         : self.id,
           'price'         : self.price,
           'course'         : self.course,
       }
 ######Insert at end of file#####
engine = create_engine('sqlite:///restaurant.db')  # It is sqlite not sqllite - use single l instead of double l (ll)

Base.metadata.create_all(engine)