#hangman game
import random


wordlist=["chapman","machine","learning","computer","python","california",
          "jellybeans","coffee","laboratory","disneyland","library", "freedom",
		  "happiness", "majority", "vexing", "undulation", "periphery", "exultant",
		  "jeering", "trampoline","weirdo","blondie","bowtie","controller","completion"]
index=random.randint(0, len(wordlist) - 1) #selects a random integer from range of list
correctword=wordlist[index]
#declaring variables
maxGuesses = len(correctword) + 5
guessCounter = 0
sofar= []
win = False 
wordLetters = 0
whileloop = False
mainLoop = True
guessList = []

for char in correctword:
	sofar.append("_") #makes the list have only Dashes
	wordLetters = wordLetters + 1
#display the length of wordlist (done in loops)
# print(sofar)
# print(" ".join(sofar)) #joins the elements in sofar into a string

print("Hangman game! Let's begin")
print("*+_______________________________________________________+*\n")

def findInd(string, char):
	return [i for i, letter in enumerate(string) if letter == char]
	#This will be called to find all indexes of letter in CorrectWord. 

def find_letter(list):
    if not list:          
        return 0

    elif list[0] == l:  #check first element here for guessed letter
        return True

    elif find_letter(list[1:]):  # checked the first element, skip it and return the other elements of the list
        return True

    else: 
        return False

while (mainLoop == True):
	print ('The word to guess: ',  " ".join(sofar), wordLetters, "letters long")
	letter = raw_input("guess a letter: ")
	guessCounter = guessCounter +1
	
	l = letter
	if (find_letter(guessList) == True):
			print("You already guessed that letter!")
			guessCounter = guessCounter -1
			continue
	else:
		guessList.append(letter)
	
	for char in correctword:
		if letter == char:
			whileloop = True
			mainLoop = True
			
	if whileloop == False:
		print ("That letter is not in the word! Guess again. \n")
		mainLoop = True
		
		#will skip this loop if letter is wrong
	while (whileloop == True):
		for num in (findInd(correctword, letter)): #returns list of indexes
			sofar[num] = letter #Replaces the places in sofar with char
		whileloop = False;	
			#if (letter == char): 
				#index = correctword.find(letter)
				#sofar[index] = letter
	
	print("*+_______________________________________________________+*\n") 
	
	count = sofar.count("_")
		
	if count == 0:
		win = True
		break #exits the main while loop
			
	guessList.sort()
	print ("you have guessed these letters: ", guessList)
	print ("Guesses left: ", (maxGuesses-guessCounter))
	if guessCounter == maxGuesses:
		break #User has used all the guesses and not won.
		
#outside of While loop

if win == True:
	print ("CONGRADULATIONS! You won. The word was ", correctword)
	print (" Thanks for playing")
else:
	print ("heh you lose... Try again some time")
	print ("The word was ", correctword)