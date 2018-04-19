#need two functions, wordtoPig and nameToPig
#to return two things, we can return both as a tuple #return (firstName, lastName) and then unpack after

ay = "ay" #will just add this to end of strings
vowelPlace = 0 #will iterate through string
charCheck = 'z' #just need a consenant
Checkcounter = 0
boolCheck = False #whatv
char = ''

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

UsersFirstName = raw_input("Please enter a first name: ")
UsersLastName = raw_input("Please enter a last name: ")
my_newFirst, my_newLast = nameToPig(UsersFirstName, UsersLastName)
print(my_newFirst.title() + " " + my_newLast.title()) #stack overflow so nice, taught me .title()
	
	
	
	
	
	
	
	

