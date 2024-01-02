#!/usr/bin/python3
"""respose header"""


import sys
from urllib.request import urlopen
from urllib.parse import urlencode

if __name__ == "__main__":
    data = {"email": sys.argv[2]}
    data_parsed = urlencode(data)
    data_encoded = data_parsed.encode("utf-8")

    with urlopen(sys.argv[1], data=data_encoded) as resp:
        print(resp.read().decode("utf-8"))
