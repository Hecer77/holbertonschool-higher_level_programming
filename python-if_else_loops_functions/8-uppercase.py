#!/usr/bin/python3
def uppercase(str):
    netice = ''
    for herf in str:
        if 'a' <= herf <= 'z':
            netice += chr(ord(herf) - 32)
        else:
            netice += herf
    print("{}".format(netice))
