#!/usr/bin/python3
for i in range(0, 100):
    if i == 99:
        print(str(i))
    else:
        print(str(i).zfill(2), end=", ")
