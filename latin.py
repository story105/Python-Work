#to return two things, we can return both as a tuple #return (firstName, lastName) and then unpack after
#Added file reading and exception handling to assignment: will output to a file also
ay = "ay" #will just add this to end of strings
vowelPlace = 0 #will iterate through string
charCheck = 'z' #just need a consenant
Checkcounter = 0
boolCheck = False #whatv
char = ''
tryCatch = False  #new 


def CheckString(userString): #was thinking... gotta make sure the "word" is not just "tttttttt"
	Checkcounter = 0
	for char in userString:
		if (char in ('aeiou')):
			Checkcounter = Checkcounter + 1
	if (Checkcounter > 0 ):
		return True
	else:
		return False

def wordToPig(userString):
	if len(userString) > 0 and userString.isalpha(): #make sure it's a word with only alphabetic characters
		string = userString.lower() 
		first = string[0]
		boolCheck = CheckString(string)
		charCheck = 'z'
		vowelPlace = 0 #will iterate through string
		#print ("made it int WordtoPig")
		if (boolCheck == True): #make sure it's a word with vowels
			#print ("made it past BoolCheck")
			if first in ('aeiou'): #sick vowel check
				first.upper()
				finalString = first + string[1:] + "y" + ay
				return finalString
			else:
				while (charCheck not in ('aeiou')):
					vowelPlace = vowelPlace + 1 
					charCheck = string[vowelPlace]
				first = string[vowelPlace]
				first.upper()
				finalString = first + string[(vowelPlace+1):] + string[:vowelPlace] + ay
				return finalString
		else: 
			return "That word has no vowels"
	else:
		return "empty"
		
def nameToPig(firstName, lastName):
	newFirstName = wordToPig(firstName)
	newLastName = wordToPig(lastName)
	return [newFirstName, newLastName] 

question1 = 1 
listOfNames = []
userChoice = ""
listOfPigLatinNames = [] #Total first last before printing to file
PigNameIntermediate = "" #string of each FULL name to append to listOfPigLatinNames
counter = 0
#main loop
while (question1 == 1):
	userChoice = raw_input("Do you want to read from a file? 'No' = input a name (Y/N) or 'EXIT'?\n")
	if (userChoice.upper() == "Y"):
		while(tryCatch == False):
			try:
				userFile = raw_input("Yo choose a file to read: (Ex: encryptThis.txt) \n") 
				file1 = open(userFile, 'r')
				tryCatch = True
			except FileNotFoundError:
				print ("could not find file. Try again")
				tryCatch = False
		wah = open('results_latin.txt', 'w')
		with open(userFile, mode = 'r') as file:
			listOfNames = file.read().splitlines() #creates a full list
			#print (listOfNames)
			for names in listOfNames:
				#iterate through list of "Chuck Durham" with spaces (issue)
				words = names.split() #returns a list of just two strings, first and last
				for word in words: #gets each name
					newName = wordToPig(word).title() #title() is a godsend
					PigNameIntermediate = (PigNameIntermediate + newName + " ")
				listOfPigLatinNames.append(PigNameIntermediate[:-1]) #ignore the extra space at end
				PigNameIntermediate = "" #reset after each name 
				#print (listOfPigLatinNames)
		while (counter != len(listOfPigLatinNames)):
			wah.write(listOfPigLatinNames[counter])
			wah.write("\n")
			counter = counter + 1 #keep going up writing to the file per line per index in list
		wah.close()
		print ("File 'results_latin.txt' has been created")
	elif (userChoice.upper() == "N"):
		UsersFirstName = raw_input("Please enter a first name: ")
		UsersLastName = raw_input("Please enter a last name: ")
		my_newFirst, my_newLast = nameToPig(UsersFirstName, UsersLastName)
		print(my_newFirst.title() + " " + my_newLast.title()) #stack overflow so nice, taught me .title()
	elif (userChoice.lower() == "exit"):
		print ("thanks for using the 'gram.")
		break
	else:
		print ("Yo could not understand what you wanted, let's retry ")
		question1 = 1
		userChoice = ""
	

	
	
	
	
	
	
	

