#!/usr/bin env python3

import os

with open("mydata.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("mary was amuse\nWhy?\nCause the quick brown fox jumped")


with open("mydata.txt", encoding="utf-8") as myFile:

    print(myFile.read())
