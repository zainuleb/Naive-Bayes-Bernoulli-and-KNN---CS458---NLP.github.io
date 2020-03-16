from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score
import re

#open dataset
corpus = open('badges.data').read()

#Removing first line.

res = re.sub(r'','',corpus)
dlist=res.split('\n')#.remove(dlsit[0])
dlist.remove(dlist[0])
dlist.remove(dlist[-1])

#dlist
