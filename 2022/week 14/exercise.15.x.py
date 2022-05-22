# DATASET LIBRARIES
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np


# ESTIMATORS
from sklearn.cluster import KMeans , DBSCAN, MeanShift, SpectralClustering, AgglomerativeClustering , AffinityPropagation


# GRAPHING
import seaborn as sns
import matplotlib.pyplot as plt
from itertools import cycle





'''
15.x

    Once completed, how did the estimator you chose perform against
    the others? You can use 15.7.6 here to run all estimators, including your chosen one, at
    the same time.

    RESPONSE:
        Affinity Propagation chooses the number of clusters used for you. This made it somewhat hard to read the actual findings of the algorithm, therefore I looked into some hyperparameter tuning in order to boil down the clusters.

        I left comments within the arguments passed into the model object initialization.

        With 7 clusters, the setosa plant species were separated into two clusters.

        With 6 clusters, the setosa plant was classified as a singularity.

        When comparing the two tunings, I noticed that 7 clusters gave the setosa two classifications, Versicolor two classifications with a couple of outliers from the virginica cluster group, and virginica received three clusters with some outliers from the Versicolor groups.

        When analyzing the 6 cluster tuning, setosa received one distinct cluster, and the other two had the same pattern as the prior, default tuning [7 clusters].

        With these classification label numbers grouped into relative sub-groups, a data scientist can use a trained eye to create a scope of accuracy that may actually be more accurate than broader scoped clusters used in other estimators shown in your lecture. Using a majority vote we can eliminate the outliers and distinguish a percentage of accuracy but that is cheating since if this were unlabeled data, we would not know which plant is whom. Only after using Affinity Propagation clustering with labeled data, then aggregating the sub-groups into respective representations can we find a reliable source of predictability.

        I would use an algorithm that allows me to identify k amount of clusters in order to let the computer do its "magic" since the data would not be under my control in an unsupervised environment.
    

'''







# DATASET
iris = load_iris() #csv

iris_df = pd.DataFrame(iris.data, columns=iris.feature_names) #pandas
iris_df['species'] = [iris.target_names[i] for i in iris.target] #checking targets for learning (unsupervised wouldn't)






# VISUALIZING DATAFRAME
sns.set_style('whitegrid')

grid = sns.pairplot(data=iris_df, vars=iris_df.columns[0:4] ) #un-supervised
plt.show()

grid = sns.pairplot(data=iris_df, vars=iris_df.columns[0:4], hue='species') #supervised
plt.show()








# ESTIMATOR MODEL (unsupervised so no target data!)
AP = AffinityPropagation(
    # damping=0.5,    # 7 clusers ---> DEFAULT
    damping=0.7,  # 6 clusters --->  HYPERPARAMETER TUNING
    max_iter=1000,
    convergence_iter=500,
    copy=True,
    preference=None,
    affinity='euclidean',
    verbose=True
)


# TRAINING MODEL
AP.fit(iris.data)

# attribs
cluster_centers_indices = AP.cluster_centers_indices_
labels = AP.labels_
n_clusters_ = len(cluster_centers_indices)






#  *************    DEBUG    *************
# print() 
# print(  labels[0:50]   ) 
# print(  [  i[:3]    for i in iris_df['species'][0:50]  ]   )
# print("\n\n") 
# print(  labels[50:100]   ) 
# print(  [  i[:3]    for i in iris_df['species'][50:100]  ]   )
# print("\n\n") 
# print(  labels[100:150]   ) 
# print(  [  i[:3]    for i in iris_df['species'][100:150]  ]   )
# print("\n") 
# print(  set(iris_df['species'])  )
# print(  'Estimated number of clusters: %d' % n_clusters_  )
# exit()








# VISUALIZING CLASSIFICATION
colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
for k, col in zip(range(n_clusters_), colors):
    class_members = labels == k
    cluster_center = iris.data[cluster_centers_indices[k]]
    plt.plot(iris.data[class_members, 0], iris.data[class_members, 1], col + '.')
    centroid = plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,markeredgecolor='k', markersize=14 , label=str(k))

    for x in iris.data[class_members]:
        plt.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)

plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.legend(bbox_to_anchor=(1, 1), loc='upper left', borderaxespad=0)
plt.show()

















# RUNNING MULTIPLE CLUSTER ESTIMATORS 
estimators = {
    'KMeans': KMeans(n_clusters=3),
    'DBSCAN': DBSCAN(),
    'MeanShift': MeanShift(),
    'SpectralClustering': SpectralClustering(n_clusters=3),
    'AgglomerativeClustering': AgglomerativeClustering(n_clusters=3),
    'Affinity Propagation': AP
}



for name, estimator in estimators.items(): #counting frequencies of clusters classified with each ML model
    estimator.fit(iris.data)
    print(f'\n{name}:')
    for i in range(0, 101, 50):
        labels, counts = np.unique(estimator.labels_[i:i+50], return_counts=True)
        print(f'{i}-{i+50}:')
        for label, count in zip(labels, counts):
            print(f'   label={label}, count={count}')   
    print("------------------")

