#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity.
    Attributes:
        name: String - The name of the amenity.
    """

    name = ""
