import csv
import os
import re
import sys


def parse_file(path):
    line_regex=re.compile("Word -> .*")
    just_word = re.compile("Word -> .*? (?=[(])")
    all_words = []
    with open(path) as f1: 
        lines =f1.readlines()

    for i, line in enumerate(lines):
        # get lines starting with word -> ...
        s = line_regex.search(line)
        if s is not None:
            # get the word
            word_string = just_word.search(s.group(0))
            if word_string is not None:
                word = word_string.group(0)[7:]
            # split it up, get the onsets and nuclei

            syl_strings = get_syls(s.group(0))

            if syl_strings is not None:
                syllabified_word = ""
                for s in syl_strings:
                    syl = process_syl(s)
                    syllabified_word += syl + " "
                if syllabified_word == "":
                    print(line)    
                all_words.append(syllabified_word) 

            else:
                print(s.group(0))
    
    return all_words
def get_syls(string):
    just_syl = re.compile("Syl -> .*?(?=(, Syls ->)|\))")

    return [x.group(0) for x in just_syl.finditer(string)]


def process_syl(string):
    onset_regex = re.compile("Onset -> \'.*\'.*")
    rhyme_regex = re.compile("Rhyme ->.*")
    nucleus_regex = re.compile("Nucleus -> \'.*\'")
    coda_regex = re.compile("Coda -> \'.*\'")

    o = onset_regex.search(string)
    onset,nucleus, coda=None,None,None
    if o is not None:
        onset = re.sub("[\',]", "",o.group(0).split(" ")[2])
    r = rhyme_regex.search(string)
    if r is not None:
        n = nucleus_regex.search(r.group(0))
        if n is not None:
            nucleus = re.sub("[\',]", "", n.group(0).split(" ")[2])
        else:
            print(r.group(0))
        c = coda_regex.search(r.group(0))
        if c is not None:
            coda = re.sub("[\',]", "", c.group(0).split(" ")[2])
    else:
        return ""
    toret = "" 
    if onset is not None:
        toret+= onset    
    toret+= nucleus
    if coda is not None:
        toret+= coda


    return toret


if __name__ == '__main__':
    f2 = open("syllabified", "w")
    file_regex = re.compile("infag.*")
    directory = sys.argv[1]    
    for dir in os.walk(directory):
        for file in dir[2]:
            if file_regex.match(file):
                path = os.path.join(dir[0],file)
                all_words = parse_file(path)
                for w in all_words:
                    f2.write(w + "\n")
    f2.close()
