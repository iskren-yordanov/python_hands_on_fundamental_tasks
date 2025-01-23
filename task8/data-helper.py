"""simple functions to generate desired output per type"""

import random
import string
from datetime import datetime, timedelta

random.seed(datetime.today().microsecond)

def get_random_date():
    """function generates a random date"""
    t = datetime.today()
    rand_days = random.randint(-10000,10000)
    new_date = t + timedelta(days=rand_days)
    return new_date.strftime('%Y-%m-%d %H:%M:%S')

def get_random_string():
    """function generates a random striung"""
    lenf = 25
    res = ''.join(random.choices(string.ascii_letters + string.digits, k=lenf))
    return res

def get_random_integer():
    """function generates a random integer""" 
    return random.randint(-1000000, 100000)

def get_random_double():
    """function generates a random integer"""
    return random.random()
