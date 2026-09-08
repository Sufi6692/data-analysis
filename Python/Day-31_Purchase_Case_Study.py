# Day 30 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("purchase_data.csv")

print(df)



"""
 # EDA Exloratory data analysis
1. Null values (finding and removing or dropping)
2. duplicates
3. outliers
5. label encoding

*   List item
*   List item

"""

print(df['Stay_In_Current_City_Years'].unique())

df['Stay_In_Current_City_Years'] = df['Stay_In_Current_City_Years'].replace('4+','4')

print(df['Stay_In_Current_City_Years'].unique())

df['Stay_In_Current_City_Years'] = df['Stay_In_Current_City_Years'].fillna('0')

print(df['Stay_In_Current_City_Years'].isnull().sum())

print(df['Stay_In_Current_City_Years'].unique())

df['Stay_In_Current_City_Years'] = df['Stay_In_Current_City_Years'].astype(int)

print(df.info())

print(df.isnull().sum())

df[['Product_Category_2','Product_Category_3']] =df[['Product_Category_2','Product_Category_3']].fillna(0.0)

df[['Product_Category_2','Product_Category_3']] = df[['Product_Category_2','Product_Category_3']].astype(int)

print(df.isnull().sum())

df.dropna(inplace=True)

df.isnull().sum()

# -----------------------------
# OUTLIER ANALYSIS
# -----------------------------

print("Shape before removing outliers:", df.shape)

# Boxplot BEFORE removing outliers
plt.figure(figsize=(10, 5))
sns.boxplot(x=df['Purchase'])
plt.title("Purchase - Before Removing Outliers")
plt.show()


# Calculate Q1 and Q3
Q1 = df['Purchase'].quantile(0.25)
Q3 = df['Purchase'].quantile(0.75)

# Calculate IQR
IQR = Q3 - Q1

# Calculate Lower Bound and Upper Bound
LB = Q1 - 1.5 * IQR
UB = Q3 + 1.5 * IQR

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Bound:", LB)
print("Upper Bound:", UB)


# Remove outliers
df = df[
    (df['Purchase'] >= LB) &
    (df['Purchase'] <= UB)
]

print("Shape after removing outliers:", df.shape)


# Boxplot AFTER removing outliers
plt.figure(figsize=(10, 5))
sns.boxplot(x=df['Purchase'])
plt.title("Purchase - After Removing Outliers")
plt.show()

# Label Encoding- Conversion of the object datatype into

df = df.copy()  

cols = ['Gender','Age','City_Category','Product_ID']

print(df['Age'].unique())

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder() #le is an instance

#LinerRegression

# fit: understand the pattern
# tranform - covert the whole col accodding to the parttern

for col in cols:
  df[col] = le.fit_transform(df[col])



# Day 31 



"""
Statiticla Analysis
1. Preparing the samples
2. Creating the hypothesis (Null/Alternate)
3. Applying the test
4. Compare it with the p_vale

if p_value > 0.05  = Fail to reject the null hypo (Accepting the null hypothesis)

if p_Value < 0.05 = reject the null hypo( accept the alternate hypo)


"""



"""
A) It was observed that the average purchase made by the men by the men of the age 18 -25 was 10000. is it still the same ?

"""
# NULL HPOTHESIS : The sample mean is = to the population mean .
# Alternate Hypothesis : (H1) the sample mean is different from the popluation mean

# Extracting the data of of the age group ranging 18 -25
# If you are having the age values from 0 to 17 as 0
# then from 18 to 25 > as 1
new_data = df[(df['Age'] == 1) & (df['Gender'] == 1)]

print(new_data)

# Collect sample population
# random state - fixed sequence of randomly selection represented by number.

sample = new_data.sample(3600,random_state=5)
print(sample)

# Manually checking the null hypthesis

print(new_data['Purchase'].mean())

# Null hypo - will be having the mean as 10000 ?

# hypothesis - mean is not 10000!


print(df)


"""
 STATISTICAL ANALYSIS
1. Prepare sample
2. Creating teh hypothesis (Null,Alternate)
3. Apply the appropriate test
4. Compare the p vlaue


If p_value > 0.05 -> Faild to reject the null hypothesis (Accept the null hypo)
 if P_value < 0.05 -> reject the null hypothesis (Accept the Alternate Hypo)


"""

#  It was observed that the average purchase made by the men of the age 18 - 25 was 10000 is it still the same ?

new_data = df[(df['Age'] == 1) & (df['Gender'] == 1)]
print(new_data)

sample = new_data.sample(3600, random_state= 5)
print(sample)

print(new_data['Purchase'].mean())


# Null hypo = mean will be 10000
# Alternate Hypo = Mean will not be equal to 10000

from scipy.stats import ttest_1samp
a_mean = 10000

t_stat,p_value = ttest_1samp(sample['Purchase'],a_mean)
print(t_stat)
print(p_value)



# t_stat = 6.03
# p_value = 1.7766*10^-9

# p_value < 0.05 -> Reject null hypo
# our p_value is less than 0.05, so we reject the null hypothesis
# Therefore, any Purchase of the mean category aged between 19 - 25 is statistically significant


# b) Is the average purchse made by the men and the women of the age 18 - 25 same ?

# Need to compare the means of two independent groups -> two - sample t-test

from scipy.stats import ttest_ind

# men aged 18 - 25
men = df[(df['Age'] == 1) & (df['Gender'] == 1)]['Purchase']
# women aged 18 - 25
women = df[(df['Age'] == 1) & (df['Gender'] == 0)]['Purchase']


# Two sample t_test
t_stat, p_value = ttest_ind(men,women)
print("Men Averge : ", men.mean())
print("Women Average : ", women.mean())
print("T-stats :",t_stat)
print("p_value :", p_value)


# hypthesis >

#h0 -> Average purchase of men and women are Equal
# h1 -> Average purchase of men and women are not equal


# p_value < 0.05 -> Reject null hypothesis



"""

# Liner algebra
# Matrix ? It is the rectanglular arrangement of anything which is in the form of rows and columns

# Rows = Horizontal line of elements
# Columns - Vertical line of element

# Matrix Dimension - If a Matrix has m rows and the n columns - > dimension = m*m rows * colums



# Order of matrix - > no.of rows * no.of columns

# Matrix Notation ? we should use the capital notation only (A,B,C,D)

# Real wordl examples ->

# 1) Data of the student marks -> student * subject

# 2) Sales data -> product * month * year
# 3) hospital record -> patient * Medical test



# Types of the matrix

# 1) Row matrix -> the matrix which is haiving the row only
# A = [10,20,30,40]

 # Row =1 , columns = 4, order => 1*4

 # Storing the marks of single student

 # 2) Column matrix -> the matrix which is having the column only

 '''
 A =[1
 2
 3
 4]
 No of rows => 4, No of columns = 1, order of the matrix = 4*1
 Store the data of the temperature

 '''

# 3) Rectangular Matrix -> in which the number of rows != number of columns
m != n
ex = student data
roll number, maths , hindi, english

# 4) Square matrix => in which the number of rows = number of columns
# 5) Zero matrix / mull matrix

Example ->  A Classroom where there is no test occured yet

# 6) Identity matrix/ Unit matrix

Every diagonal element is 1
and Rest every element is 0

A, I = A

dot product and the cross product



"""



























































































































































































