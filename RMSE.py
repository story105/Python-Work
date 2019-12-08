import math
# Change these to be your Nx1 matrices
x = [14,17,20,37,28,55]
e = [14.96,15.58,20.56,36.44,28.33,55.13]

def summation(got,actual):
	total = 0
	counter = 0
	#length of lists must be the same
	length = len(actual)
	while counter != length:
		total += (got[counter] - actual[counter]) * (got[counter] - actual[counter])
		counter += 1
	#print(total)
	return(total)
	
#count should be the number of values in actual
#summed in what you got from summation()
def otherstuff(count,summed):
	n = count
	summed = summed / n 
	returnVal = math.sqrt(summed)
	return(returnVal)

wee = summation(x,e)
hey = otherstuff(6,wee)
print(hey)
