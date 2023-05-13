#!/usr/bin/python3
"""Auto init for file storage """
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
