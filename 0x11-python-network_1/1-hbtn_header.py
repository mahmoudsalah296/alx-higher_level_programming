#!/usr/bin/python3
"""respose header"""


import sys
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as resp:
        print(resp.headers.get("X-Request-Id"))
