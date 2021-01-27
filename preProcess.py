####this program removes stop words from all data
import sys
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer

#open the files
fileName1 = sys.argv[1]
newFileName = fileName1 + ".csv"
f = open(newFileName, "r")

createdFileName = fileName1 + "PreProcessed.csv"
f2 = open(createdFileName, "w")
f2.write("Sentiment,SentimentText\n")

#remove punctuation
import re
def multiwordReplace(text, wordDic):
    rc = re.compile('|'.join(map(re.escape, wordDic)))
    def translate(match):
        return wordDic[match.group(0)]
    return rc.sub(translate, text)

wordDic = {
'.' : '',
')' : '',
'(' : '',
'!' : '',
'-' : '',
'_' : '',
'"' : '',
'*' : '',
'?' : '',
'/' : '',
'&' : '',
'[' : '',
']' : '',
':' : '',
';' : '',
}


ps = PorterStemmer()
for p in f:
    str2 = multiwordReplace(p, wordDic)
    words = word_tokenize(str2)
    newStr = ""
    for w in words:
        stem = ps.stem(w)
        newStr = newStr + stem + " "
    f2.write(newStr + "\n")
