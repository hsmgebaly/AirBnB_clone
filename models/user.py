#!/usr/bin/python3
""" Define User class"""
from model.base_model import BaseModel


class User(BaseModel):
    """ Define a User

    attributes:
    email: string - Email of user
    password: string -Password of user
    first_name: string - first name of user
    last_name: string - Last name of user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
