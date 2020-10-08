# This is the updated code 
import random 

def calc_profit(hotel_build_pattern, build_time, years):
	T = len(hotel_build_pattern)
	m = build_time
	profits = []
	hotels = hotel_build_pattern
	for t in range(0,years):
		profits.append((750 + 50*(t+1))/(hotels[t] + 1))
	return(sum(profits))


def build_profile(years, build_time):
	n = 0 #hotels built (already)
	hotels = []
	#comp_start_hotels = random.randrange(0, 10) 
	# u can up how many hotels you think competition should have
	comp_start_hotels = 0   # IF WE START AT 0 enemy hotels???
	building = False
	build_time_counter = build_time
	for _ in range(years):
		
		if random.choice([0, 1]) == 1:
			building = True
		if building == True: 
			build_time_counter -= 1
		if build_time_counter == 1:
			n += 1
			building = False
			build_time_counter = build_time
		#randomly didn't decide to start building a hotel 
		hotels.append(comp_start_hotels+n)
	return([hotels,build_time])		

def check_int(checked_thing):
	its_a_digit = False # boolean value
	if checked_thing.isdigit():
		its_a_digit = True
	return(its_a_digit)

def check_input(input1):
	checked = False
	while checked == False:
		checked = check_int(input1)
		if checked == False:
			input1 = input("That wasn't an integer... please enter an integer: ")
	return(input1)
	

def Monte_Carlo_way(input1):
	print("Trials is how many times this func will iterate. Make it big for accuracy's sake (if your computer can handle it).")
	trails = input("Enter number of trails: ")
	trails = check_input(trails)
	sum1 = 0
	for _ in range(trials):
		#value_bounds = [10,50]
		#years =  random.randrange(value_bounds[0], value_bounds[1])
		years = 10    # IF THERES ONLY 10 years???
		build_time = input1 #years
		checklist = build_profile(years, build_time)
		finalThing = calc_profit(checklist[0],checklist[1],years)
		sum1 += finalThing
	
	sum1 = sum1 / trials
	return(sum1)


XXX = MonteCarloWay(3)
print("The average profit for the build patterns is:",XXX)