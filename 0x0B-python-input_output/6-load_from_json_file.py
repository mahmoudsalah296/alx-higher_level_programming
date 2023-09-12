#!/usr/bin/python3
"""load from json file"""
import json


def load_from_json_file(filename):
    """load from json file"""
    with open(filename) as f:
        return json.load(f)
