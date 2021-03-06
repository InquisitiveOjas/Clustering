
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset=pd.read_csv('mall.csv')
X=dataset.iloc[:,[3,4]].values

#using the dendrogram to find the optimum number of clusters
#linkage is the algorithm of hierarchical clustering 
import scipy.cluster.hierarchy as sch
dendrogram=sch.dendrogram(sch.linkage(X, method='ward'))
#ward is the method used to minimize the variance in each of the clusters
plt.title('Denrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean Distances')
plt.show()

#fitting clustering to the data set
from sklearn.cluster import AgglomerativeClustering
hc=AgglomerativeClustering(n_clusters=5,affininty='euclidean',linkage='ward')
y_hc=hc.fit_predict(X)

#visulaising the clusters
plt.scatter(X[y_hc ==0,0],X[y_hc ==0,1],s=100,c='red', label='Cluster 1 :- Careful')
plt.scatter(X[y_hc ==1,0],X[y_hc ==1,1],s=100,c='blue', label='Cluster 2:- Standard')
plt.scatter(X[y_hc ==2,0],X[y_hc ==2,1],s=100,c='green', label='Cluster 3:-Target')
plt.scatter(X[y_hc ==3,0],X[y_hc ==3,1],s=100,c='magenta', label='Cluster 4:- Careless')
plt.scatter(X[y_hc ==4,0],X[y_hc ==4,1],s=100,c='cyan', label='Cluster 5:- Sensible')
plt.title('Clusters of  Clients')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()  
