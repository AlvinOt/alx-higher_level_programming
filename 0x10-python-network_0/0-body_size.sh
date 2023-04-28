#!/bin/bash
#take in a url, send it a request, display response body size
curl -s "$1" | wc -c
