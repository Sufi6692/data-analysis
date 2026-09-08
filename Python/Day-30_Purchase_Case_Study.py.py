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
























































































































































































































