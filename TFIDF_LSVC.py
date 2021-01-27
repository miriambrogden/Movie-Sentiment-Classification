import pandas as pd
import sys
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

featureSize = int(sys.argv[1])

df = pd.read_csv("originalPreProcessed.csv")

print("LOADING CONTENT")
print(df.head())

x = df['SentimentText']
y = df['Sentiment']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.15, random_state=53)

tfidf_vectorizer = TfidfVectorizer(stop_words="english", max_features=featureSize, max_df=0.7)
tfidf_train = tfidf_vectorizer.fit_transform(x_train.values)
tfidf_test = tfidf_vectorizer.transform(x_test.values)

print
featuresName = tfidf_vectorizer.get_feature_names()
count = 1
for f in featuresName:
    print(str(count) + ". " + f)
    count += 1
print
print("TFIDF VECTORIZER FEATURES: " + str(len(featuresName)))
print
print("LINEAR SUPPORT VECTOR CLASSIFIER")
print
nb_classifier = LinearSVC(max_iter=15000)
nb_classifier.fit(tfidf_train, y_train)
pred = nb_classifier.predict(tfidf_test)
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