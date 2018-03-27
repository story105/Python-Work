#I have never played this game before, and this online version is hard as heck
start = []
middle = []
end = []

#This first function just takes the inputted disks and gives the "start peg" list the descending values it needs
def countdisks(disks):
	Disk_copy = disks
	while Disk_copy > 0:
		start.append(Disk_copy)
		Disk_copy = Disk_copy - 1
	return start 
	
def MoveDisk(disks, start, middle, end):
	if disks > 0: 
		MoveDisk(disks - 1, start, end, middle)
		if start[0]:
			end.append(start.pop())
		MoveDisk(disks - 1, middle, start, end)
	return (start, middle, end)	
	
disks = int(raw_input("enter a number of disks to solve the Tower of Hanoi:"))

print countdisks(disks)	#I HAD TO ADD THIS IN BC I DON'T KNOW HOW TO RUN THE FIRST FUNCTION WITHOUT THIS
#It makes the Start list become the decreasing integers you need for the second function

print ("Game begins", start, middle, end) #returns the starting Tower of Hanoi 
print ("Game ends:", MoveDisk(disks, start, middle, end))

print ("The amount of steps it took:", (2**(disks)-1)) #Minimum number of steps for input 

# second part of the code for 5 disks
# minimum_number_of_moves = 2**(disks)-1
print ("minimum number of moves for 5 disks is:", (2**(5)-1))

def recursion(h):
	if h == 1:
		return 1
	else:
		return 2*(recursion(h-1))+1

print recursion(5)