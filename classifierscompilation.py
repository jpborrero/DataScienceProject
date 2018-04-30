# This is a compilation of most of our classifiers
import pandas as pd
import numpy as np
import csv
from sklearn import model_selection
from sklearn.model_selection import cross_validate
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import Perceptron
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import  BernoulliNB
from sklearn.naive_bayes import  GaussianNB
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score

# MODELS
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('PER', Perceptron()))
models.append(('SGD', SGDClassifier()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('DT', DecisionTreeClassifier()))
models.append(('RF', RandomForestClassifier()))
models.append(('EXT', ExtraTreesClassifier()))
models.append(('ADA', AdaBoostClassifier()))
models.append(('BAG', BaggingClassifier()))
models.append(('BNB', BernoulliNB()))
models.append(('GNB', GaussianNB()))
models.append(('MLP', MLPClassifier()))

# EVALUATE MODELS
def evaluate(models):
    with open('accuracyMetrics.csv', 'w') as accuracy_file, open('f1scoreMetrics.csv', 'w') as f1score_file, open('timeMetrics.csv', 'w') as time_file:
        fieldnames = ['BINS', 'LR', 'LDA', 'PER', 'SGD','KNN', 'DT', 'RF', 'EXT', 'ADA', 'BAG', 'BNB','GNB','MLP']
        accuracyWriter = csv.DictWriter(accuracy_file, fieldnames=fieldnames)
        f1scoreWriter = csv.DictWriter(f1score_file, fieldnames=fieldnames)
        timeWriter = csv.DictWriter(time_file, fieldnames=fieldnames)
        accuracyWriter.writeheader()
        f1scoreWriter.writeheader()
        timeWriter.writeheader()
        for k in range (2,11):
            in_file = 'discreteData'+str(k)+'bins.csv'
            names = ['budget', 'genres', 'original_language','popularity', 'production_companies', 'production_countries', 'revenue', 'runtime', 'vote_count', 'vote_average'] #movie id and original title not here
            X_train = pd.read_csv(in_file, header=None, usecols=[0,1,2,3,4,5,6,7,8])
            X_train = X_train.as_matrix()
            Y_train = pd.read_csv(in_file, header=None, usecols=[9])
            Y_train = np.ravel(Y_train.as_matrix())
            print X_train.shape
            print Y_train.shape
            scoring = ['accuracy', 'f1_weighted']

            # EVALUATE EACH MODEL
            accuracyResults = []
            f1scoreResults = []
            timeResults = []
            for name, model in models:
                kfold = model_selection.KFold(n_splits=10)#, random_state=seed)
                cv_results = model_selection.cross_validate(model, X_train, Y_train, cv=kfold, scoring=scoring)
                accuracyResults.append(cv_results['test_accuracy'].mean())
                f1scoreResults.append(cv_results['test_f1_weighted'].mean())
                timeResults.append(cv_results['fit_time'].mean())
                msg = "%s - ACCURACY: %f (%f) F1_SCORE: %f (%f) TIME: %f (%f)" % (name, cv_results['test_accuracy'].mean(), cv_results['test_accuracy'].std(), cv_results['test_f1_weighted'].mean(), cv_results['test_f1_weighted'].std(), cv_results['fit_time'].mean(), cv_results['fit_time'].std())
                print(msg)

            accuracyWriter.writerow({'BINS':k, 'LR':accuracyResults[0], 'LDA':accuracyResults[1], 'PER':accuracyResults[2], 'SGD':accuracyResults[3],'KNN':accuracyResults[4], 'DT':accuracyResults[5], 'RF':accuracyResults[6], 'EXT':accuracyResults[7], 'ADA':accuracyResults[8], 'BAG':accuracyResults[9], 'BNB':accuracyResults[10],'GNB':accuracyResults[11],'MLP':accuracyResults[12]})
            f1scoreWriter.writerow({'BINS':k, 'LR':f1scoreResults[0], 'LDA':f1scoreResults[1], 'PER':f1scoreResults[2], 'SGD':f1scoreResults[3],'KNN':f1scoreResults[4], 'DT':f1scoreResults[5], 'RF':f1scoreResults[6], 'EXT':f1scoreResults[7], 'ADA':f1scoreResults[8], 'BAG':f1scoreResults[9], 'BNB':f1scoreResults[10],'GNB':f1scoreResults[11],'MLP':f1scoreResults[12]})
            timeWriter.writerow({'BINS':k, 'LR':timeResults[0], 'LDA':timeResults[1], 'PER':timeResults[2], 'SGD':timeResults[3],'KNN':timeResults[4], 'DT':timeResults[5], 'RF':timeResults[6], 'EXT':timeResults[7], 'ADA':timeResults[8], 'BAG':timeResults[9], 'BNB':timeResults[10],'GNB':timeResults[11],'MLP':timeResults[12]})

evaluate(models)

# SAVE RESULTS IN A FILE TO LATER DISPLAY USING MATHPLOT LIB
