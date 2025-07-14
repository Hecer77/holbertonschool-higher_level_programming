#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    Print all integers of a list in reverse order.

    Args:
        my_list (list): List of integers.
    """
    for number in reversed(my_list):
        print("{:d}".format(number))




print_reversed_list_integer([1, 2, 3, 4, 5])
