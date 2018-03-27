#This all runs together if you don't mind. Thanks!

def energy(C):
	answer = M*(C**2)
	return answer

C = 299792458
M = float(raw_input("Enter mass:"))

print (energy(C), "amount of energy")


def reverse(mystring):

	if mystring[::-1] == mystring:
		return "true"
	else:
		return "false"


mystring = raw_input("enter palindrome?")

print reverse(mystring)

def yardstomiles(yards):
	answer = float(yards / 1760)
	return answer
	
yards = float(raw_input("enter yards to calculate how many miles:"))

print yardstomiles(yards)


def check(max, min, guessvalue):
	if guessvalue > max:
		return "Greater"
	elif guessvalue < min:
		return "less"
	else:
		return "in range"
		
min,max=map(float,raw_input("Enter a range from low to high Ex:(x x):").split())
xvalue = raw_input ("enter a value to check if in range:")
guessvalue = float(xvalue)

print check(max, min, guessvalue)

def halflife(t, t_5, NO):
	t = float(t)
	answer = float(NO*(1.0/2.0)**(t/t_5))
	return answer
	
t, t_5, NO =map(float,raw_input \
("Enter a time span, halflife, and initial quantity of substance (form a b c):").split())

print halflife(t, t_5, NO)

#this gives a number, but I'm not sure it's right
# second check... its right I think

