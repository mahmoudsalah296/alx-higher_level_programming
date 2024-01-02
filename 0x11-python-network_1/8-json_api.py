#!/usr/bin/python3
"""search api"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""
    response = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})
    try:
        response_json = response.json()
        if len(response_json) == 0:
            print("No result")
        else:
            print(f'[{response_json["id"]}] {response_json["name"]}')
    except Exception:
        print("Not a valid JSON")
