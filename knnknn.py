#https://stackabuse.com/k-nearest-neighbors-algorithm-in-python-and-scikit-learn/
import numpy as np  
import matplotlib.pyplot as plt  
import pandas as pd


dataset=pd.read_csv("C:\\Users\\9701239167\\Desktop\\m.tech project\\datasets\\2.Acute Liver Failure\\ALF_Data1.csv")

print(dataset.head())

X= dataset.iloc[:, :-1].values 
y= dataset.iloc[:, 29].values

from sklearn.model_selection import train_test_split  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)  
#names=names

#inf=open(infnm,"r")

from sklearn.preprocessing import StandardScaler  
scaler = StandardScaler()  
scaler.fit(X_train)

X_train = scaler.transform(X_train)  
X_test = scaler.transform(X_test)


from sklearn.neighbors import KNeighborsClassifier  
classifier = KNeighborsClassifier(n_neighbors=5)  
classifier.fit(X_train, y_train)  

y_pred = classifier.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix  
print(confusion_matrix(y_test, y_pred))  
print(classification_report(y_test, y_pred)) 
from sklearn.metrics import accuracy_score
print ('Accuracy Score :',accuracy_score(y_test, y_pred))
from sklearn.metrics import precision_score
print (' precision_score:',precision_score(y_test, y_pred))
from sklearn.metrics import recall_score
print ('recall Score :',recall_score(y_test, y_pred))

from sklearn.metrics import f1_score
print ('f1-score :',f1_score(y_test, y_pred))
from sklearn.metrics import error_score
print ('error-score :',error_score(y_test, y_pred))


#https://stackabuse.com/k-nearest-neighbors-algorithm-in-python-and-scikit-learn/
