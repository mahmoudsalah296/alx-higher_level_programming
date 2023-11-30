#!/bin/bash
# display body size of response of curl command
# curl -s "$1" | wc -c -> content size means number of characters inside the page
# another answer
curl -s -I "$1" | grep 'Content-Length' | cut -f2 -d ' '
