import os
import sys

dirOne = sys.argv[1]
newFileName = dirOne + ".csv"
f2 = open(newFileName, "a")

directory = dirOne + "/negData"
for filename in os.listdir(directory):
    if filename.endswith(".txt"): 
        f = open(os.path.join(directory, filename), "r")
        string = ""
        for x in f:
            temp = x.replace("\n"," ")
            test = temp.replace(",", "")
            string = string + test + " "
        f2.write("0, " + string + "\n")
        continue
    else:
        continue

directory = dirOne + "/posData"
for filename in os.listdir(directory):
    if filename.endswith(".txt"): 
        f = open(os.path.join(directory, filename), "r")
        string = ""
        for x in f:
            temp = x.replace("\n"," ")
            test = temp.replace(",", "")
            string = string + test + " "
        f2.write("1, " + string + "\n")
        continue
    else:
        continue
