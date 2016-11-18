
f1= open("truth.dat") 
lines = f1.readlines()
s = set(lines)
l = list(s)
f2 = open("real_sylls","w")
for x in l:
    f2.write(x )