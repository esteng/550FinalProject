#!/usr/bin/python
# -*- coding: utf8 -*-
mapping = {}
with open("../../resources/syllabified/Lexique381.txt") as f2:
    lines = f2.readlines()

with open("lexique_syllabified","w") as f3:
    for line in lines:
        syllabification = line.split("\t")[22]
        syllabification = syllabification.replace('§', '3').replace('Â', 'A').replace('°','0').replace("-"," ")
        word = syllabification.replace(" ","")
        mapping.update({word:syllabification})

    for k,v in mapping.items():
        f3.write(k + ":" +v + "\n")


with open("../French/train.dat", 'w') as f4:
    for i,k in enumerate(mapping.keys()):
        if i == 0:
            continue;
        f4.write(" ".join(k) + "\n")



