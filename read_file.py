# -*- coding: utf-8 -*-
"""
reading from files
example: echo -e "Yo.\n My name is Joao." | python read_file.py
"""
import sys

lines=sys.stdin.readlines()

for l in lines:
    print(l)
    s=len(l)
    print("length: "+str(s))

