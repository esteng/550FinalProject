#! /bin/env python

"""Maps br-phono.txt to the input required by py-cfg"""

import sys
import lx

whitespace = "\r\n\t "

def file_brentformat(inf, outf):
    for line in inf:
        first = True
        for char in line:
            if char in whitespace:
                continue
            if not first:
                outf.write(' ')
            outf.write(char)
            first = False
        outf.write('\n')

if __name__ == "__main__":
    file_brentformat(sys.stdin, sys.stdout)
