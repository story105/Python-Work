#!/bin/python3

import os
import re

# For systems with an OUTPUT_PATH set, uncomment the fptr.
def camelcase(s):
    checkString = s
    wordCount = 1
    counter = 0
    for char in checkString:
        try:
            if char.isupper() and checkString[(counter+1)].islower():
                wordCount += 1
        except IndexError:
            wordCount = "String ends in a capital"
        counter += 1
    return wordCount


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
	fo = open("camelCase.txt", "w")
	s = raw_input("Enter a camelCaseWord: ")
	result = camelcase(s)

    #fptr.write(str(result) + '\n')
	#fptr.close()
	fo.write(str(result) + '\n')
	fo.close()
    