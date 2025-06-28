#!/usr/bin/python3
def islower(c):
    """Check if a character is lowercase (a-z) without using str methods."""
    if not isinstance(c, str) or len(c) != 1:
        raise TypeError("Expected a single character string")
    return ord('a') <= ord(c) <= ord('z')


print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))
