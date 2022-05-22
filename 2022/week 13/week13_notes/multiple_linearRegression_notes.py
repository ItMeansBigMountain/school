import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression , ElasticNet, Lasso, Ridge
from sklearn.datasets import fetch_california_housing
from sklearn import metrics
from sklearn.model_selection import KFold, cross_val_score



import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt






# DATA OBJECT
california = fetch_california_housing()  
pd.set_option('precision', 4)  # 4 digit precision for floats
california_df = pd.DataFrame(california.data, columns=california.feature_names)
pd.set_option('max_columns', 9)  # display up to 9 columns in DataFrame outputs
pd.set_option('display.width', None)  # auto-detect the display width for wrapping
california_df['MedHouseValue'] = pd.Series(california.target)
print(california_df)
# print(california_df.describe())
exit()





# GRAPHING RANDOM SAMPLE OF OUR DATASET
# sample_df = california_df.sample(frac=0.1, random_state=17)
# sns.set_style('whitegrid')                                    
# for feature in california.feature_names:
#     plt.figure(figsize=(8, 4.5))  # 8"-by-4.5" Figure
#     sns.scatterplot(data=sample_df, x=feature, 
#                     y='MedHouseValue', hue='MedHouseValue', 
#                     palette='cool', legend=False)
# plt.show()













# SPLITTING DATA FOR TRAIN / TEST
X_train, X_test, y_train, y_test = train_test_split( california.data, california.target, random_state=11)








# TRAIN MODEL
linear_regression = LinearRegression()
linear_regression.fit(X=X_train, y=y_train)



# DISPLAY SLOPES FOR METRICS FOUND
# for i, name in enumerate(california.feature_names):
#     print(f'{name:>10}: {linear_regression.coef_[i]}')  
# print("\n\n")


# PREDICTIONS
predicted = linear_regression.predict(X_test)
expected = y_test



# GRAPHING PREDICTIONS
# ai_df = pd.DataFrame()
# ai_df['Expected'] = pd.Series(expected)
# ai_df['Predicted'] = pd.Series(predicted)

# figure = plt.figure(figsize=(9, 9))
# axes = sns.scatterplot(data=ai_df, x='Expected', y='Predicted',  hue='Predicted', palette='cool', legend=False)
# start = min(expected.min(), predicted.min())
# end = max(expected.max(), predicted.max())
# axes.set_xlim(start, end)
# axes.set_ylim(start, end)
# line = plt.plot([start, end], [start, end], 'k--')
# plt.show()






# R2 SCORE CONFIDENCE | 1:good , 0:bad
# confidence = metrics.r2_score(expected, predicted)
# print(confidence)













# MULTIPLE REGRESSION ESTIMATOR MODELS cross evaluation
estimators = {
    'LinearRegression': linear_regression,
    'ElasticNet': ElasticNet(),
    'Lasso': Lasso(),
    'Ridge': Ridge()
}
for estimator_name, estimator_object in estimators.items():
    kfold = KFold(n_splits=10, random_state=11, shuffle=True)
    scores = cross_val_score(estimator=estimator_object, X=california.data, y=california.target, cv=kfold, scoring='r2')
    print(f'{estimator_name:>16}: ' + f'mean of r2 scores={scores.mean():.3f}')

