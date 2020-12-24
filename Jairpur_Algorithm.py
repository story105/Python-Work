import random
import math 
from collections import Counter,OrderedDict

def create_deck():    
	values = ["Ruby","Gold","Silver","Cloth","Spice","Leather","Camel"]    
	deck = []    
	for v in values:   
		counter = 0
		if v == "Ruby" or v == "Gold" or v == "Silver":
			amount = 6
		elif v == "Cloth" or v == "Spice":
			amount = 8
		elif v == "Leather":
			amount = 10
		else: # its a camel but in all cases the 3 camels are dealt out (11 norm)
			amount = 8 
		while counter < amount:
			deck.append(v)
			counter += 1
	for i in range(6):
		random.shuffle(deck) #order matters in terms of drawing cards! but we need to shuffle
	return(deck) # i know it's randomized
	
# order matters, so in terms of list logic, we pop the FIRST card 5 times off the list
def deal(deck):
	hand = []
	for i in range(5):
		hand.append(deck[i])
	for card in hand:
		deck.remove(card) # since there are multiple occurances of values, we also dont care
	return(hand, deck)

def take_camels(hand,deck,river): # when you draw a camel, you take them ALL
	counterCamel = 0
	for i in range(len(river)):
		if river[i] == "Camel":
			hand.append(river[i])
			counterCamel+=1
	for i in range(counterCamel):
		river.remove("Camel") # CHECK THIS WORKS
	for i in range(counterCamel):
		fill(river,deck)
	return(hand,river,deck)

def draw(hand,deck,river): # this can be super intense method
	if river[0]== "Camel":
		take_camels(hand,deck,river)
	hand.append(river[0])
	river.append(deck[0])
	deck.remove(deck[0])
	return(hand,deck,river)

def fill(river,deck): # when you just put from deck to river
	river.append(deck[0])
	deck.remove(deck[0])
	return(river,deck)

# might need chips here too / or combo? # this is "sell"
def spend(cardType, cardNum, hand, market,playerpoints): 
	for i in range(cardNum):
		hand.remove(cardType) # this is always
	if cardNum == 3:
		combo3points = market.get('3combo')
		combo3points.remove(combo3points[0])
		playerpoints+=combo3points[0]
		market['3combo'] = combo3points # get combo points and update the market for next 
	elif cardNum == 4:
		combo4points = market.get('4combo')
		playerpoints+=combo4points[0]
		combo4points.remove(combo4points[0])
		market['4combo'] = combo4points 
	elif cardNum == 5:
		combo5points = market.get('5combo')
		playerpoints+=combo5points[0]
		combo5points.remove(combo5points[0])
		market['5combo'] = combo5points 
	else: #1 or 2
		valuesLeft = market.get(cardType)
		pointsEarned = 0
		for i in range(cardNum):
			playerpoints+=valuesLeft[0]
			valuesLeft.remove(valuesLeft[0])
		market[cardType] = valuesLeft
	return(hand,market,playerpoints)

def check_market(market): # once 3 resources are empty!
	#game_over == True if len(market)==4 else False 
	game_over = False
	resourceEmptyCounter = 0
	for resourceNum in market.values(): 
		resourceEmptyCounter += 1 if resourceNum == [] else 0 
	if resourceEmptyCounter == 3:
		game_over = True
	return(game_over)

def make_market(): # let's get a dict of lists
	market = {}
	rubylist = [7,7,5,5,5]
	market["Ruby"] = rubylist
	goldlist = [6,6,5,5,5]
	market["Gold"] = goldlist
	silverlist = [5,5,5,5,5]
	market["Silver"] = silverlist
	clothlist = [5,3,3,2,2,1,1]
	market["Cloth"] = clothlist
	spicelist = [5,3,3,2,2,1,1]
	market["Spice"] = spicelist
	leatherlist = [4,3,2,1,1,1,1,1,1,]
	market["Leather"] = leatherlist
	combo3list = [1,1,2,2,2,3,3] # 14 pts
	for i in range(3):  # we want random access to give a random value as if we shuffled the combos too
		random.shuffle(combo3list)
	market["3combo"] = combo3list # make this a dict with a list value so we can random get combo
	combo4list = [6,6,5,5,4,4]
	for i in range(3):
		random.shuffle(combo4list)
	market["4combo"] = combo4list
	combo5list = [8,8,9,10,10]
	for i in range(3):
		random.shuffle(combo5list)
	market["5combo"] = combo5list
	return(market)

