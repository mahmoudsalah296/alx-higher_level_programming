#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    print(len(argv) - 1, end=" ")
    if len(argv) == 2:
        print("argument:")
    else:
        print("arguments", end="")
        if len(argv) == 1:
            print(".")
        else:
            print(":")
    for i in range(1, len(argv)):
        print("{:d}: {:s}".format(i, argv[i]))
