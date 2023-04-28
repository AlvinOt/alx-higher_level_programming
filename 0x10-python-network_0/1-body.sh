#!/bin/bash
#take in url, send GET req, disp resp body
curl -sfL "$1" -X GET
