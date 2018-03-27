file_name = raw_input("input the file to be opened (input.txt):")
file_line_str = raw_input("enter the line number?")


try:
	input_file = open(file_name, "r")
	file_line_num = int(file_line_str)
	temp_file = open("output.txt", "w")
	linecount = 0
	charcount = 0
	for lines in input_file:
		if linecount % file_line_num == 0:
			temp_file.write(str(linecount))
			temp_file.write("/n")        #I saw this would keep it from double space
			for char in range(len(line)):
				if char % file_line_num == 0: 		#I only barely came onto the range(len)
					temp_file.write(line[char])
					temp_file.write("/n")
					linecount += file_line_num
		else:
			continue 
	else:
		print ("File exists, but not the line in said file")
	
except NameError:
	print ("file don't exist, program will exit (name error)")
	
except ValueError:
	print ("the line", file_line_num, "doesnt exist, program will exit")

except IOError:
	print ("The file", file_name, "doesn't exist, program will exit")

input_file.close()
temp_file.close()   #I dunno if we should close them if they might still reuse this? But I rememeber you saying something about this

#I would close the input file, but my comp never finds the input file!
	
