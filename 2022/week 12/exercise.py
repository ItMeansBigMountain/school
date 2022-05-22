import time

# SAMPLE DATA
from sklearn.datasets import load_digits

# DATAFRAMES
import pandas as pd

# CROSS VALIDATION
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

# SPLITTING DATA
from sklearn.model_selection import train_test_split

# TRAINING MODELS
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier

# CONFUSION MATRIX
from sklearn.metrics import confusion_matrix

# GRAPHING
import matplotlib.pyplot as plt
import seaborn as sns


# LOAD DATASET
digits = load_digits()


# DISPLAY DATASET INFORMATION
print(digits.DESCR)
print("Target sample outcomes", digits.target[::100])
print("Training set", digits.data.shape)
print("Testing set", digits.target.shape)
print("\nData tested as '3' \n", digits.images[13])


# GRAPHING IMAGE
figure, axes = plt.subplots(nrows=4, ncols=6, figsize=(6, 4))
for item in zip(axes.ravel(), digits.images, digits.target):
    axes, image, target = item
    axes.imshow(image, cmap=plt.cm.gray_r)
    axes.set_xticks([])
    axes.set_yticks([])
    axes.set_title(target)
plt.tight_layout()
print("Displaying First 24 Pictures In Data Set...")
plt.show()


# K NEAREST-NEIGHBORS MANUAL SPLIT ANALYSIS
# SPLIT DATA INTO TWO SECTIONS : Train / Test
X_train, X_test, y_train, y_test = train_test_split(
    digits.data, digits.target, random_state=11)
knn = KNeighborsClassifier()
knn.fit(X=X_train, y=y_train)
predicted = knn.predict(X=X_test)
expected = y_test
wrong = [(p, e) for (p, e) in zip(predicted, expected) if p != e]
print("\n\nK Nearest-Neighbors Single Split")  # output
print(f"{predicted[:20] = }")
print(f"{expected[:20] = }")
print(f"{wrong = }")
print(f'KNN Score: {knn.score(X_test, y_test):.2%}')

confusion = confusion_matrix(
    y_true=expected, y_pred=predicted)  # confusion matrix
print("\nCONFUSION MATRIX\n", confusion)
confusion_df = pd.DataFrame(confusion, index=range(10), columns=range(10))
figure = plt.figure(figsize=(7, 6))
axes = sns.heatmap(confusion_df, annot=True, cmap=plt.cm.nipy_spectral_r)
print("Displaying MATRIX...")
plt.show()

# [K] FOLD CROSS-VALIDATION
kfold = KFold(n_splits=10, random_state=11, shuffle=True)
scores = cross_val_score(estimator=knn, X=digits.data,
                         y=digits.target, cv=kfold)
print("CROSS VALIDATION technique Scores of iterations\n",
      [f"{decimalVar:.2%}" for decimalVar in scores])
print(f'Mean accuracy: {scores.mean():.2%}')


# CROSS VALIDATION USING MULTIPLE "ML CLASSIFICATION ALGORITHMS"
print('\n\n\nCROSS VALIDATION USING MULTIPLE "ML CLASSIFICATION ALGORITHMS"')
estimators = {
    'KNN': knn,
    'SVC': SVC(gamma='scale'),
    'GaussianNB': GaussianNB(),
    "Decision Tree": DecisionTreeClassifier()
}
maximum_accuracy = 0
maximum_output = ""
for estimator_name, estimator_object in estimators.items():
    kfold = KFold(n_splits=10, random_state=11, shuffle=True)
    scores = cross_val_score(estimator=estimator_object,
                             X=digits.data, y=digits.target, cv=kfold)
    print(f'{estimator_name:>20}: ' +
          f'mean accuracy={scores.mean():.2%}; ' +
          f'standard deviation={scores.std():.2%}')
    if scores.mean() > maximum_accuracy:
        maximum_accuracy = scores.mean()
        maximum_output = estimator_name
print("\nMax Effeciancy: ", maximum_output)


# HYPER PARAMETER TUNING
print('\n\n\nK Nearest-Neighbors HYPER PARAMETER TUNING\n\tloop of changing amount of neighbors to dictate bias')
maximum_accuracy = 0
maximum_output = ""
for k in range(1, 20, 2):  # k is an odd value 1-19; odds prevent ties
    kfold = KFold(n_splits=10, random_state=11, shuffle=True)
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(estimator=knn,
                             X=digits.data, y=digits.target, cv=kfold)
    if scores.mean() > maximum_accuracy:
        maximum_accuracy = scores.mean()
        maximum_output = f'k={k:<2}; mean accuracy={scores.mean():.2%}; ' + \
            f'standard deviation={scores.std():.2%}'
    print(f'k={k:<2}; mean accuracy={scores.mean():.2%}; ' +
          f'standard deviation={scores.std():.2%}')
print("\nMax Effeciancy\n\t", maximum_output)
