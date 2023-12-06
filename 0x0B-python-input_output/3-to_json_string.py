#!/usr/bin/python3
# 333-to_json_string.py
# Ahmed Mahmoud - Gwaez
"""Defines a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a string object."""
    return json.dumps(my_obj)
