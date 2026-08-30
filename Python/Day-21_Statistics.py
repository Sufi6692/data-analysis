"""

# Statistic



# 1) Descriptive Statistics

It will have your core mathematical functions for data analysis



1-> Measure of Central Tendancy ( To find the centre of your data )

Mean

Mode

Median


2-> Measure of Dispersion  ( To calculate the spread of data )

Range

Variance

Standards deviation

Percentage

Percentile

Quartile

Outliers

Correlation

Covariance

Skewness

Kurtosis

Normal distribution




# 2) Inferential statistic

It will have hypothesis and all

Null Hypothesis

Alternate Hypothesis


----------------------------------------------------------------------

# Probability

Marginal Probability

Conditional Probability




"""


# Measure of Central Tendancy ( To find the centre of your data )


## Mean

#Average of your data


"""
'''
data = [500,750,1200,2500,1150,5600,4120]
Average / Mean = (Sum of all values) / Total no of value
Average / Mean = 15820 / 7
Average / Mean = 2260
'''
"""

import numpy as np
data =[500,750,1200,2500,1150,5600,4120]
ans = np.mean(data)
print(ans)



import statistics as stats
data = [500,750,1200,2500,1150,5600,4120]
ans = stats.mean(data)
print(ans)



# Median

#Middle value of your data

"""
'''
data = [ 5,11,12,2,3,6,7,9 ]

First sort your data ( Ascending or Descending )
Second check do you have EVEN no of values or ODD no of values in your data

We have 8 value so we will apply the EVEN formula

data = [ 5,11,12,2,3,6,7,9 ]
sorted_data = [ 2,3,5,6,7,9,11,12]
Median = Sum of middle 2 values / 2
Median = 6+7 /2
Median = 13/2
Median = 6.5
'''


"""


data = [ 5,11,12,2,3,6,7,9 ]
ans = np.median(data)
print(ans)

data = [ 5,11,12,2,3,6,7,9 ]
ans = stats.median(data)
print(ans)

"""
'''
data = [ 5,2,7,8,5,9,1,3,5 ]

First sort your data ( Ascending or Descending )
Second check do you have EVEN no of values or ODD no of values in your data

We have 9 value so we will apply the ODD formula

data = [ 5,2,7,8,5,9,1,3,5 ]
sorted_data = [ 1,2,3,5,5,5,7,8,9]

Median = n+1 / 2 position
Median = 10/2 position
Median = 5th position
Median = 5
'''


"""

data = [ 5,2,7,8,5,9,1,3,5 ]
ans = np.median(data)
print(ans)




data = [ 5,2,7,8,5,9,1,3,5 ]
ans = stats.median(data)
print(ans)



# Mode
"""
Most common value /Most frequent value/ Most repeated value/ The value having highest frequency 

"""

'''
data = [ 1,4,11,12,23,23,56,23,78,1,1,4,11,23,11,19]

We need to calculate the frequency of each value
1= 3 times
4= 2 times
11= 3 times
12= 1 times
19= 1 times
23= 4 times
56= 1 times
78= 1 times

so 23 is being repeated most no of times so 23 is the mode of this data

'''

data = [ 1,4,11,12,23,23,56,23,78,1,1,4,11,23,11,19]
ans = stats.mode(data)  #Numpy don't have mode only stats library you can use 
print(ans)

"""


'''
data = [ 1,4,11,12,11,23,23,56,23,78,1,1,4,11,23,11,19]

We need to calculate the frequency of each value
1= 3 times
4= 2 times
11= 4 times
12= 1 times
19= 1 times
23= 4 times
56= 1 times
78= 1 times

NOW MORE THAN 1 VALUE IS BEING REPATED SAME NO OF TIME / MORE THEN 1 VALUE IS HAVING SAME HIGHEST FREQUENCY

Are we going to have multimode ( Means 11 and 23 both are going to be the mode )   ?
Are we going to have only 1 mode by using some logic or approach   ?


1st group of Mathemticians - We can have multimode

2nd group of Mathemticians - We will only have 1 mode so if more than 1 value is having same highest frequency then the value that will come first
                             in my data is going to be the mode so if this is the data [ 1,4,11,12,11,23,23,56,23,78,1,1,4,11,23,11,19]
                             11 is coming 4 times
                             23 is also coming 4 times
                             so 11 is going to be the Mode
'''
"""

data = [ 1,4,11,12,11,23,23,56,23,78,1,1,4,11,23,11,19]
ans = stats.mode(data)
print(ans)


data = [ 1,4,23,12,11,11,23,56,23,78,1,1,4,11,23,11,19]
ans = stats.mode(data)
print(ans)

data = [11,10,1,2,3,4,5,6,7,8,9]
ans = stats.mode(data)
print(ans)


# How to find multimode

data = [1,4,11,12,11,23,23,56,23,78,1,1,4,11,23,11,19]
ans = stats.multimode(data)
print(ans)


# FAQ - How to sort the data in python 

# Ascending order

data = [4,8,87,567,986,26,99,76,567,999 , 56.09 , 4.5]
data.sort()
print(data)



# Descending order
# Descending order
data = [4,8,87,567,986,26,99,76,567,999 , 56.09 , 4.5]
data.sort(reverse=True)
print(data)





# Measure of Dispersion 

# The operation that will give us the idea about the spread of our data


# Rang

# Just the difference between the highest values and lowest value of your data

'''
salary_data = [ 25000 , 47000 , 84000 , 251000 , 421500 , 30000 , 10000]

highest_value = 421500
lowest_value =  10000

Range = highest_value - lowest_value
Range = 421500 - 10000
Range = 411500
'''
salary_data = [ 25000 , 47000 , 84000 , 251000 , 421500 , 30000 , 10000]

ans = np.ptp(salary_data) # Use .ptp for finding range

print(ans)


"""
# Variance

**It quantifies the spread of data around the mean**


In simple words variance will help me to get the idea that values in my data is close to each other or values in my data are far away from each other



"""


data_1 = [1,5,12,7,3,19,18,11,16,6,0.5,10.5,17.2]    #1st type of data in which values are close to each other      - Data with low variance
data_2 = [1 , 100 , 550.5 , 158 , 333 , 97539 , 45]  #2nd type of data in which values are far away from each other - Data with high variance

print("Variance of data 1 is  :", np.var(data_1))
print("Variance of data 2 is  :", np.var(data_2))


"""
data_1 = [25,30,35,40,45,55,50,60,65,70]

variance = Sum of squared difference between each data point and mean / Total no of data points - 1
"""






























































