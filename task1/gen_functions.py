"""simple functions to generate desired output per type"""

import random
import string
from datetime import datetime, timedelta

random.seed(datetime.today().microsecond)

def generate_date():
    """function generates a random date"""
    t = datetime.today()
    rand_days = random.randint(-10000,10000)
    new_date = t + timedelta(days=rand_days)
    return new_date.strftime('%Y-%m-%d %H:%M:%S')

def generate_boolean() -> bool:
    """function generates a random boolean"""
    choise = random.randint(0,1)
    #b = True if choise else False
    return bool(choise)

def generate_string(lenf: int) -> str:
    """function generates a random striung"""
    res = ''.join(random.choices(string.ascii_letters + string.digits, k=lenf))
    return res

def generate_float(pres: int) -> float:
    """function generates a random integer"""
    return round(random.random(), pres)

def generate_int(gen_range: int, is_positives_only: bool) -> int:
    """function generates a random integer""" 
    if is_positives_only:
        return random.randint(0, gen_range)

    return random.randint(-gen_range, gen_range)
