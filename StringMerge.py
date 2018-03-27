string1 = raw_input("enter first string:")
string2 = raw_input("enter second string:")
mylist1 = string1.split()
mylist2 = string2.split()

print (mylist1)

mylist1.extend(mylist2)

print (mylist1)


def stringfunction(of_a_list):   
	string1 = " ".join(sorted(mylist1))  #joins with a space andddddd is sorted in one step :D
	return string1

print stringfunction(mylist1)
