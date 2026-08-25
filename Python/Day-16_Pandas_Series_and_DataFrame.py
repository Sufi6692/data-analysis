# Note - Pandas match the data by index label
# If any label is missing -> Nan

import pandas as pd
# Statistical Operations 

s1 = pd.Series([100,200,300,400])
s2 = pd.Series([500,600,700,800])


print(s1)

print("mean of a series-",s1.mean())
print("sum of series-",s1.sum())
print("max vlaue of a series-",s1.max())
print("min value of a series-",s1.min())
print("median of a series-",s1.median())
print("standard deviation of a series-",s1.std())
print("variance of series-",s1.var())


#Some more function -

# if you want to the stats summary of the data - data.describe()

print(s1)

print(s1.describe())

# Series Manupulation it refers to changing values,index,datatype or structure of a series 

a = pd.Series([101,102,'a','python',90,99])
print(a)

#updating the values
a[3] = 'Java'

print(a)

## apply() -- > It applies a custom function to each and every element of a series 
# series.apply(function)

z1 = pd.Series([100,200,300,400,5])
z1.apply(lambda i:i+10)

print(z1)

print(z1.apply(str))


## Replace() -- > It will replace a specific value - syntax 
# series.replace(value_replace, new_value)

print(a)

a.replace(101,'sunday')

## rename() --> renames the index label without changing original series

print(a)

a.rename(index={0:'a',1:'b',2:'c',3:'d',4:'e',5:'f'})

print(a)

# Concatenation of a series

s1 = pd.Series([100,200,300,400,99])
s2 = pd.Series([500,600,700,800])
print(pd.concat([s1,s2]))

# Conditional filtering and storing in a series

marks = pd.Series([45,78,88,32,95,33,41,28,19,18,17])
print(marks)

# syntax - series[condition]

print(marks[(marks>60) & (marks<70)])

#  SORTING THE DATA -> ARRANGE THE DATA IN A SPECIFIC ORDER
# SOR THE DATA BY USING EITHER VALUES OR INDEX

marks = pd.Series([45,78,88,32,95,33,41,28,19,18,17])
print(marks)

# sort_values() - sort the data based on their values

print(marks.sort_values())

# by default data will sort in ascending order

print(marks.sort_values(ascending=False))

# sort.index() - sort the data on index labels

x = pd.Series([70,78,'a','i','red',34],index =['hello','avni','riya','rahul','python','java'])
print(x)

print(x.sort_index())

print(x.index)
print(x.values)

# Dataframe  a dataframe is a 2 dimensional, labeled, tabular structure in Pandas a table with rows and columns

## DataFrame = multiple series aligned by index

# creating a dataframe ---> pd.DataFrame()

d1 = {'a':['raju','aman','amit','neha'],'b':[101,102,103,104],'c':['red','yellow','green','orange']}
print(d1)

df1 = pd.DataFrame(d1)
# the keys in dictionary are acting here as column label

print(df1)


# from Excel/CSV file
df = pd.read_csv("purchase_data.csv")

print(df)

l1 = [[1,'avni',3],['a','b','c'],[10,30,20]]
print(l1)

df = pd.DataFrame(l1,columns=['random1','random2','random'])
print(df)

df=pd.DataFrame(l1)

print(df)


#some basic DataFrame attrubutes

# df.shape --> gives the no.of rows and columns

print(df.shape)

#df.columns --> display all the column names which are present the data

print(df.columns)

#df.dtypes --> data type of each columns

print(df.dtypes)

print(df1)

# 1 -- selecting/accessing column

print(df1['b'])

print(df1[['a','c']])

#selecting the rows
# loc --> label based 

print(df.loc[2])

print(df.loc[0:2])

#iloc --> integer position based access

print(df.iloc[0])






















