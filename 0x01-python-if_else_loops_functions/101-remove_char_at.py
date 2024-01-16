#!/usr/bin/python3

def remove_char_at(str, n):
    # Check if the index n is within the valid range
    if n >= 0 and n < len(str):
        # Use string slicing to remove the character at position n
        return str[:n] + str[n + 1:]
    else:
        # If the index is out of range, return the original string
        return str
