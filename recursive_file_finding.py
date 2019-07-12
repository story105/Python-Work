import os
# Recursive function to look for .XX type of files

py = ".py"
rob = ".robot"

end_list = []

python_path = "/Users/charliestory/Documents/GitHub/edge-cloud-qa-ui"

def get_all_tests(path):
    testcases_files = os.listdir(path)

    for dirs in testcases_files:
        panic = False
        if dirs[0] == ".":
            print("Hidden file: " + dirs)
        else:
            if py in dirs:
                end_list.append(dirs)
            elif rob in dirs:
                end_list.append(dirs)
            else:
                for letter in dirs:
                    if letter == ".":
                        print(dirs)
                        panic = True
                if panic == False:
                    one_step_deeper_path = path + "/" + dirs
                    print(one_step_deeper_path)
                    get_all_tests(one_step_deeper_path)

    return(end_list)

returned_List = get_all_tests(python_path)

print(returned_List)
