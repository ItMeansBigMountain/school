import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression , ElasticNet, Lasso, Ridge
from sklearn.datasets import load_diabetes
from sklearn import metrics
from sklearn.model_selection import KFold, cross_val_score



import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt



'''
15.15

    The dataset contains 442 samples, each with 10 features and a label indicating the “dis-
    ease progression one year after baseline.” Using this dataset, reimplement the steps of
    this chapter's multiple linear regression case study in Section 15.5.

'''



# DATA OBJECT
diabetes = load_diabetes()  
diabetes_df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
diabetes_df['1 Year Disease Progression'] = pd.Series(diabetes.target)
# print(diabetes_df)
# print(diabetes_df.describe())






# GRAPHING RANDOM SAMPLE OF OUR DATASET
sample_df = diabetes_df.sample(frac=0.1, random_state=17)
sns.set_style('whitegrid')                                    
for feature in diabetes.feature_names:
    plt.figure(figsize=(8, 4.5))  # 8"-by-4.5" Figure
    sns.scatterplot(data=sample_df, x=feature, y='1 Year Disease Progression', hue='1 Year Disease Progression', palette='cool', legend=False)
plt.show()











# SPLITTING DATA FOR TRAIN / TEST
X_train, X_test, y_train, y_test = train_test_split( diabetes.data, diabetes.target )








# TRAIN MODEL
linear_regression = LinearRegression()
linear_regression.fit(X=X_train, y=y_train)



# DISPLAY SLOPES FOR METRICS FOUND
for i, name in enumerate(diabetes.feature_names):
    print(f'{name:>10}: {linear_regression.coef_[i]}')  


# PREDICTIONS
predicted = linear_regression.predict(X_test)
expected = y_test



# GRAPHING PREDICTIONS
ai_df = pd.DataFrame()
ai_df['Expected'] = pd.Series(expected)
ai_df['Predicted'] = pd.Series(predicted)

figure = plt.figure(figsize=(9, 9))
axes = sns.scatterplot(data=ai_df, x='Expected', y='Predicted',  hue='Predicted', palette='cool', legend=False)
start = min(expected.min(), predicted.min())
end = max(expected.max(), predicted.max())
axes.set_xlim(start, end)
axes.set_ylim(start, end)
line = plt.plot([start, end], [start, end], 'k--')
plt.show()






# R2 SCORE CONFIDENCE | 1:good , 0:bad
confidence = metrics.r2_score(expected, predicted)
print("R2 Score:", confidence)








# MULTIPLE REGRESSION ESTIMATOR MODELS cross evaluation
print("\n\n\tNOW USING MULTIPLE REGRESSION ESTIMATORS...\n")
estimators = {
    'LinearRegression': linear_regression,
    'ElasticNet': ElasticNet(),
    'Lasso': Lasso(),
    'Ridge': Ridge()
}
for estimator_name, estimator_object in estimators.items():
    kfold = KFold(n_splits=10, random_state=11, shuffle=True)
    scores = cross_val_score(estimator=estimator_object, X=diabetes.data, y=diabetes.target, cv=kfold, scoring='r2')
    print(f'{estimator_name:>16}: ' + f'mean of r2 scores={scores.mean():.3f}')

