# DATASET LIBRARIES
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np



# ESTIMATORS
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN, MeanShift, SpectralClustering, AgglomerativeClustering
from sklearn.decomposition import PCA




# GRAPHING
import seaborn as sns
import matplotlib.pyplot as plt







# DATASET
iris = load_iris() #csv

iris_df = pd.DataFrame(iris.data, columns=iris.feature_names) #pandas
iris_df['species'] = [iris.target_names[i] for i in iris.target] #checking targets for learning (unsupervised wouldn't)






# NOTE NO DIMENTION REDUCTION

# VISUALIZING DATAFRAME
# sns.set_style('whitegrid')
# grid = sns.pairplot(data=iris_df, vars=iris_df.columns[0:4] ) #un-supervised
# grid = sns.pairplot(data=iris_df, vars=iris_df.columns[0:4], hue='species') #supervised
# plt.show()


# K-MEANS ESTIMATOR MODEL (unsupervised so no target data!)
kmeans = KMeans(n_clusters=3, random_state=11)
kmeans.fit(iris.data)


# DISPLAYING CLASSIFICATION PREDICTIONS VS TARGET
# print(  kmeans.labels_   ) 
# print(  "vs."   )
# print(  [  i[0]    for i in iris_df['species']  ]   )













# NOTE DIMENTIONALITY REDUCTION
pca = PCA(n_components=2, random_state=11)

# TRAINING MODEL
pca.fit(iris.data)  #4 columns of dimentions (features)

# REDUCE DIMENTIONS
iris_pca = pca.transform(iris.data) #2 columns of dimentions (features) --> refer to PCA(n_components)
# print(iris.data.shape , "vs." , iris_pca.shape )



# REDUCED DIMENTION PANDAS DATAFRAME
iris_pca_df = pd.DataFrame(iris_pca, columns=['reduct.Component1', 'reduct.Component2'])
iris_pca_df['species'] = iris_df.species #target produced for testing purposes





# VISUALIZING CENTROIDS OF CLUSTERS (middle point of euclidean distances within each cluser)
# iris_centers = pca.transform(kmeans.cluster_centers_)                   # reduce centroids to 2 dimensions 
# axes = sns.scatterplot(data=iris_pca_df, x='reduct.Component1', y='reduct.Component2', hue='species', legend='brief') 
# dots = plt.scatter(iris_centers[:,0], iris_centers[:,1], s=100, c='k')  # plot centroids as larger black dots
# plt.show()







# RUNNING MULTIPLE CLUSTER ESTIMATORS 
estimators = {
    'KMeans': kmeans,
    'DBSCAN': DBSCAN(),
    'MeanShift': MeanShift(),
    'SpectralClustering': SpectralClustering(n_clusters=3),
    'AgglomerativeClustering': AgglomerativeClustering(n_clusters=3)
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

