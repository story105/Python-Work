#BattleGame
import random 
rockDamage = random.randint(1,10)
paperDamage = random.randint(1,10)
scizzorDamage = random.randint(1,10)

if (scizzorDamage == rockDamage):
	rockDamage = rockDamage +1
if (scizzorDamage == paperDamage):
	scizzorDamage = scizzorDamage + 1 #just general preferences
if (paperDamage == rockDamage):
	paperDamage = paperDamage + 1 #makesure it's not gnna be stuck tieing
	if (scizzorDamage == rockDamage):
		rockDamage = rockDamage +1 #got an error of scizzors = Rock damage. Some mathematical so added this in loop fixed
	
moves = [("rock", rockDamage),("paper", paperDamage)]
gameLoop = True
Turn = False
turn2 = False
turn3 = False
turn23Loop = False
checkValid = False
checkValid2 = False
moveStrength = 0

while (gameLoop == True):
	print ("Are you ready? FIGHT!")
	print ("Starting moves are 'rock' and 'paper'")
	print ("3")
	print ("2")
	print ("1")
	while (Turn == False):
		moveChoice = raw_input("FIGHT! Choose a move or type 'exit': ").lower()
		if (moveChoice == "exit"):
			break
		for key, value in moves:
			if key == moveChoice: #and key == computerChoice
				moveStrength = value
				Turn = True
		if (moveStrength == 0): #did not find the key (doesn't exist)
			print ("That is not a valid choice! Choose again fighter")
			Turn = False
		#outside turn while loop
	if (moveChoice == "exit"):
		break
	computerMove = random.randint(0, len(moves) - 1)
	computerChoice = moves[computerMove]
	a, computerStrength = computerChoice #assigns computerStrength to the value not key (a)
	
	#the "fighting" happens here
	if (moveStrength > computerStrength):
		print ("You've won! Your first opponent is wrapped up")
		moves.append(("scizzors", scizzorDamage)) 
		print ("You've leveled up! Learned 'scizzors'")
		turn2 = True
		Turn = True
		turn23Loop = True
	elif (moveStrength < computerStrength):
		print ("You've LOST. Restarting round one")
		turn2 = False
		Turn = False
	else:
		print ("You tied: pick another move!")
		turn2 = False
		Turn = False
	while (turn23Loop == True):
		while (turn2 == True):
			#Second round!
			moveStrength = 0
			checkValid = False
			while (checkValid == False):
				moveChoice = raw_input("FIGHT! Choose a move or type 'exit': ").lower()
				if (moveChoice == "exit"):
					break
				for key, value in moves:
					if key == moveChoice: #and key == computerChoice
						moveStrength = value
						checkValid = True
				if (moveStrength == 0): #did not find the key (doesn't exist)
					print ("That is not a valid choice! Choose again fighter")
					checkValid = False
			if (moveChoice == "exit"):
				break #Have to break both while loops
			computerMove = random.randint(0, len(moves) - 1)
			computerChoice = moves[computerMove]
			a, computerStrength = computerChoice 
		
			if (moveStrength > computerStrength):
				print ("You've won! Your second apponent is toast")
				moves.append(("shoot", 8)) 
				print ("You've leveled up! Learned 'shoot'")
				turn2 = False
				Turn = True
				turn3 = True #advance to next while loop
			elif (moveStrength < computerStrength):
				print ("You've LOST. You've been dropped one round, and forgotten 'scizzors'") 
				del moves[-1:]
				turn2 = False
				Turn = False
				turn3 = False
				turn23Loop = False
			else:
				print ("You tied: pick another move!")
				turn2 = True
				turn3 = False
				turn23Loop = True
				#Third and final round!
		while (turn3 == True):
			moveStrength = 0 #Only to check the if statement in 11 lines
			checkValid2 = False
			while (checkValid2 == False):
				moveChoice = raw_input("FIGHT! Choose a move or type 'exit': ").lower()
				if (moveChoice == "exit"):
					break
				for key, value in moves:
					if key == moveChoice: #and key == computerChoice
						moveStrength = value
						checkValid2 = True
				if (moveStrength == 0): #did not find the key (doesn't exist)
					print ("That is not a valid choice! Choose again fighter")
					checkValid2 = False
				#outside turn while loop
			if (moveChoice == "exit"):
				break #Have to break all while loops
			computerMove = random.randint(0, len(moves) - 1)
			computerChoice = moves[computerMove]
			a, computerStrength = computerChoice #assigns computerStrength to the value not key (a)
			#for key, value in computerChoice:
				#computerStrength = value
			#the "fighting" happens here
		
			if (moveStrength > computerStrength):
				print ("You've won! Your final opponent is space dust") 
				userInputted = raw_input("Would you like to play again? (Y/N) ")
				userInputted.lower()
				if (userInputted == 'y'):
					Turn = False 
					turn2 = False
					turn3 = False 
					turn23Loop = False
					gameLoop = True #restarts all the way at top while
				else:
					turn2 = False
					Turn = True
					turn3 = False 
					turn23Loop = False
					gameLoop = False #Exit ALL while loops
			elif (moveStrength < computerStrength):
				print ("You've LOST. You've been dropped one round, and forgotten 'shoot'")
				del moves[-1:]
				turn2 = True
				Turn = True
				turn3 = False
				turn23Loop = True #new loop added to keep it from returning up to initial game loop
			else:
				print ("You tied: pick another move!")
				turn2 = False 
				turn3 = True
				checkValid2 = False

print ("Thanks for playing. Come again")			