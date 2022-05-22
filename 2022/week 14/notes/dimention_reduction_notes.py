from sklearn.datasets import load_digits
from sklearn.manifold import TSNE


import matplotlib.pyplot as plt






# DATASET 
digits = load_digits()



# DIMENTIONALITY REDUCTION / ML ALGO
tsne = TSNE(n_components=2, random_state=11)



# TRAINING DATA
reduced_data = tsne.fit_transform(digits.data)



# GRAPHING REDUCED DIMENTIONS DATA
# figure = plt.figure(figsize=(5, 5))
# dots = plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c='black')


figure = plt.figure(figsize=(6, 5))
dots = plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=digits.target, cmap=plt.cm.get_cmap('nipy_spectral_r', 10))
colorbar = plt.colorbar(dots) 
plt.show()


