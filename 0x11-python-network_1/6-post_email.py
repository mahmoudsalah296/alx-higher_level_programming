#!/usr/bin/python3
"""
akes in a URL and an email address, sends a POST request to the passed URL
with the email as a parameter
"""

import requests
import sys

if __name__ == "__main__":
    response = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    print(response.text)
