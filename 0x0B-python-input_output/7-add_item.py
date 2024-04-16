#!/usr/bin/python3
"""Adds all arguments to a Python list,
and then save them to a file as json.
"""
import json
import sys
from os import path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


args = sys.argv[1:]
filename = "add_item.json"


if path.exists(filename):
    current_list = load_from_json_file(filename)
    save_to_json_file([*args, *current_list], filename)
else:
    save_to_json_file(args, filename)
