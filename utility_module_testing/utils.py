import json
from datetime import datetime

def sum_numbers(a, b):
    return a+b

def create_user(name, age):
    return{"name":name, "age":age, "created_at":datetime.now()}


def filter_adults(users):
    return[user for user in users if user["age"] >= 18]


def find_in_list(list, value):
    return value in list


def parse_json(json_string):
    if not json_string:
        return ValueError("no JSON string provided")
    return json.loads(json_string)



def approximate_division(a, b):
    return a/b