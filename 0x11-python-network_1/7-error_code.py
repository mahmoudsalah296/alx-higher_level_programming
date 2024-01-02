#!/usr/bin/python3
"""error code"""

import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if response:
        print(response.text)
    else:
        print(f"Error code: {response.status_code}")
