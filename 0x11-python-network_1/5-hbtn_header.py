#!/usr/bin/python3
"""
sends a request to the URL and displays the value of the variable X-Request-Id
"""

import requests
import sys

response = requests.get(sys.argv[1])
print(response.headers.get("X-Request-Id"))
