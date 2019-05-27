
from sklearn.datasets import fetch_20newsgroups
from pprint import pprint


newsgroups_train = fetch_20newsgroups(subset='train')

#pprint(list(newsgroups_train.target_names))

x=newsgroups_train.filenames.shape
y=newsgroups_train.target.shape
z=newsgroups_train.target[:10]

#print(x,y,z)
#print(newsgroups_train.filenames)
print(newsgroups_train.target)