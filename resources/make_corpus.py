#!/usr/bin/python
# -*- coding: utf8 -*-

import os
import csv
import math

words = {}



with open("syllabified/Lexique381.txt") as f:
    lines = f.readlines()

for i,line in enumerate(lines):
    if i == 0: 
        continue
    splitline = line.replace("°","0").replace("Â","A").replace("§","3").split("\t")
    words[splitline[1].strip()] = splitline[8].strip()

with open("french","w") as f1:
    for k,v in words.items():
        if math.ceil(float(v)) != 0:
            f1.write(" ".join([c for c in k]) + "\n")


