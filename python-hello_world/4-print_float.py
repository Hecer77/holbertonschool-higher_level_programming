#!/usr/bin/python3
def print_float(number):
    if type(number) == float:
        print(f"Float: {number:.2f}")
    else:
        print("Wrong type")

if __name__ == "__main__":
    print_float(333.12)   # positive float
    print_float(-45.678)  # negative float
    print_float(0.0)      # zero float
    print_float("hello")  # wrong type
