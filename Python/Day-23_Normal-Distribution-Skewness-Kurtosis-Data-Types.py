# Normal distribution

"""
You data is being distributed properly means there is a proper balance between the values

A Normal distribution data will have same value as its Mean, Median and Mode.


"""
import numpy as np
import matplotlib.pyplot as plt
import statistics as stats



data = [15,16,16,17,17,17,18,18,19]
plt.hist(data, bins = 5, edgecolor ="black")
plt.show()

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Mode:", stats.mode(data))



# Skewness

"""
it describes the shapes of data in the form of Right skewed,(+ve) or Left skewed(-ve)

"""


# Right skewed data(+Ve) -Mean the tail of data is going to be on right side 
data=[10,10,10,10,10,11,11,12]
plt.hist(data,bins=3,edgecolor="black")
plt.show()

from scipy.stats import skew
print("Skewness of Right skewed data:",skew(data))



# Left skewed data (-Ve)  - Mean the tail of data is going to be on left side
data=[10,11,11,12,12,12,12,12]
plt.hist(data,bins=3,edgecolor="black")
plt.show()

from scipy.stats import skew
print("Skewness value of this Left/Negatively skewed data is :", skew(data))



# Kurtosis

"""

it describes the shape of data in the form of peakedness (+ve) or tailedness (-ve)

"""

# Peakedness graph ( +ve Kurtosis value )
data=[10,11,11,12,12,12,12,12,12,12,12,12,12,13,13,14]
plt.hist(data,bins=3,edgecolor="black")
plt.show()

from scipy.stats import kurtosis
print("Kurtosis value of this Peaked  data is :", kurtosis(data))




# Tailedness graph ( -ve Kurtosis value )
data=[11,10,13,14,12]
plt.hist(data,bins=5,edgecolor="black")
plt.show()

from scipy.stats import kurtosis
print("Kurtosis value of this Tailed  data is :", kurtosis(data))



"""
# Data types


1) Categorical data / Qualitative data

This type of data will represent categories or qualities and doesn't involve any numbers in a meaningful way

example

["Small-1","Medium-2,"Large-3"]

["Boy","Girl"]

["Yes","No","Maybe"]

["Good","Bad"]

**Types of Categorical data / Qualitative data**

-> Nominal data

-> Ordinal data

-----------------------------------------------------------------------


2) Numerical data / Quantitative data

This type of data will represent numbers in a meaningful way

example

[1,2,3,4,5]

[123124,6356754,3676547478]

[23.4 , 67.6 , 888.77 ]


**Types of Numerical data / Quantitative data**


-> Discrete data

-> Continuous data











"""



























































































































































































































































