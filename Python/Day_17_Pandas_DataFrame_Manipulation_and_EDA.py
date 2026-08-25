import pandas as pd


df2 = pd.DataFrame({'name':['raj','siya','harman','yash'],'age':[24,21,19,17],'gender':['M','F','M','M']})
print(df2)


print(df2.drop('age',axis=1,inplace=False))

print(df2)


print(df2[df2['age']>20])

print([(df2['age']>20)& (df2['gender']=='F')])

print(df2[df2['name']=='raj'])


# DataFrame Manipulation

# 1 Remove the columns

print(df2)


print(df2.drop('age',axis=1,inplace=True))

#df2.drop(column=[],inplace=True) this line will help you to remove multiple columns

print(df2)

# inplace = True ---> original DataFrame is changed permanently
# inplace = False(default) ---> original DataFrame is not changed instead of this it will give you a new dataframe


# rename the columns -----> rename()
# df2.rename(columns={'old':'new_name'})


# # Sorting Data
# .sort_values()
# .sort_index()



# concatenation of DataFrame


d1 = pd.DataFrame({"Id":[1,2],"Name":['A','B']})
d2 = pd.DataFrame({"Age":[28,29],"Grade":['C','D']})

pd.concat([d1,d2],ignore_index=True)

"""
result =pd.concat(
    [df1,df2], #obj
    axis = 0,
    join='outer',
    ignore_index=True,
    keys=["first","Second"],
    sort=False,
    copy=True,
)
print(result)


"""

# groupby() ---> divide the data into groups

x2 = pd.DataFrame({'city':["Banglore","Delhi","Banglore","Mumbai","Banglore"],"Sales":[30,40,50,60,70]})
print(x2)


result = x2.groupby('city', as_index=False).agg(
    Average_Sales=('Sales', 'mean')
)

print(result)


# avg sales based on city

x2.groupby('city')['Sales'].mean()



#Handling the null or missing values


import numpy as np
df2 = pd.DataFrame({'age':[10,20,np.nan],'gender':['m','f','f'],'name':['riya',np.nan,np.nan]})

print(df2)


print(df2.isnull())


df2.isnull().sum() # give the count of null values in each column
# df2.count()

df2.isnull().sum().sum()


# How to handle them??
# 1 - Delete the null values ---> df.dropna(inplace=True)
# 2 - fill the null values with other values(mean,median,mode,constant value) --> df.fillna(value,inplace=True)


print(df2)


df2['age'] = df2['age'].fillna(0)
print(df2)


df2.dropna(inplace = True)  # remove the entire row where null value is present


print(df2)

df2.isnull().sum()

"""
EDA(Exploratory Data Analysis)
  Understanding the data before building any model
  helps us to discover different patterns, clean data,and uncover relationships

"""


# Load the data
# view the data -> top rows, bottom rows
# understand the data-> Informaion, staistical summary about the data, shape
# check null values
# if we null values -> handle them
# check for duplicate values
# if we have duplicate values -> remove duplicate values
# column wise analysis
# outlier detection
# correlation


import seaborn as sns

df = sns.load_dataset('titanic') # in-built dataset





























