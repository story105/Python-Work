price_total = 0.0

ID_descriptionset = {}
ID_priceset = {}
ID_quantityset = {}

ID = int(raw_input("Please enter an ID of an object you'd like to add to your inventory (<0 to exit): "))
while ID >  0:          #entering for inventory
	description = raw_input("enter the description of item:")
	ID_descriptionset [ID] = description
	priceofitem = float(raw_input("enter the price of item:"))
	ID_priceset [ID] = priceofitem
	quantityofitem = int(raw_input("enter the quantity of the item:"))
	ID_quantityset [ID] = quantityofitem
	ID = int(raw_input("Please enter an ID of an object you'd like to add to your inventory: ")) #will repeat until <=0 is inputted

#After inventory archived, now to find items
#this should happen afterwards all of the lists are filled (yes I reuse ID makes it easy for me to follow)
ID = int(raw_input("OK, enter an ID of an object you like to see the details of:"))
while ID > 0:
	print ("there are", ID_quantityset[ID], ID_descriptionset[ID], "and costs", ID_priceset[ID])
	ID = int(raw_input("enter an ID of an object you like to see the details of (0 to exit):"))
	
#After items are inspected, time to order $$$
total_order, quantity = map(int,raw_input("For your order, enter the ID of item you want and # of that item (14 2), enter 0 0 when done:").split())
while total_order > 0:
	price_total = price_total + (ID_priceset[total_order] * quantity) 
	total_order, quantity = map(int,raw_input("Enter ID of item you want and # of that item (14 2), enter 0 0 when done:").split())
	
print ("your total is:", price_total, "$$$$$$")


