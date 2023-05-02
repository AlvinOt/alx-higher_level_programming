#!/bin/bash
# send request to URL & only display response status code
curl -s -o /dev/null -w "%{http_code}" "$1"
