import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold
import sys

featureSize = int(sys.argv[1])
kfoldSize = int(sys.argv[2])

df = pd.read_csv("traintestPreProcessed.csv")

x = df['SentimentText']
y = df['Sentiment']

TotalScores = 0
TotalFMES = 0

print("K-FOLD CROSS VALIDATION: " + str(kfoldSize))
print("")
kf = StratifiedKFold(n_splits=kfoldSize)

for train_index, test_index in kf.split(x,y):
    x_train, x_test, y_train, y_test = x[train_index], x[test_index], y[train_index], y[test_index]

    count_vectorizer = CountVectorizer(stop_words="english", max_features=featureSize)
    count_train = count_vectorizer.fit_transform(x_train.values)
    count_test = count_vectorizer.transform(x_test.values)

    featuresName = count_vectorizer.get_feature_names()
    print("COUNT VECTORIZER FEATURES:" + str(len(featuresName)))
    
    print("LOGISTIC REGRESSION CLASSIFIER")
    nb_classifier = LogisticRegression(solver="lbfgs", max_iter=500)
    nb_classifier.fit(count_train, y_train)
    pred = nb_classifier.predict(count_test)
    score = metrics.accuracy_score(y_test, pred)
    print("Accuracy Score: " + str(score * 100) + " %")
    fmes = metrics.f1_score(y_test, pred)
    print("F Measure Score: " + str(fmes * 100) + " %")
    TotalScores = TotalScores + score
    TotalFMES = TotalFMES + fmes
    
    cm = metrics.confusion_matrix(y_test, pred, labels=[1,0])
    list1 = ["Actually 1", "Actually 0"]
    list2 = ["Classified 1", "Classified 0"]
    cmtable = pd.DataFrame(cm, list1,list2)
    print(cmtable)
    print("")
    print("")
    
print("Average Accuracy Score: " + str((TotalScores/kfoldSize) * 100) + " %")
print("Average F Measure Score: " + str((TotalFMES/kfoldSize) * 100) + " %")
print("")
    