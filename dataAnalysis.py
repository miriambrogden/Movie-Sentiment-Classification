import os
import sys
import nltk
from nltk.tokenize import word_tokenize 

dirOne = sys.argv[1]

fileName = dirOne + "Analysis.csv"
f2 = open(fileName, "a")

myDir = "original/" + dirOne + "/."
totalNumFiles = len([name for name in os.listdir(myDir)])

numTokens = 0.0
numSentences = 0.0
totalNumTokens = 0.0
totalNumSentences = 0.0
count = 0

directory = "original/" + dirOne

f2.write("Document, Number of Tokens, Number of Sentences, Tokens per Sentence\n")

for filename in os.listdir(directory):
    if filename.endswith(".txt"): 
        count += 1
        numSentences = 0.0
        numTokens = 0.0
        f = open(os.path.join(directory, filename), "r")
        for x in f:
            numSentences += 1
            words = word_tokenize(x)
            numTokens = numTokens + len(words)
            words = []
        tokensPerSentence = float(numTokens/numSentences)
        f2.write(str(count) + "," + str(numTokens) + "," + str(numSentences) + "," + str(tokensPerSentence) + "\n", )
        totalNumSentences = totalNumSentences + numSentences
        totalNumTokens = totalNumTokens + numTokens
        continue
    else:
        continue
aveTokensPerSentence = float(totalNumTokens/totalNumSentences)
aveTokens = float(totalNumTokens/totalNumFiles)
aveSentences = float(totalNumSentences/totalNumFiles)
f2.write("Total," + str(totalNumTokens) + "," + str(totalNumSentences) + "\n")
f2.write("Average," + str(aveTokens) + "," + str(aveSentences) + "," + str(aveTokensPerSentence) + "\n")