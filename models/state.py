#!/usr/bin/python3
""" State Module for HBNB project """
import os
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        from sqlalchemy.orm import relationship
        cities = relationship(
                'City',
                backref='state',
                cascade='all, delete-orphan'
                )

    else:
        from models import storage
        def cities(self):
            all_cities = storage.all(City)
            my_cities = []

            for city in all_cities:
                if city.state_id == self.id:
                    my_cities.append(city)

            return my_cities
