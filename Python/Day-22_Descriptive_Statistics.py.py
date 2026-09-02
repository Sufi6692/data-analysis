import numpy as np
import statistics as stats


'''
data_1 = [25,30,35,40,45,55,50,60,65,70]

variance = Sum of squared difference between each data point and mean / Total no of data points - 1
Mean = 47.5

variance = [ (25-47.5)^2 +(30-47.5)^2 +(35-47.5)^2 +(40-47.5)^2 +(45-47.5)^2 +(55-47.5)^2 +(50-47.5)^2 +(60-47.5)^2 +(65-47.5)^2 +(70-47.5)^2 ] / 9
variance = [ -22.5^2 + -17.5^2 +  -12.5^2 + -7.5^2 + -2.5^2 + 7.5^2 + 2.5^2 + 12.5^2 + 17.5^2 + 22.5^2 ] / 9
variance = 229.16

'''
# Numpy will calculate your Population variance
# variance = Sum of squared difference between each data point and mean / Total no of data points
data_var = [25,30,35,40,45,55,50,60,65,70]
print("Variance of this data by using numpy is :", np.var(data_var))

# Stats will calculate your Sample variance
# variance = Sum of squared difference between each data point and mean / Total no of data points - 1
data_var = [25,30,35,40,45,55,50,60,65,70]
print("Variance of this data  by using stats is :", stats.variance(data_var))

# Population - Full data
# Sample - A part of that full data


# Standard Deviation

"""
It indicates how much a individual data point deviates from the mean 

In simple words = it means on a average how much these individual data points are far away from the mean value

Standard Deviation = Square root of variance

"""
print("Variance of this data  by using stats is :", stats.variance(data_var))
print("Standard deviation of this data by using stats is :" , np.sqrt(stats.variance(data_var)))
print("Standard Deviation of this data by using numpy is :", np.std(data_var))
print("Standard Deviation of this data by using stats is :", stats.stdev(data_var))


# Percentage 

# A percentage is an absolute measure of a value out of 100

"""
'''
A school child - Rohan got 58 percent marks
This means Rohan got 58/100
'''
"""


# Percentile

# While a percentile is a relative rank comparing your score against a larger group 


"""

'''
A Jee Mains exam was there - Rohan got 99 percentile
So this means whatever marks Rohan got ( let it be 300/320 or 250/320 or any marks ) those marks are more than 99% of all students who attended the exam and got the marks
'''

"""

data = [ 1,5,2,10,45,67,33,29,19,61,54,45,12,9]

# Calculating 90 percentile of this data

print("90 percentile of this data is :", np.percentile(data, 90))


"""

'''
data = [ 1,5,2,10,45,67,33,29,19,61,54,45,12,9]
data = [1,2,5,9,10,12,19,29,33,45,45,54,61,67]   # same data after sorting
so we got 90 percentile as 58.90
this means 90% of values in my data is less than 58.90
'''

'''

Children have chocolates
data=[Priya:5 , Rahul:10 , Aman:20 , Alice:19 , Bob:25 , Chris:29]
so let say Bob got 90 percentile that means whatever chococlates bob got that no is still more the 90% of other child chococlate no
'''

"""




# Correlation 

# The relationship between 2 values / data /columns 

"""
For Example -:

Temperature and Ice cream sales

if temp will increase = ice cream sales will also increase 
if temp will decrease = ice cream sales will also decrease 


"""

"""

For Example -:


Speed and time to reach the destination 

if speed will increase = The time taken to reach the destination will decrease 

If speed will decrease = The time taken to reach the destination will increase

"""


# Types of correlation


""" 

# Positive correlation -: If x will increase , Y will also increase or If x will  Decrease, Y will also Decrease (They are moving in same direction )

# Negative Correlation -: If x will increase , Y will Decrease or If x will  Decrease, Y will Increase (They are moving in opposite direction )

# No correlation -: If x will increase or decrease , Y will not change (They are moving in no direction )
                    No relationship between x and y and they are independent of each other

"""

import pandas as pd

df = pd.read_csv("Housing.csv")
print(df)

# As Correlation we can only calculate with numerical values so lets filter out numerical data first from the our data 
new_data  = df.select_dtypes(include = np.number)
print(new_data)

new_data.corr() # It will give the correlation between all numerical columns in our data


# Covariance

# It will provide the actual values like if X will increase how much Y will increase of decrease and if X will decrease how much Y will increase or decrease


new_data.cov() # It will give the covariance between all numerical columns in our data 































































































































































































































































