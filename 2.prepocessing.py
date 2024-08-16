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

print( "#printing the dataset" )
print(dataset)

print("#to know what are the columns in ur dataset")
print(dataset.columns)

print("#head function will help us printing top 5 rows(instances) of the dataset")
print(dataset.head(5))

print("#tail function will help us printing bottom 5 rows(instances) of the dataset")
print(dataset.tail(5))

print("#checking number of null values in each attribute ")
print(dataset.isnull().sum())

print("#Another useful method if value_counts() which can get count of each category in a categorical attributed series of values. For an instance suppose you are dealing with a dataset of customers who are divided as youth, medium and old categories under column name age and your dataframe is “DF”. You can run this statement to know how many people fall in respective categories. In our data set example education column can be used")
print(dataset["Age"].value_counts()) 
print(dataset["Gender"].value_counts()) 
print(dataset["Region"].value_counts()) 
print(dataset["Weight"].value_counts()) 
print(dataset["Height"].value_counts())
print(dataset["Body Mass Index"].value_counts())
#print(dataset["Source of Care"].value_counts()) 


print("# for computing correlations")
print(dataset.corr())



plt.show(sns.heatmap(dataset.corr(),cmap='Blues',annot=True))

print("# computes numerical data ranks ")
print(dataset.rank())

print("# prints first 5 rows and every column which replicates dataset.head() ")
print(dataset.iloc[0:5,:]) 
# prints entire rows and columns 
print(dataset.iloc[:,:]) 
# prints from 5th rows and first 5 columns 
print(dataset.iloc[5:,:5])

#descriptions
print(dataset.describe())


#gives the count and datatype of the dataset
dataset.info()
print('')

#total number of rows and columns
print(dataset.shape)
print("\n")


#describe function is used to find out the total count,mean,standard deviation,minimum value,maximum value,25,50,70 percentage of the dataset used for further reference
# computes various summary statistics, excluding NaN values print(dataset.describe())
print(type(dataset))


print("#checking number of null values in each attribute ")
print(dataset.isnull().sum())

print("#checking number of null values in each attribute ")
print(dataset.isnull().sum(),axis=0)




