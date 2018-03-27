import math
a,b,c=map(float,raw_input \
("please enter three coefficients for a quadratic in form A B C:").split()) 

d = b**2 - (4*a*c)

if d < 0:
	print ("scrub there's no real solutions")
elif d == 0:
	x1 = -b / (2*a) 
	print ("Only one solution:"), x1 
else: # if d > 0
	x1 = (-b + math.sqrt(d)) / (2*a)
	x2 = (-b - math.sqrt(d)) / (2*a)
	print ("solutions are", x1 , x2)
print ("It works finally!")