import time

# SAMPLE DATA
from sklearn.datasets import load_digits

# TRAIN TEST SPLIT 
from sklearn.model_selection import train_test_split

# CROSS VALIDATION (k-fold)
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

# GRAPHING
import matplotlib.pyplot as plt
import seaborn as sns

# CONFUSION MATRIX
import pandas as pd
from sklearn.metrics import confusion_matrix



# TRAINING MODELS
from sklearn.neighbors import KNeighborsClassifier as knn
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier








# helper functions
def graphing_data(digits):
    figure, axes = plt.subplots(nrows=4, ncols=6, figsize=(6, 4))
    for item in zip(axes.ravel(), digits.images, digits.target):
        axes, image, target = item 
        axes.imshow(image, cmap=plt.cm.gray_r)
        axes.set_xticks([])  # remove x-axis tick marks
        axes.set_yticks([])  # remove y-axis tick marks
        axes.set_title(target)
    plt.show()























estimators = {
    'KNeighborsClassifier': knn(), 
    'SVC': SVC(gamma='scale'),
    'GaussianNB': GaussianNB(),
    'DecisionTreeClassifier': DecisionTreeClassifier(),
}





#NOTE fetch data
['data', 'target', 'frame', 'feature_names', 'target_names', 'images', 'DESCR']
digits = load_digits()


#NOTE GRAPHING
graphing_data(digits)


#NOTE train test split
X_train,X_test, y_train, y_test = train_test_split( digits.data, digits.target, random_state=11) 





tree = DecisionTreeClassifier.fit(X=X_train, y=y_train)
predicted = tree.predict(X=X_test)
expected = y_test



print("PREDICTED",predicted[:20])
print("EXPECTED",expected[:20])
exit()








# train
print("K-NEAREST NEIGHBORS")
knn = KNeighborsClassifier()
knn.fit(X=X_train, y=y_train)


# test
predicted = knn.predict(X=X_test)
expected = y_test # answers



print("PREDICTED",predicted[:20])
print("EXPECTED",expected[:20])





#NOTE cleaning data to find wrong results
wrong = [ (p,e) for (p,e) in zip(predicted,expected) if p != e ]
print("WRONG", len(wrong))



# DISPLAY CONFIDENCE SCORE
print( "ACCURACY" ,  knn.score(X_test,y_test) )






#NOTE GRAPHING THE CONFUSION MATRIX
print("displayed CONFUSION MATRIX")
confusion = confusion_matrix(y_true=expected, y_pred=predicted)
confusion_df = pd.DataFrame(confusion, index=range(10), columns=range(10))
figure = plt.figure(figsize=(7, 6))
axes = sns.heatmap(confusion_df, annot=True,cmap=plt.cm.nipy_spectral_r) 
plt.show()





#NOTE K FOLD CROSS-VALIDATION
kfold = KFold(n_splits=10, random_state=11, shuffle=True)
scores = cross_val_score(estimator=knn, X=digits.data, y=digits.target, cv=kfold)
print("cross-validation scores: " , scores)
print("cross-validation average: " , scores.mean())






print("n\nnow using another multiple algos at once...")
time.sleep(3)




estimators = {
    'KNeighborsClassifier': knn, 
    'SVC': SVC(gamma='scale'),
    'GaussianNB': GaussianNB()
}

for estimator_name, estimator_object in estimators.items():

    kfold = KFold(n_splits=10, random_state=11, shuffle=True)
    scores = cross_val_score(estimator=estimator_object, X=digits.data, y=digits.target, cv=kfold)

    print(f'{estimator_name:>20}: ' + 
          f'mean accuracy={scores.mean():.2%}; ' +
          f'standard deviation={scores.std():.2%}')







print("\n\nnow changing hyperparameters on k clusters...")
print("adding more clusters to algo...")
time.sleep(3)



for cluster_amount in range(1, 20, 2): 
    kfold = KFold(n_splits=10, random_state=11, shuffle=True)
    knn = KNeighborsClassifier(n_neighbors=cluster_amount)
    scores = cross_val_score(estimator=knn,  X=digits.data, y=digits.target, cv=kfold)

    print(f'k={cluster_amount:<2}; mean accuracy={scores.mean():.2%}; ' + f'standard deviation={scores.std():.2%}')