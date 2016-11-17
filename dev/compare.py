import sys


file1 = sys.argv[1]
file2 = sys.argv[2]

with open(file1) as f1:
    lines1 = f1.readlines()
with open(file2) as f2:
    lines2 = f2.readlines()

print(len(lines1), len(lines2))
assert(len(lines1) == len(lines2))

