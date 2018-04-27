#Encription code 
#Having some logic isues on decrypting the same file that is encrypted: Issue with special characters...
#Will get to working on where the logical issue falls



import collections #for decrypt

tryCatch = False #boolean loop in main
mainLoop = "notDone"
def getKey():
	key = 0
	while True:
		print('Enter the key number (1-26)')
		key = (int(input())%26)
		if (key >= 1 and key <= 26):
			return key

			#'z' = 122 "A" = 65
def encrypt(FileName, OFFSET):
	d = OFFSET
	charInFile = ""
	f = open('encrypted.txt', 'w')
	for line in FileName:   #iterate over the text
		line = line.strip()
		charInFile = "" #reset each line
		for i in line:
			if (i.isalpha()):
				num = ord(i)
				num += d 
				x = 0
				if (num > ord('z')):
					x = num - ord('z')
					num = ord('a') + x
					charInFile += (chr(num)) #something with logic here
				elif (num > (ord('Z')) and num < (ord('z')+1)):
					charInFile += (chr(num))
				elif (num > (ord('A')) and (num < (ord('Z')))):
					charInFile += (chr(num))
					#This shouldnt ever happen since we add
			else:
				charInFile += (i) #if its a space just add it or special char
		f.write(charInFile) #write each line

	f.close()
	print ("Encrypted File is complete")

	
mostCommon = ""
def decrypt(decryptFile):
	df = decryptFile
	wah = open('decrypted.txt', 'w')
	mostCommon = ""
	stringFile = ""
	ordValue = 65
	checkValue = ord('e')
	resetValue = 0
	num = 0
	
	d = collections.defaultdict(int)
	for line in df:
		for i in line:
			if (i != ' '):
				#mostCommon = (collections.counter(stringFile).most_common(1)[0])
				d[i] += 1
	print ("most common character is ", sorted(d.items(), key = lambda x: x[1], reverse = True)[0])
	valueE = (ord('e'))
	MostCommon = (sorted(d.items(), key = lambda x: x[1], reverse = True)[0])
	mostCommon = MostCommon[0] #take char in tuple above
	ordValue = ord(mostCommon)
	resetValue = ordValue - checkValue 
	df.close()
	df = open('encrypted.txt', 'r')
	for line in df:
		for i in line:
			if (i != ' '):
				num = ord(i) - resetValue
				if (num < ord('A')):
					num = ord('A') - num
					num = ord('z') - num
				#elif (num >)
				stringFile += (chr(num))
		#print (stringFile)
	wah.close()
	print ("decrypted file is complete")
	
	
	
	
#put this in main
while(tryCatch == False):
	try:
		userFile = raw_input("Yo choose a file to read: (Ex: encryptThis.txt) ") 
		file1 = open(userFile, 'r')
		tryCatch = True
	except FileNotFoundError:
		print ("could not find file. Try again")
		tryCatch = False

while (mainLoop != "done"):
	offsetDistance = raw_input ("Want to offset a particular distance in encryption? (Y/N)  ")
	if (offsetDistance.upper() == 'Y'):
		OFFSET = getKey()
	elif (offsetDistance.upper() == 'N'):
		OFFSET = 2
	else:
		print ("no clue what you wanted offset distance is now set to 'preset'")
		OFFSET = 2
	encrypt(file1, OFFSET)
	f = open('encrypted.txt', 'r')
	decrypt(f)
	f.close()
	mainLoop = "done"
	
	
	
	
	
	
	
	
	