#!/bin/bash
#take in url ad displays http methods server accepts
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
