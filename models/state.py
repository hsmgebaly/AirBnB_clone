#!/usr/bin/python3
"""Defines the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """ Define a state.
    Attributes:
        name: String -  The name of the state.
    """

    name = ""