# BASIC FUNCS ABOVE # ALWAYS ::: HAND - DECK - RIVER ----
# remember, you need 2 of silver, gold, and ruby to sell!
def decide_turn(hand, deck, river, market, playstyle,playerpoints): # let's see if I can build better overall code
	if playstyle == 1: # we doing aggro fast sell
		print("Players hand is:",hand)
		if len(hand) > 0:
			handDict = Counter(hand)
			
			tempdict = {} # catch the darn camels always being largest resource
			keys = set(handDict.keys())
			excludes = set(["Camel"])
			for key in keys.difference(excludes):
				tempdict[key]= handDict[key]
			max_resource = max(tempdict, key=tempdict.get)
			all_values = tempdict.values() 
			max_number_resource = max(all_values)
			
			# iterate through the dictionary for second most prevalent
			if max_resource == "Gold" or max_resource == "Silver" or max_resource == "Ruby":
				if max_number_resource >= 2:
					print("Selling ",max_number_resource, max_resource)
					setOfValues = spend(max_resource,max_number_resource,hand,market,playerpoints)
				else: # then it means that there was 1 of these ONLY CAN TRADE 2+ resources
					tempdict2 = {}
					keys = set(tempdict.keys())
					excludes = set([max_resource])
					for key in keys.difference(excludes):
						tempdict2[key]= tempdict[key]
					max_resource = max(tempdict2, key=tempdict2.get)
					all_values = tempdict2.values() 
					max_number_resource = max(all_values)
					print("Selling ",max_number_resource, max_resource)
					setOfValues = spend(max_resource,max_number_resource,hand,market,playerpoints)
			else:	
				# we are selling the other resources
				print("Selling ",max_number_resource, max_resource)
				setOfValues = spend(max_resource,max_number_resource,hand,market,playerpoints)
				# hand,market,playerpoints
		else:
			draw(hand,deck)
			print("Sheeshhh")# WE ARE TAKING A CARD
	elif playstyle == 2: # saving for combos
		print("Ill get to this")
	return(hand, deck, river, market, playerpoints)	
	# IM HERE
	
 
def play_normal_game():
	game_over = False
	market = make_market()
	deck = create_deck()
	river = []
	for i in range(3): # 3 camels to start
		river.append("Camel")
	player1hand = deal(deck) # this returns 2 things
	player2hand = deal(deck)
	
	fill(river,deck) # put 2 in, not going to players hands
	fill(river,deck)
	
	player1points = 0
	player2points = 0
	#val = input("what type of playstyle? 'Aggro' or 'combo' :")
	#val.capitalize()
	val = "AGGRO" # DELETE THIS WHEN DONE
	if val == 'AGGRO':
		playstyle = 1
	else:
		playstyle = 2 # go for combos
	playerTurn = 1
	while game_over == False:
		print("It is player :",playerTurn, "s turn!")
		# player 1 starts, max hand size is 7, let's see if combos beat just instant draw?
		decide_turn(player1hand[0],deck,river,market,playstyle,player1points) # what to do on turn
		#print(market)
		
		print("")
		print('NO=-=1212=-12!!!!!!!!!NOT HERE YET DUUUDE!!!!!!!!!!!!!!!!-=-1212-2=1NOT')
		game_over = True
	
	print("Game over!")
	# CALCULATE WHO HAD MORE CAMELS AND ADD 5
	if player1points > player2points:
		winningPoints = player1points
		#print("player 1 won with ",winningPoints, "points")
	elif player1points < player2points:
		winningPoints = player2points
		#print("player 2 won with ",winningPoints, "points")
	else:
		winningPoints = player1points
		#print("They tied?? With ",winningPoints, "points!")
	#print("The market looks like ", market)
	return(winningPoints)
# make it monte carlo for some part
play_normal_game()
#samples = 1000
#pointsInAGame = 0
#for _ in range(samples):    
#	pointsInAGame += 1 if (have_2rubies(hand)>1) else 0 
#print(successes / samples)