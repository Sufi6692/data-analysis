import numpy as np


# Nominal data


"""
This is a data that can be categorized but has no specific order
Example = [Yes, No]

Example = [Apple, Banana, Cherry]

"""

# Ordinal data


"""
This is a data that can be categorized and also follows a specific order
Example = [Low, Medium, High]

Example = [Bad, Average, Good, Excellent]



"""

# Discrete data

"""
This type of data can only take specific numerical values (Whole numbers)

Example = [1 student, 2 students, 3 students]

Example = [ 4 Apples, 10 Banana]




"""




# Continuous data 


"""
This type of data can take any value including decimals/float

Example = [45.2 Kg, 30Kg, 46.1 Kg]

"""

# Probability Basics

"""
It is a measure of how likely an event is going to occur.

 # Experiment
 
 Any process or any task

 Like rolling a dice, flipping a coin, Drawing a card from the deck

 #Event

 It is a specific or group of results that comes from a experiment

 Example = If you will flip a coin there is only going to be 1 result - either Head or Tail 


  # Types of event

  1. Simple event = 1 specific outcome / result

  Example = Rolling 1 dice ( will give me only 1 result means any 1 number will come out of 6 numbers)

  2. Compound event = 2 or more specific outcomes / results

  Example = Rolling 2 dice ( 2 number will come 1,1 2, 1 3, 1 4, 1 5, 6, 1.... 66)

"""

# Probability = No of Favourable 
# outcomes / Total no of outcomes



'''
1st Example = You are flipping a coin , what is the probability of getting a Head

Probability = 1 / 2
Probability = 0.5 or 50%


2nd Example = We are rolling a dice , what is the probability of getting a even number

No of favourable outcomes = 3 (2,4,6)
Total no of outcomes = 6 (1,2,3,4,5,6)
Probability = No of favourable outcomes / Total no of outcomes
Probability = 3 / 6
Probability = 0.5 or 50%

3rd Example = We are taking out a card from a deck of cards , what is the probability it is going to be a face card

No of favourable outcomes = 12 face card
Total no of outcomes = 52
Probability = No of favourable outcomes / Total no of outcomes
Probability = 12/52
Probability = 0.23 or 23%

4th Example = You are rolling 2 dice , what is the probability of getting same no on both dice

No of favourable outcomes = 6
Total no of outcomes = 36
Probability = No of favourable outcomes / Total no of outcomes
Probability = 6/36
Probability = 0.17 or 17%

5th Example = You are rolling 2 dice , what is the probability of getting both numbers sum less than 5 ( less than 5 , not even equal to )

No of favourable outcomes = 6
Total no of outcomes = 36
Probability = No of favourable outcomes / Total no of outcomes
Probability = 6/36
Probability = 0.17 or 17%

6th Example = I am taking our 2 cards from a deck what are the changes of those 2 cards being of same color

No of favourable outcomes =
Total no of outcomes =
Probability = No of favourable outcomes / Total no of outcomes
Probability =
Probability =
'''


# Types of Probability 

# 1. Marginal Probability 
# 2. Joint Probability
# 3. Conditional Probability

"""
1. Marginal Probability

It is a probability of a single event happening without considering any other event

Example = You are having a bag full of balls ( 5 red balls , 6 black balls , 4 blue balls )

If i want to take out 1 balls , what is going to be the probability of its being red

Probability = 5/15

Probability = 0.333 or 33%

"""


"""

2) Joint probability

It is a probability of two or more than two event happening at the same time

Example = Rolling 2 dice at the same time and what is going to be the probability of both dice showing 3

Probability = 1/36
Probability = 0.027


"""




"""

**3) Conditional probability**

It is the probability of a event happening given that another event already happened

Example = Suppose you have a drawn a card from a deck and it was a face card , what is the probability that face to be a king

No of favourable outcomes = 4 king

Total no of outcomes = 12 cards

Probability = No of favourable outcomes / Total no of outcomes

Probability = 4/12

Probability = 0.33 or 33%

"""




import pandas as pd
data = pd.read_csv("country_profile_variables.csv")
print(data)

print(data.to_string()) # To print the full data


# I want to find the average population or world in 2017

print(data["Population in thousands (2017)"].mean())

# print(np.mean(data(["Population in thousands (2017)"])))

# Find in which region most of the countries are present
print(data["Region"].mode())

# Which country is having the highest population density per Km2

# Step 1 - Find the highest value in population density column
print(data["Population density (per km2, 2017)"].max())

#step 2 - Find the country having that values
print(data[data["Population density (per km2, 2017)"]==25969.8])


# Which country have the lowest sex ration



column = "Sex ratio (m per 100 f, 2017)"

sex_ratio = data[column].replace(-99, np.nan)
lowest_ratio = sex_ratio.min()

print(data.loc[sex_ratio == lowest_ratio, ["country", column]])


# In 2017 find top 5 countries with highest population

population_column = "Population in thousands (2017)"

sorted_data = data.sort_values(
    by=population_column,
    ascending=False
)

top_5 = sorted_data.head(5)

print(top_5[["country", population_column]])


# Country with the lowest mobile-cellular users

mobile_column = "Mobile-cellular subscriptions (per 100 inhabitants)"

mobile_users = pd.to_numeric(
    data[mobile_column],
    errors="coerce"
).replace(-99, np.nan)

lowest_mobile_index = mobile_users.idxmin()

print(data.loc[
    lowest_mobile_index,
    ["country", mobile_column]
])



# Countries with the highest and lowest CO2 emissions

co2_column = "CO2 emission estimates (million tons/tons per capita)"

co2 = pd.to_numeric(
    data[co2_column],
    errors="coerce"
).replace(-99, np.nan)

lowest_co2_index = co2.idxmin()
highest_co2_index = co2.idxmax()

print("Lowest CO2 emission:")
print(data.loc[lowest_co2_index, ["country", co2_column]])

print("Highest CO2 emission:")
print(data.loc[highest_co2_index, ["country", co2_column]])



# Which country was having the highest forest covered area


forest_column = "Forested area (% of land area)"

forest_area = pd.to_numeric(
    data[forest_column].astype(str).str.split("/").str[0],
    errors="coerce"
).replace(-99, np.nan)

highest_forest_index = forest_area.idxmax()

print(data.loc[
    highest_forest_index,
    ["country", forest_column]
])

















































































































































