README


*** Student Information ***
Student Name:         Miriam Snow


*** Organization of Files ***
Once the tar file is extracted you will find one directory titled "original" which contains two directories "negData" and "posData" which each contain 1000 files of negative and positive movie reviews, respectively.

You will also find a makefile, split.py, format2CSV.py, dataAnalysis.py and preProcess.py which are used for data analysis and pre processing before any testing can be done. The rest of the files contain implementation code for various feature selection and classifier method combinations as specified below.


Here is a list of codes for how each file is named:

FEATURE:
    CV = Count Vectorizer Feature Selection
    TFIDF = TFIDF Vectorizer Feature Selection


CLASSIFIER:
    MNB = Multinomial Naive Bayes Classifier
    LR =  Logistic Regression Classifier
    LSVC = Linear Support Vector Classification Classifier


*** Build and Test Instructions ***

1. In the main directory, type "make" into the command line to…
   1. Create two data analysis files for the negative and positive data collections
   2. Separate the entire data set into validation (15%) and K-Fold Cross Validation (85%) data sets
   3. Format the data into CSV files
   4. Preprocess the data by removing punctuation, performing case normalization and stemming words

2. Perform K-Fold Cross Validation
   1. Using the codes listed above, choose a combination to test.
   2. The files are named KFOLD_<FEATURE>_<CLASSIFIER>.py
   3. Indicate the number of features to be selected as the first command line argument
   4. Indicate the number of folds to be performed as the second command line argument


        For example, if you want to test 2000 features from the Count Vectorizer Feature Selection method with a Multinomial Naive Bayes Classifier and 10 folds, type the following into the command line:


                       "python KFOLD_CV_MNB.py 2000 10"


        As another example, if you want to test 500 features from the TFIDF Vectorizer Feature Selection method with a Linear Support Vector Classification Classifier and 5 folds, type the following into the command line:


                        "python KFOLD_TFIDF_LSVC.py 500 5"


3. Validate a feature selection and classifier combination (15/85 test/train split)
   1. Using the codes listed above, choose a combination to test.
   2. The files are named <FEATURE>_<CLASSIFIER>.py
   3. Indicate the number of features to be selected as the first command line argument


        For example, if you want to test 1500 features from the Count Vectorizer Feature Selection method with a Logistic Regression Classifier, type the following into the command line:

                        "python CV_LR.py 1500"

        As another example, if you want to test 3000 features from the TFIDF Vectorizer Feature Selection method with a Multinomial Naive Bayes Classifier, type the following into the command line:


                        "python TFIDF_MNB.py 3000"

4. Type "make clean" into the command line after testing to remove all pre processed data and CSV files
