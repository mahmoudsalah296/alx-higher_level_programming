#!/usr/bin/python3
"""respose header"""


import sys
import urllib.request

with urllib.request.urlopen(sys.argv[1]) as resp:
    print(resp.headers.get("X-Request-Id"))
