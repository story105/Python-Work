#For Atamian Lab
choiceList = [9,21]
indentList = []
f=open("AtamianTxt.txt")
g=open("AtamianTxt.txt")
def keyLine( linenumber ): 
	ii=0
	for a,line in enumerate(f): #find away around enumerating the whole file
		if line[0] == '>':
			#print ("found")
			indentList.append(a)
	lines = g.readlines()
	#print indentList
	for ii in linenumber:
	#	linemax = ii+5
		while (ii> -1):
			if (ii not in linenumber) and ((ii) in indentList): 
				#print ("it broke at the first line")
				ii = -40
				break;
	#		if (ii > linemax): #will print one line past this
	#			print("linemax break")
	#			ii=-400
	#			break;
			else:
				#if (a-ii in linenumber):
					#print(ii)
				print(lines[ii])
					#break;
			ii=ii+1
	#return;
	
number=set(choiceList)

o=open('ResultsAtamian.txt','w')
print(number)
keyLine(number)
f.close()
g.close()
o.close()
