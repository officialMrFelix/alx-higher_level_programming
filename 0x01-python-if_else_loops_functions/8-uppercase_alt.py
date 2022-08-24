#!/usr/bin/python3
def uppercase(str):
    """"Changes a given string from lowercase to upppercase"""
    t = ''
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            t = t + chr(ord(i) - 32)
        else:
            t = t + i
    print("{}".format(t))
