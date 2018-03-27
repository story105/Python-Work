#Charles Story Tuple EC assignment

nucleotide_tuple= ("A", "C", "T", "G");
user_input_list = []
user_input = raw_input("Enter individual DNA to add to a list to varify if valid strand(enter done to varify):")
user_input = user_input.upper()
while user_input != "DONE":
	user_input_list.append(user_input)
	user_input = raw_input("Enter individual DNA to add to a list to varify if valid strand(enter done to varify):")
	user_input = user_input.upper()
	print user_input_list

Nucleotide_index = 0

for char in user_input_list:
	if char in nucleotide_tuple:
		Nucleotide_index += 1
		continue
	else:
		print ("The nucleotide at", Nucleotide_index, "is invalid")
#Next step is to input a file with individual strands of Chars and check for inconsistencies
