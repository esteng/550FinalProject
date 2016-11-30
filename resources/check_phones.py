#!/usr/bin/python
# -*- coding: utf8 -*-

import os
import csv
import math

words = {}
phones = set()



with open("../dev/French/train.dat",'r') as f:
    lines = f.readlines()

for i,line in enumerate(lines):
    if i == 0: 
        continue
    splitline = line.split(' ')

    [phones.update(x.strip()) for x in splitline]

vs = 'aiyuoOeE02951@3'
cs= 'pbtdlkgfvszSZmnNRxG'
ls = 'j8w'


original = set([x for x in vs+cs+ls])

for o in original:
    if o in phones:
        continue
    else:
        print("{} not in phones".format(o) )

to_add = ""
for o in phones:
    if o in original:
        continue
    else:
        to_add+=o
        print("{} not in original".format(o) )
 
print(to_add)     