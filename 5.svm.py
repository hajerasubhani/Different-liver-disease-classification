#Import Library

import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn import svm
import re
import pandas as pd

X=[]
Y=[]
Xt=[]
#X = np.array([])
#Xt = np.array([])
Xpre=[]  #predector variable
Yout=[]   #target variable
Xtest=[]  #test data
Ytest=[]
j=0
k=0
#Assumed you have, X (predictor) and Y (target) for training data set and x_test(predictor) of test_dataset
# Create SVM classification object

#### open input file with read mode

infnm=input("enter your input file name")

inf=open(infnm,"r")

for ln in inf:
    ln=ln.rstrip()
    ln=ln.lstrip()
    #print(ln)
    tks=ln.split(",")
    #url=tks[0]
    #cls=tks[1]
    n=len(tks)
    Xpre=[]
    for i in range(0,n-1):
        t=tks[i]
        if t=="":
            #t=float(tks[i])
            t=0.0
            Xpre.append(t)
        else:
            t=float(t)
            Xpre.append(t)
    t=tks[n-1]
    Y.append(t)
    X.append(Xpre)
    

#Y=np.array(Yout)

#plt.scatter(X[:, 0], X[:, 1], c=Y, s=50, cmap='autumn');
#plt.show()
###SVM model 
clf = SVC(kernel='linear')#clf is the object created for class
clf.fit(X, Y)#fit is the method inside SVC class
               
outfnm=input("enter your test file name")

tinf=open(outfnm,"r")

for ln in tinf:
    ln=ln.rstrip()
    ln=ln.lstrip()
    #print(ln)
    tks=ln.split(",")
    #print(ln)
    #data.append(row[:-1])
    #target.append(row[-1])
    #url=tks[0]
    #cls=tks[1]
    n=len(tks)
    Xtest=[]
    Xt=[]
    for i in range(0,n-1):
        t=tks[i]
        if t=="":
            t=0.0
            Xtest.append(t)
        else:
            t=float(t)
            Xtest.append(t)
    ot=tks[n-1]
    Xt.append(Xtest)
    Ytest.append(ot)
    
    #clf = SVC(kernel='linear')
    #clf.fit(X, Y)
    prediction = clf.predict(Xt)
    print(prediction,",",ot)        

