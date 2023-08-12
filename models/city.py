#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Define a city.
    Attributes:
        state_id: String - The state id.
        name: String- The name of the city.
    """

    state_id = ""
    name = ""
