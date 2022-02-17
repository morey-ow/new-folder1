# from the book Matplotlib by Hekkert
#Devert, Alexandre. Matplotlib Plotting Cookbook, Packt Publishing, Limited, 2014. ProQuest Ebook Central, http://ebookcentral.proquest.com/lib/oldwestbury-ebooks/detail.action?docID=1600396. Created from oldwestbury-ebooks on 2022-02-06 19:17:44.
#Copyright © 2014. Packt Publishing, Limited. All rights reserved.

#%%
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('my_data.txt') 
for column in data.T: #we need to transpose the matrix so we can loop through columns, because a matrix is a list of rows
	plt.plot(data[:,0] , column)  #data[:,0] 
plt.show()
# %%

#%%
b=data.T
# %%
import numpy as np
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA 
from sklearn.preprocessing import scale 
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
import matplotlib.cm as cm
digits = load_digits()
data = digits.data
n_samples, n_features = data.shape 
n_digits = len(np.unique(digits.target)) 
labels = digits.target
# %%
labels
len(labels)
# %%
pca = PCA(n_components=10)
data_r = pca.fit(data).transform(data)
print('explained variance ratio (first two components): %s' % str(pca.explained_variance_ratio_))
print('sum of explained variance (first two components): %s' % str(sum(pca.explained_variance_ratio_)))

# %%
