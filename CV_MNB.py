import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB
import sys

featureSize = int(sys.argv[1])

df = pd.read_csv("originalPreProcessed.csv")

print("LOADING CONTENT")
print(df.head())

x = df['SentimentText']
y = df['Sentiment']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.15, random_state=53)

count_vectorizer = CountVectorizer(stop_words="english", max_features=featureSize)
count_train = count_vectorizer.fit_transform(x_train.values)
count_test = count_vectorizer.transform(x_test.values)

print
featuresName = count_vectorizer.get_feature_names()
count = 1
for f in featuresName:
    print(str(count) + ". " + f)
    count += 1
print
print("COUNT VECTORIZER FEATURES: " + str(len(featuresName)))
print
print("MULTINOMIAL NAIVE BAYES CLASSIFIER")
print
nb_classifier = MultinomialNB()
nb_classifier.fit(count_train, y_train)
pred = nb_classifier.predict(count_test)
score = metrics.accuracy_score(y_test, pred)
print("Accuracy Score: " + str(score * 100) + " %")
print
fmes = metrics.f1_score(y_test, pred)
print("F Measure Score: " + str(fmes * 100) + " %")
print
cm = metrics.confusion_matrix(y_test, pred, labels=[1,0])
list1 = ["Actually 1", "Actually 0"]
list2 = ["Classified 1", "Classified 0"]
cmtable = pd.DataFrame(cm, list1,list2)
print(cmtable)