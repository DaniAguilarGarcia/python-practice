#usinf scikit-learn
from sklearn.cluster import Kmeans
import pandas as pd
#load data
customer_data = pd.read_cvs('customer_data.csv')
#feature selection
X = customer_data[['Number_of_purchases', 'Age']]

#cluster into segments
kmeans = KMeans(n_cluster=5)
customer_data['Cluster'] = kmeans.fit_predict(x)


