import sys


file1 = sys.argv[1]
file2 = sys.argv[2]

with open(file1) as f1:
    lines1 = f1.readlines()
with open(file2) as f2:
    lines2 = f2.readlines()

print(len(lines1), len(lines2))

unfound = 0
for line in lines1:
    found = False
    for line2 in lines2:
        if line.strip() == line2.strip():
            print("{} matches to {}".format(line.strip(), line2.strip()))
            found = True
            break
    if not found:
        unfound +=1
        print("{} has no match".format(line.strip()))

print("{} remained unmatched".format(unfound))