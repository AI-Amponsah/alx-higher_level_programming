#!/usr/bin/python3
""" function that creates an Object
    from a “JSON file”:
"""
import json


def load_from_json_file(filename):
    """creates obj from  json"""

    with open(filename, 'w', encoding='utf-8') as f:
        return json.loads(f.read())
