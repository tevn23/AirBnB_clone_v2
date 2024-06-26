#!/usr/bin/python3
"""This module instantiates an object of a Storage Class"""
import os
from.base_model import BaseModel
from.amenity import Amenity
from.place import Place
from.state import State
from.user import User
from.city import City
from.review import Review

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage

    storage = DBStorage()


else:
    from models.engine.file_storage import FileStorage

    storage = FileStorage()

storage.reload()

__all__ = [
        'BaseModel',
        'storage',
        'Amenity',
        'Review',
        'Place',
        'State',
        'User',
        'City'
        ]
