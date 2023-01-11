#!/usr/bin/python3
"""
This module adds all arguments to a Python List
and then save them to a file.
"""


from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

file_handle = "add_item.json"

try:
    file_content = load_from_json_file(file_handle)
except FileNotFoundError:
    file_content = []

save_to_json_file(file_content + argv[1:], file_handle)
