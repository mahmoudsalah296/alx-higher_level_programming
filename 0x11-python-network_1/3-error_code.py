#!/usr/bin/python3
"""error code"""


import sys
from urllib.request import urlopen
from urllib.error import HTTPError

if __name__ == "__main__":
    try:
        with urlopen(sys.argv[1]) as resp:
            print(resp.read().decode("utf-8"))
    except HTTPError as error:
        print(f"Error code: {error.code}")
