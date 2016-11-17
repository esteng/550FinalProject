import csv
f1 =  open("truth.dat", "w")
f1cw = csv.writer(f1, delimiter = " ")
with open("train.dat") as f2:
    lines = f2.readlines()

for line in lines:
    toadd = []
    split = [x.strip() for x in line.split(" ")]

    it = iter(split)
    for c in it:
        if c == 'B':
            try:
                toadd.append(c+next(it).strip())
            except StopIteration:
                print(line)
        elif c!= " " and c!= "":
            toadd.append(c)

    f1cw.writerow(toadd)

