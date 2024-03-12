#!usr/bin/Python3
"""
    Defines a python module
"""

def read_file(filename=""):
"""
    read_file function
    reads the UTF-8 format
"""
    with open(filename, mode='r', encoding="utf-8") as file:
	    read_data = file.read()
	    print(read_data, end='')

    file.closed
