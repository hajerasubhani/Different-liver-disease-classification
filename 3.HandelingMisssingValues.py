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

df=dataset
mod_df=df
dataset['Weight'].fillna(value=dataset['Weight'].mean(),axis=0,inplace=True)
dataset['Height'].fillna(value=dataset['Height'].mean(),axis=0,inplace=True)
dataset['Body Mass Index'].fillna(value=dataset['Body Mass Index'].mean(),axis=0,inplace=True)
dataset['Obesity'].fillna(value=dataset['Obesity'].mean(),axis=0,inplace=True)
dataset['Waist'].fillna(value=dataset['Waist'].mean(),axis=0,inplace=True)
dataset['Maximum Blood Pressure'].fillna(value=dataset['Maximum Blood Pressure'].mean(),axis=0,inplace=True)
dataset['Minimum Blood Pressure'].fillna(value=dataset['Minimum Blood Pressure'].mean(),axis=0,inplace=True)
dataset['Good Cholesterol'].fillna(value=dataset['Good Cholesterol'].mean(),axis=0,inplace=True)
dataset['Bad Cholesterol'].fillna(value=dataset['Bad Cholesterol'].mean(),axis=0,inplace=True)
dataset['Total Cholesterol'].fillna(value=dataset['Total Cholesterol'].mean(),axis=0,inplace=True)
dataset['Physical Activity'].fillna(value=dataset['Physical Activity'].mean(),axis=0,inplace=True)
dataset['Education'].fillna(value=dataset['Education'].mean(),axis=0,inplace=True)
dataset['Unmarried'].fillna(value=dataset['Unmarried'].mean(),axis=0,inplace=True)
dataset['Income'].fillna(value=dataset['Income'].mean(),axis=0,inplace=True)
dataset['PoorVision'].fillna(value=dataset['PoorVision'].mean(),axis=0,inplace=True)
dataset['HyperTension'].fillna(value=dataset['HyperTension'].mean(),axis=0,inplace=True)
dataset['Diabetes'].fillna(value=dataset['Diabetes'].mean(),axis=0,inplace=True)
dataset['Hepatitis'].fillna(value=dataset['Hepatitis'].mean(),axis=0,inplace=True)
dataset['Family Hepatitis'].fillna(value=dataset['Family Hepatitis'].mean(),axis=0,inplace=True)
dataset['Chronic Fatigue'].fillna(value=dataset['Chronic Fatigue'].mean(),axis=0,inplace=True)
dataset['ALF'].fillna(value=dataset['ALF'].mean(),axis=0,inplace=True)

print(dataset)
out=open("ALF_Data.csv","w")
mod_df.to_csv("ALF_Data.csv")


print("#checking number of null values in each attribute ")
print(dataset.isnull().sum())


