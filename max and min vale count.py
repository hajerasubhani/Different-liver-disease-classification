import sys
import numpy as np#importing numeric python package and np is the variable which is used to call the function under numpy
import pandas as pd#importing pandas package and pd is the variable which is used to call the function under pandas
import matplotlib.pyplot as plt
import scipy
import sklearn
import seaborn as sns

from pandas.plotting import scatter_matrix

#importing the required dataset file
dataset=pd.read_csv("C:\\Users\\9701239167\\Desktop\\m.tech project\\datasets\\2.Acute Liver Failure\\ALF_Data.csv")#reading dataset from the location,data loaded in the variable name dataset

#head function will help us printing top 5 rows(instances) of the dataset
print(dataset.head(5))

print("prints the max vale and in vale")

print(dataset.max())
print(dataset.value_counts())

print("prints the min vale and in vale","\n")

print(dataset.min())
