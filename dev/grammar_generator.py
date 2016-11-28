header = "% non-terminals\
Word ->  Syls\
Syls ->  Syl\
Syls ->  Syl Syls\
Syl ->  Rhyme\
Syl ->  Onset Rhyme\
Rhyme -> Nucleus\
Rhyme -> Nucleus Coda\
Onset -> Consonant\
Onset -> Consonant Consonants\
Coda -> Consonant\
Coda -> Consonant Consonants\
Consonants -> Consonant\
Consonants -> Consonant Consonants\
\
% adapted non-terminals\
@ Word 1500 100 0\
\
\
% terminals"

def write_grammar(syllabics, nonsyllabics, file, liquids=None):
    with open(file, "w") as f1:
        f1.write(header)

        for vowel in syllabics:
            f1.write('Nucleus -> "{}"'.format(vowel))
        for c in nonsyllabics:
            f1.write('Consonant -> "{}"'.format(c))

        if liquids:
            for seg in liquids:
                f1.write('Nucleus -> "{}"'.format(seg))
