#!/usr/bin/python3
def islower(c):
    """Check if a character is lowercase (a-z) without using str methods."""
    if not isinstance(c, str) or len(c) != 1:
        raise TypeError("Expected a single character string")
    return ord('a') <= ord(c) <= ord('z')
