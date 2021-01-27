#the purpose of this program is to categorize data into different sets; validation, training and test

import os
import sys

totalNumFiles = len([name for name in os.listdir('original/negData/.')])

lower = sys.argv[1]
lowerB = float(lower) * totalNumFiles
lowerBound = int(lowerB)

#put anything below the % given into the development directory
directory = "original/negData"
count = 0
for filename in os.listdir(directory):
    if filename.endswith(".txt"): 
        f = open(os.path.join(directory, filename), "r")
        if (count >= lowerBound):
            f2 = open("traintest/negData/fileNeg" + str(count) + ".txt", "w")
            for x in f:
                f2.write(x)
        count = count + 1
        continue
    else:
        continue
        
#put anything above the % given in the validation directory
directory = "original/posData"
count = 0
for filename in os.listdir(directory):
    if filename.endswith(".txt"): 
        f = open(os.path.join(directory, filename), "r")
        if (count >= lowerBound):
            f2 = open("traintest/posData/filePos" + str(count) + ".txt", "w")
            for x in f:
                f2.write(x)
        count = count + 1
        continue
    else:
        continue
