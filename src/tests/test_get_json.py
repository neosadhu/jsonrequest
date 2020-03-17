import requests
import sys
from src.main.crud_ops import CRUD
def lib():
    c = CRUD()
    return c.get_data()

