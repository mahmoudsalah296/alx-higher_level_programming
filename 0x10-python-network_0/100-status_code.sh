#!/bin/bash
# displays only the status code of the response.
curl -I -s -o /dev/null -w "%{http_code}" "$1"
