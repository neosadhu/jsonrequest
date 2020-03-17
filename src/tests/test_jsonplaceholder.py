import sys
import os
p = os.path.abspath(os.path.join(__file__,"../../.."))
sys.path.insert(0,p)
from src.tests.test_get_json import lib

def test_1():
    assert lib().status_code ==200