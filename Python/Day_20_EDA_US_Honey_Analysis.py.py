import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("US_honey_dataset.csv")
print(df)


# Remove the extra Unnamed: 0 column
df=df.drop(["Unnamed: 0"], axis=1)
print(df)



df.head(50)

"""
# EDA - Exploratory Data Analysis

Explore your data before performing any analysis so if some issue are there in your data,Resolve it

"""

# Check for missing values in your data

print(df.isnull().sum())



df.isna().sum()  #.sum() to get the final count of null values inour data rather than manually calcualting wr will use .sum()

# Check for duplicate data
print(df.duplicated().sum())



# Check the data type of columns
df.info()  # It will provide a summary stats report



"""
#Data Analysis 

Which states are Rarely contributing to honey production for the last 27 years?




In simple word find out that which state have produced honey for how many years form
1995 to 2021 and then check which state have produced honey for the least no of years


"""

print(df["state"].value_counts())




"""
# Conclusion

SouthCarolina	= 12

Maryland	= 9

Oklahoma	 = 9

Least times Honey producing states in US from 1995 to 2021

"""




"""
# Which are the top 5 Honey producing states in the US ?

You need to find from 1995 to 2021 which state have produced the highest amount of honey by using "production" column



"""


ans = df.groupby("state").sum()
print(ans)


ans = df.groupby("state").sum().sort_values("production",ascending=False).reset_index()
print(ans[["state","production"]])



#Increase the size of plot

plt.figure(figsize =(20,10))

sns.barplot(x=ans["state"],y=ans["production"])

#To rotate the name of state by 90 degree to avoid overlapping
plt.xticks(rotation =90)

plt.show()



"""
# Conclusion

NorthDakota	,C alifornia ,SouthDakota	, Florida	, Montana	 are the top 5 honey producing states

"""



"""
# What is the Change in mean Average price of Honey from 1995 to 2021?

Hint - Find the average price of honey of all states in 1995 then for 2021 and then see the difference


"""

new_df =df.groupby("year").mean("average_price").reset_index()
print(new_df[["year","average_price"]])


print(new_df [(new_df["year"]==1995) | (new_df["year"]==2021)] )  # | means or


"""
# Conclusion

Year     Average Price

1995	 , 74.840909

2021	,  3.334250

"""

# Which was the year when production of Honey in wholeUS was the highest?

df5= df.groupby("year").sum().sort_values("production",ascending=False).reset_index()
print(df5 [["year","production"]])


"""

# Conclusion

In year 2000 the honey production was highest in US with - 220320000

"""



"""

# From the above inference we get the production was highest in the year 2000, now let infer which state was having highest contribution in that year

in simple words - we know that in year 2000 production was highest , now please find which state was having the highest contribution in the proudction in 2000




"""


# Fetch data where year==2000 then find our which state is having highest production
# data = df[(df["year"]==2000 )]




data = df[ (df["year"]==2000 ) ]
ans = data.sort_values("production", ascending=False)
print(ans)


"""

# Conclusion -

NorthDakota is the state having highest production in year 2000


"""

"""

# Which states have the highest no. of colonies in the year 2000?
"""

data = df[ (df["year"]==2000 ) ]
ans = data.sort_values("colonies_number", ascending=False)
print(ans)


"""
# Conclusion

California is the state with highest no of colonies in year 2000

"""



















