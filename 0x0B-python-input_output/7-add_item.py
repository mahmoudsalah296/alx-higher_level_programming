#!/usr/bin/python3
"""add argiments to python list"""
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


try:
    data = load_from_json_file("add_item.json")
except FileNotFoundError:
    save_to_json_file(sys.argv[1:], "add_item.json")
else:
    data += sys.argv[1:]
    save_to_json_file(data, "add_item.json")
