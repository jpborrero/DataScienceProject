import pandas as pd
import numpy as np
import csv
from sklearn import model_selection
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_validate
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier

# MODELS
models = []
models.append(('RF', RandomForestClassifier()))
models.append(('EXT', ExtraTreesClassifier()))
models.append(('ADA', AdaBoostClassifier()))

# FIND FEATURE IMPORTANCES
def evaluate_key_features(models):
    restriction = input("Evaluate restricted data (vote count > 10)? Yes=1, No=0: ")
    res = ''
    if restriction == 1:
        res ='Res'
    for k in range (2,11):
        in_file = 'discreteData'+str(k)+'bins'+res+'.csv'
        X_train = pd.read_csv(in_file, header=None, usecols=[0,1,2,3,4,5,6,7,8])
        X_train = X_train.as_matrix()
        Y_train = pd.read_csv(in_file, header=None, usecols=[9])
        Y_train = np.ravel(Y_train.as_matrix())
        print X_train.shape
        print Y_train.shape
        scoring = ['accuracy', 'f1_weighted']

        for name, model in models:
            # CHECK BEST FEATURE FOR FOREST OF TREES
            model.fit(X_train,Y_train)
            importances = model.feature_importances_
            std = np.std([tree.feature_importances_ for tree in model.estimators_],axis=0)
            indices = np.argsort(importances)[::-1]
            # Print the feature ranking
            print("Feature ranking ("+name+"- "+str(k)+" bins):")
            for f in range(X_train.shape[1]):
                print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))

            # Plot the feature importances of the forest
            plt.figure()
            plt.title("Feature importances - "+name)
            plt.bar(range(X_train.shape[1]), importances[indices],
                   color="r", yerr=std[indices], align="center")
            plt.xticks(range(X_train.shape[1]), indices)
            plt.xlim([-1, X_train.shape[1]])
            plt.show()


evaluate_key_features(models)
