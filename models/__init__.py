#!/usr/bin/python3
"""initilaize method for models dictionary"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
