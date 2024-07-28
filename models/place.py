#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, String
from sqlalchemy import Integer, Float, ForeignKey


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship(
            'Review',
            backref='place',
            cascade='all, delete-orphan'
            )
    place_amenity = Table(
                        'place_amenity', Base.metadata,
                        Column(
                            'place_id',
                            String(60),
                            ForeignKey('places.id'),
                            primary_key=True,
                            nullable=False
                            ),
                        Column(
                            'amenity_id',
                            String(60),
                            ForeignKey('amenities.id'),
                            primary_key=True,
                            nullable=False
                            )
                        )
    amenities = relationship(
            'Amenity',
            secondary=place_amenity,
            viewonly=False,
            back_populates='place_amenities'
            )
    amenity_ids = []

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        from models import storage
        from models.review import Review
        from models.amenity import Amenity

        @property
        def reviews(self):
            all_reviews = storage.all(Review)
            my_reviews = []

            for review in all_reviews:
                if review.place_id == self.id:
                    my_reviews.append(review)

            return my_reviews

        @property
        def amenities(self):
            return amenity_ids

        @amenities.setter
        def amenities(self, amenity):
            if isinstance(amenity, Amenity):
                self.amenity_ids.append(amenity.id)
