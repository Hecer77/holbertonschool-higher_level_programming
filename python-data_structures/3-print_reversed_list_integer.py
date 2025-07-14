#!/usr/bin/python3
def print_list_integer_reverse(my_list=[]):
    """
    Print all integers of a list in reverse order.

    Args:
        my_list (list): List of integers.
    """
    for number in reversed(my_list):
        print("{:d}".format(number))




print_list_integer_reverse([1, 2, 3, 4, 5])
