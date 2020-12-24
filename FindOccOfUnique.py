# find first occurance of unique character in big string
def FindOccurance(passed):
    arr1 = [] # character array
    arr2 = [] # counts of occurance
    for char in passed:
        if char not in arr1:
            arr1.append(char)
            arr2.append(1)
        else:
        #arr2[arr1.index(char)] > 1:
            arr2[arr1.index(char)] += 1 #increment how many times seen

    finalList = []
    counter = 0
    length = len(arr1)

    while counter != length-1:
        if arr2[counter] == 1: #only seen once
            finalList.append([arr1[counter],counter])
        counter += 1
    if len(finalList) == 0:
        print("No unique characters")
    else:
        print("first unique occurance is " + finalList[0][0])
        print("at position "+ str(finalList[0][1]))

FindOccurance("absfgietpomxuvugmkamqmzxccvbnasfietpoqn")
#print("absfgietpomxuvugmkamqmzxccvbna".count("s"))
