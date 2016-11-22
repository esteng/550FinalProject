#!/usr/bin/python
# -*- coding: utf8 -*-

import sys 

header = "% non-terminals\n\
Word ->  Syls\n\
Syls ->  Syl\n\
Syls ->  Syl Syls\n\
\
\n\
% adapted non-terminals\n\
@ Word 1500 100 0\n\
\
Syl ->  Rhyme\n\
Syl ->  Onset Rhyme\n\
Rhyme -> Nucleus\n\
Rhyme -> Nucleus Coda\n\
Onset -> Consonant\n\
Onset -> Consonant Consonants\n\
Coda -> Consonant\n\
Coda -> Consonant Consonants\n\
Consonants -> Consonant\n\
Consonants -> Consonant Consonants\n\
\n\
\n\
% terminals\n"

def write_grammar(syllabics, nonsyllabics, file, liquids=None):
    with open(file, "w") as f1:
        f1.write(header)

        for vowel in syllabics:
            if vowel == "°":
                vowel = '0'
            f1.write('Nucleus -> "{}"'.format(vowel) + "\n")
        for c in nonsyllabics:
            f1.write('Consonant -> "{}"'.format(c)+ "\n")

        if liquids:
            for seg in liquids:
                f1.write('Nucleus -> "{}"'.format(seg)+ "\n")

try:
    write_grammar(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
except IndexError:
     write_grammar(sys.argv[1], sys.argv[2], sys.argv[3])
