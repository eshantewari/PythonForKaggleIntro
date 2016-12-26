import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt

df = pd.read_csv('train.csv', header = 0) #Take csv file that has a header row and make it a DataFrame
print(df) #Print the entire data frame
print(df.head(3)) #Print the first three rows
print(df.dtypes) #Print the column data types
print(df.info()) #Print information about the columns
print(df.describe()) #print statistics about the columns
print(df['Age'][0:10]) #Print the first 10 rows of the age column
print(type(df['Age'])) #Note that the type of the Age column is not an array, but rather a vector
print(df['Age'].mean()) #Print the mean of all ages that are numeric
print(df[['Sex','Pclass','Age']]) #Print the three columns
plt.hist(df['Age'].dropna()) #Drop the NaN values in the Age column and plot a histogram
plt.show()

df['Gender'] = df['Sex'].map({'female':0,'male':1}).astype(int) #Create new gender column, mapping female to 0 and male to 1 from the sex column
df['FamilySize'] = df['SibSp']+df['Parch'] #Create New Column with the total family size (siblings+parents)
df.drop(['PassengerId','Name','Sex','Ticket','Cabin','Embarked'], axis = 1, inplace = True) #Drop all columns that I don't want for my classification step: you can add columns or choose some of these to keep. InPlace makes the df update without reassignment.
df.dropna(inplace = True) #Drop all rows with a NaN from the DataFrame. We are losing so much data here: do something smarter
df.to_csv('train_modified.csv',index=False,float_format="%d") #Dump the df to a csv, without row indicies and with data formatted as digits
