#!/bin/bash
#tk url, send POST req, disp response body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
