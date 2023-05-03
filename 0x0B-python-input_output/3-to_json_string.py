#!/usr/bin/pyhton3
import json
"""function that returns the JSON representation
   of an object (string):
"""


def to_json_string(my_obj):
    """converts an obj to json format"""

    json_string = json.dumps(my_obj)
    return json_string
