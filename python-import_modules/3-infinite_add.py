#!/usr/bin/python3
import sys




def main():
    args = sys.argv[1:]

    if len(args) == 0:
        print(0)
        return

    total = 0

    for arg in args:
         total += int(arg)
         
    print(total)



if __name__ == "__main__":
    main() 
