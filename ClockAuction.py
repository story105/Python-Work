# this is now the rewritten code block
import random 

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

# Made this code more dynamic
def get_auction_values():
	buyers = input("Enter the number of buyers you want: ")
	buyers = check_input(buyers) # simply reaffirms integer
	
	print("")
	print("So what should the value range be be for prices?")
	bound1 = input("Enter the lower bound for prices: ")
	bound1 = check_input(bound1)
	bound2 = input("Enter the upper bound for prices: ")
	bound2 = check_input(bound2)
	
	print("")
	print("Trials is how many times this func will iterate. Make it big for accuracy's sake (if your computer can handle it).")
	trails = input("Enter number of trails: ")
	trails = check_input(trails)
	
	filled_out_values = [buyers, bound1, bound2, trails]
	#print(filled_out_values)
	return(filled_out_values)

# declare profit func before
def find_profit(revenue):
	total = 0
	for revenues in revenue:
		total += revenues
	avg_payout = total / len(revenue)
	return(avg_payout)

def find_revenues(list_of_values):
	revenue = [] # declare outside loop since we are technically an entire func
	buyers = int(list_of_values[0])
	value_bounds = [int(list_of_values[1]), int(list_of_values[2])]  # has to cost at least some money
	trials = int(list_of_values[3])
	
	for _ in range(trials):

		buyers_limits = [random.randrange(value_bounds[0], value_bounds[1]) for _ in range(buyers)]
		# buyers values
		price = random.randrange(value_bounds[0], value_bounds[1]) # only used for D
		
		values2 = buyers_limits # how I keep track of right buyer
		last_saved = 0 # just an index
		
		startprice = 0
		buyersIn = buyers  # an int to iterate
		done = False
		increment = 1
		reserve_price = 60  # Not quite sure what u wanted here in terms of "sold?"
		while done == False:
			for bidder_price in buyers_limits:
				if startprice > bidder_price:
					buyersIn -= 1 # one bidder drops out
					values2.remove(bidder_price)
					last_saved = bidder_price
			if reserve_price <= startprice:
				if buyersIn == 0: # multiple drop out at the end same time
					startprice -= increment # reset the increment
					buyer = last_saved
					revenue.append(startprice)
					done = True
				elif buyersIn > 1:
					startprice += increment
				else: # == 1
					buyer = last_saved
					revenue.append(startprice)
					done = True
			else: # nothing lol continue
				if buyersIn == 0: # multiple drop out at the end same time
					startprice -= increment # reset the increment
					buyer = last_saved
					revenue.append(startprice)
					done = True
				elif buyersIn > 1:
					startprice += increment
				else: # == 1
					buyer = last_saved
					revenue.append(startprice)
					done = True
	return(revenue) # a list of revenues for the given constraints

# This is how it would run dynamically and it's pretty neat
auction_values = get_auction_values()
revenue_for_values = find_revenues(auction_values)
profit_answer = find_profit(revenue_for_values)
print("")
print("The profit for the given auction setting is", profit_answer, "U$D.")

# This is answer for A/B/C, 
# A: I get around ~67 $ payout

# B: I get around ~73 $
# I think the large increment increased the revenue because, on average, the price point at which
# multiple buyers drop out increased along with it. A finer clock increment means a finer poin at
# which a single buyer wins the auction. But that's just my conjecture. 

# C: I get around ~91 $ 
# As we see here, I can make a way smarter guess here, there are many more chances of bidders having
# a higher price within 20 prices, instead of the 5 buyers you need two to at least have high prices set
# This is the reason C is so much higher than A. 
