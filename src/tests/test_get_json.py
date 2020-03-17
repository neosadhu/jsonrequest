import requests
import sys
from src.main.crud_ops import CRUD
def lib():
    c = CRUD()
    print ( c.get_data() )

