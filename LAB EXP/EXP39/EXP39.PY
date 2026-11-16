from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

iris = load_iris()
X = StandardScaler().fit_transform(iris.data)

pca = PCA(n_components=2)
Xp = pca.fit_transform(X)
print("Explained variance ratio:", pca.explained_variance_ratio_)

plt.scatter(Xp[:,0], Xp[:,1], c=iris.target, cmap='viridis')
plt.xlabel("PC1"); plt.ylabel("PC2"); plt.title("PCA of Iris"); plt.show()
