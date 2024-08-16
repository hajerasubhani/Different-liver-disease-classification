# import pandas library 
import re
import sys
import pandas as pd 
#dataset1=[] 
# creating file handler for  
# our example.csv file in 
# read mode 
#file_handler=open("dataset.csv","r")

# creating a Pandas DataFrame 
# using read_csv function  
# that reads from a csv file. 
data = pd.read_csv("ALF_Data.csv")
df=data

mod_df=df
  
# closing the file handler 
#file_handler.close() 
                      
Gender={'M':0,'F':1}                   
Region={'north':1,'south':2,'east':3,'west':4}  
Source_of_Care={'Private Hospital':1,'clinic':2,'Never Counsulted':3,'Governament Hospital':4,' ':0}            
        
# traversing through dataframe 
# Gender column and writing 
# values where key matches

data.Gender=[Gender[item] for item in data.Gender]
data.Region=[Region[item] for item in data.Region]
data.Source_of_Care=[Source_of_Care[item] for item in data.Source_of_Care]


print(data)
out=open("ALF_Data1.csv","w")
#for data in dataset1.csv:
  

mod_df.to_csv( "ALF_Data1.csv") #It will create a new file with normalized attributes.

