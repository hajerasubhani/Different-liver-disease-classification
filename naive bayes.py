import numpy as np  
import matplotlib.pyplot as plt  
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report, confusion_matrix




dataset=pd.read_csv("ALF_Data1.csv")
print(dataset.head())
print(dataset.shape)



X= dataset.iloc[:, :-1].values
y= dataset.iloc[:, 29].values 

from sklearn.model_selection import train_test_split  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)


# training the model on training set 
from sklearn.naive_bayes import GaussianNB 
gnb = GaussianNB() 
gnb.fit(X_train, y_train) 

# making predictions on the testing set 
y_pred = gnb.predict(X_test) 

# comparing actual response values (y_test) with predicted response values (y_pred) 
from sklearn import metrics
print("Confusion Matrix: ",
              confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred)) 

print("Gaussian Naive Bayes model accuracy(in %):", metrics.accuracy_score(y_test, y_pred)*100)
