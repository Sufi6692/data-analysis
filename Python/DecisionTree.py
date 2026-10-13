

#importing libraries

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



#importing dataset

#another way to import
#from google.colab import files
#uploaded=files.upload()
#df=pd.read_csv('heart.csv')

df=pd.read_csv('heart.csv')

print(df.head())


df.info()



"""
age-->	Age of the patient in years

gender-->	Gender/sex of the patient male->0 and female-1

chestPain-->	Type/level of chest pain experienced-->0 :no chest pain, 1: chest pain related to heart, 2: painthat is unusual, 3:pain related to angina

restingBloodPressure-->	Blood pressure measured while the patient is
resting

cholesterol-->	Cholesterol level of the patient

fastingBloodSugar-->	Indicates whether fasting blood sugar is above
the specified level, 0:high and 1:low

RestingECGresults-->	Result of the ECG test while the patient is at rest 0: normal, 1: possible heart problems , 2: thickening heart wall(Serious)

maximumHeartRate-->	Maximum heart rate achieved during the test

exerciseInducedAngina-->	Whether angina/chest discomfort occurs during exercise, 1-> yes and 0 -> no

oldpeak-->	Change/depression in the ST segment during exercise compared with rest

slope-->	Slope of the peak exercise ST segment, 0-->normal, 1-->flat(possibble heart problem), 2 downsloping(serious problem)

numberOfMajorVessels-->	Number of major blood vessels identified as
affected

thalassemia-->	Thalassemia-related test/result category 1: fixed defect(permanent damage), 2: temporary damage, 3->normal

target-->	Our prediction column — whether heart disease is present
0-> no disease, 1->disease

"""


#why decision tree and not binary classification(LogisticRegression)?
#since the target is binary we can move forward with logistic and decision tree.
#we choose decision tree because the tee can capture nonlinear relationship and feature interaction without requiring feature scaling


print(df.columns)

"""
EDA

-null value

-duplicates

-outliers

-encoding

"""

# null values

print(df.info())


df.isnull().sum()

df.isnull().sum().sum() #no null values

df['target'].value_counts()


#Duplicates

df.duplicated().sum() 

df.drop_duplicates(inplace=True)

df.duplicated().sum() #no duplicates



# Outliers

for i in df.columns:
    if(df[i].dtype !='str'):
        plt.boxplot(df[i])
        plt.title(i)
        plt.show()

#remove outliers
#we will not remove outliers
#medical dataset
#decision tree are less affected by outliers -->because they split using conditions rather than calculating distance.
#so, u dont remove the outliers but u remove errors /impossible values

#encoding-->categorical to numeric


df.info()


# Building MI Model 


# spliting data into x and y
# spliting data into training an test
# train
# test
# validating

df.columns


df.shape

x = df.drop(columns ='target')
y = df['target']

x.shape

y.shape

#spliting into train test


from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.20,random_state=42)


#np.random.seed(42)
#np.random.randint(0,100,20)
#random seed is fixing /helping in reproducing random data


x_train.shape

x_test.shape














































































































































































































