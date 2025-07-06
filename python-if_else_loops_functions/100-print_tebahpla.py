#!/usr/bin/python3


def print_reverse_alphabet():
    print("".join(
        "{}{}".format(chr(c), chr(c - 1).upper())
        for c in range(122, 96, -2)
    ), end="")


print_reverse_alphabet()

