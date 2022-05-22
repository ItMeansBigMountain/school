# DATASET LIBRARIES
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np


# ESTIMATORS
from sklearn.neighbors import KNeighborsClassifier




# TRAIN/TEST SPLIT
from sklearn.model_selection import train_test_split




# CROSS VALIDATION
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score




# GRAPHING
import seaborn as sns
import matplotlib.pyplot as plt
from itertools import cycle





'''
15.7
    Load the Iris dataset and perform classification on it with the k-nearest neighbors algorithm. Use a KNeighborsClassifier with the default k value. What is the prediction accuracy?

    RESPONSE:
        Accuracies of three techniques shown in exercise.15.7_Output.png



'''




# DATASET
iris_data = load_iris()  





# TRAIN/TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split( iris_data.data, iris_data.target )  
kfold = KFold(n_splits=10, shuffle=True)





# ESTIMATOR
knn = KNeighborsClassifier()





# TRAINING
knn.fit(X=X_train, y=y_train)
cross_validation_scores = cross_val_score(estimator=knn, X=iris_data.data, y=iris_data.target, cv=kfold)



# PREDICTION
predicted = knn.predict(X=X_test)
expected = y_test
wrong = [(p, e) for (p, e) in zip(predicted, expected) if p != e]













# SCORE
print(f'\nSINGLE TRAIN/TEST SPLIT SCORE: {knn.score(X_test, y_test):.2%}')
print(f'K-FOLD CROSS VALIDATION SCORES AVERAGE: {cross_validation_scores.mean():.2%}' , end="\n\n\n\n" )









print("HYPERPARAMETER TUNING K-FOLD CROSS VALIDATION")
for k in range(1, 20, 2):  # k is an odd value 1-19; odds prevent ties
    kfold = KFold(n_splits=10, random_state=11, shuffle=True)
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(estimator=knn, X=iris_data.data, y=iris_data.target, cv=kfold)
    print(f'k={k:<2}; mean accuracy={cross_validation_scores.mean():.2%}; ' + f'standard deviation={cross_validation_scores.std():.2%}')


