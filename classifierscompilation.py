# This is a compilation of most of our classifiers

# Extra Trees Classification
import pandas as pd
import numpy as np
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import  BernoulliNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVR
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import f1_score

# DATA
in_file = 'discreteData4bins.csv'
names = ['budget', 'genres', 'original_language','popularity', 'production_companies', 'production_countries', 'revenue', 'runtime', 'vote_count', 'vote_average'] #movie id and original title not here
X_train = pd.read_csv(in_file, header=None, usecols=[0,1,2,3,4,5,6,7,8])
X_train = X_train.as_matrix()
Y_train = pd.read_csv(in_file, header=None, usecols=[9])
Y_train = np.ravel(Y_train.as_matrix())
print X_train.shape
print Y_train.shape
scoring = 'accuracy'
seed = 8
# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('EXT', ExtraTreesClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('BNB', BernoulliNB()))
models.append(('RF', RandomForestClassifier()))
models.append(('GBM', AdaBoostClassifier()))
models.append(('NN', MLPClassifier()))
models.append(('GRA', GradientBoostingClassifier()))
#models.append(('SVM', SVR()))

# evaluate each model in turn
results = []
names = []
for name, model in models:
    kfold = model_selection.KFold(n_splits=10, random_state=seed)
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold)#, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)


# seed = 8
# num_trees = 100
# max_features = 8
# kfold = model_selection.KFold(n_splits=10, random_state=seed)
# model = LogisticRegression()#ExtraTreesClassifier()#ExtraTreesClassifier(n_estimators=num_trees, max_features=max_features)# LogisticRegression(n_estimators=num_trees, max_features=max_features)
# results = model_selection.cross_val_score(model, x, y, cv=kfold)
# print(results.mean())
