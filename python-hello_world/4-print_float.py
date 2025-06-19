#!/usr/bin/python3
# -*- coding: utf-8 -*-

def print_float(number):
    if type(number) is float:
        print(f"Float: {number:.2f}")
    else:
        print("Wrong type")

print_float(333.12)    # Positive float
print_float(-98.12)    # Negative float
print_float(0.0)       # Zero
print_float("test")    # Wrong type

         Ä
