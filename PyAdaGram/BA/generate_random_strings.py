import random
import csv
# syls of format CV or V
maxlength = 8

f1 =  open("train.dat", "w")
f1cw = csv.writer(f1, delimiter = " ")
#write 500 words
for i in range(10000):
    word = []
    length = random.randrange(2, maxlength)
    for j in range(length):
        #either BA or just A
        choice = random.randint(0,1)
        if choice == 0:
            syl = "B"
        else:
            syl = "A"
        word.append(syl)
    f1cw.writerow(word)



lines = []
with open("train.dat") as f2:
    lines = f2.readlines()
    for line in lines:
        line = line.strip()

with open('train.dat', 'w') as f3:
    for line in lines:
        f3.write(line)
