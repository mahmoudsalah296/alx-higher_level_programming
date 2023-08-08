#!/usr/bin/python3
def uppercase(str):
    for i in str:
        print(chr(ord(i) - 32) if ord(i) in range(97, 123) else i, end="")
    print("")
