#!/bin/bash
# display body size of response of curl command
curl -s -I "$1" | grep 'Content-Length' | cut -f2 -d ' '
