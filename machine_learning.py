import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression, LinearRegression

df = pd.read_csv('train_modified.csv', header = 0) #Import the condensed/modified csv file from pandas_tut.py
df_array = df.as_matrix() #We must convert the dataframe to a numpy array before performing regression
#First, let's see how to implement random forest
#For more information on how random forests work: https://citizennet.com/blog/2012/11/10/random-forests-ensembles-and-performance-metrics/

# Create the random forest object which will include all the parameters for the fit
forest = RandomForestClassifier(n_estimators = 100)

# Fit the training data to the Survived labels and create the decision trees
forest = forest.fit(df_array[0::,1::],df_array[0::,0]) #The Survived Column (y-values) are in the 0th column, and the X values are in columns 1 onwards

#Compute the accuracy of the classifier on the test data
print(forest.score(df_array[0::,1::],df_array[0::,0]))

#output = forest.predict(test_data).astype(int) #Run the classfier on test data

#Next, let's try some logistic regression
model = LogisticRegression()
model = model.fit(df_array[0::,1::],df_array[0::,0])
print(model.score(df_array[0::,1::],df_array[0::,0]))


#Here I'll just show you how to do multivariate linear regression, although it does not directly pertain to classification
lm = LinearRegression()
lm = lm.fit(df[['Pclass','FamilySize']].as_matrix(), df['Age'].as_matrix()) #Predict the passenger age from class and family size
print(lm.score(df[['Pclass','FamilySize']].as_matrix(), df['Age'].as_matrix())) #Calculate R^2
