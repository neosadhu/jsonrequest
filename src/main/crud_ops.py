import requests
import json


class CRUD():
    def get_data(self):
        r = requests.get ("https://jsonplaceholder.typicode.com/posts")
        return (r.json())



