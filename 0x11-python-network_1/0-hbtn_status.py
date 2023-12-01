#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
    body = resp.read()
    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
    print(f"\t- utf-8 content: {body.decode('UTF-8')}")
