import string
f=open('Lexique381.txt');
corpusArray=[[0 for j in range(4)] for i in range(142696)]
i=0
myList=[]
for line in f:
	myList=line.split("\t");
	#skip any of the weird cases where the spaces will mess up the parser
	if(len(myList)>35):
		continue
	if(len(myList)<24):
		continue
	#first we get the orthographic transcription
	corpusArray[i][0]=myList[0]
	#next we get the phonetic transcription with dashes
	corpusArray[i][1]=myList[8]	
	#next we get the CV
	corpusArray[i][2]=myList[22]
	#next we get the frequency
	corpusArray[i][3]=myList[24]
	i=i+1
w=open('corpus.txt', 'w')
for x in corpusArray:
	w.write(str(x[0])+' ')
	w.write(str(x[1])+' ')
	w.write(str(x[2])+' ')
	w.write(str(x[3])+' ')
	w.write('\n')
w.close()
f.close()
