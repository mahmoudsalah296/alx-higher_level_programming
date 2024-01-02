#!/usr/bin/python3
"""a script that fetches https://alx-intranet.hbtn.io/status"""


import requests

response = requests.get("https://alx-intranet.hbtn.io/status")
body = response.content.decode()
print("Body response:")
print(f"\t- type: {type(body)}")
print(f"\t- content: {body}")
