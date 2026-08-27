# Histogram
# It is used to compare continuous data/value to show the data distribution

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
age=[34,45,1,2,4,55,56,57,78,99,22,26,28,25,14,69,76,81,79,18,87,92,101,72,83]
plt.hist(age)
plt.show()



age=[34,45,1,2,4,55,56,57,78,99,22,26,28,25,14,69,76,81,79,18,87,92,101,72,83]
plt.hist(age, color="red", bins =3, edgecolor="black")  #Bins = is used to control the no of categories

plt.grid(True)
plt.title(" Histogram to show the age distribution ")
plt.xlabel(" Age Group ")
plt.ylabel(" Count of people of specific age groups ")
plt.show()


# Assign different different color to each of 3 age group
age=[34,45,1,2,4,55,56,57,78,99,22,26,28,25,14,69,76,81,79,18,87,92,101,72,83]

# creating histogram
counts, bins, patches = plt.hist(age, bins = 3, edgecolor ="black")

#Assign different color to each bin

color = ["green", "blue", "red"]



for patch , color in zip(patches , color):
    patch.set_facecolor(color)


plt.title(" Histogram to show the age distribution ")
plt.xlabel(" Age group ")
plt.ylabel("Count of people of specific age groups ")
plt.grid(True)
plt.show()


# Area plot

# It is used to show the data distribution and at the same time we can compare multiple data at once 

category =["Jan","Feb","Mar","Apr"]

apple = [10,20,12,14]
banana = [15,25,8,18]

plt.fill_between(category, apple, color="red", label="Sale of apples", alpha =0.2)
plt.fill_between(category,banana, color="yellow", label="Sale of Bananas", alpha=0.2)


plt.legend()
plt.grid(True)
plt.show()



# Box plot
# To show the data distribution as well as to detect the  in my data

age_data=[10,15,45,-989, 36,98,81,68,75,79,91,5,9,19, 451 ,28]

"""
Mean = (Sum of all values / Total no of value)
Mean = 121/16
Mean - 7.5625

"""
# Find the average age of people

print(" Average age of people is : ", np.mean(age_data))



age_data=[10,15,45, 36,98,81,68,75,79,91,5,9,19 ,28]

# Find the average age of people
print("Average age of people is :", np.mean(age_data))


age_data=[10,15,45, 36,98,81,68,75,79,91,5,9,19,28]
sns.boxplot(age_data)
plt.show()


# How to detect outliers are present in our data or not 

age=[10,15,45,36,98,81,68,75,79,91,5,9,19,-989 , -765, 36,98,36,98,81,68,75,79,91,5,9,19,81,68,75,79,91,5,9,19,36,98,81,68,75,79,91,5,9,19, 451 ,28]

sns.boxplot(age)
plt.show()



# How to detect outliers are present in our data or not

age=[5,50,1,10,35,26,99,97,250,87,73,93,71,81,65,-190,57,50,16]

Q1 = np.percentile(age,25)
Q3 = np.percentile(age,75)
IQR = Q3-Q1

lower_limit = Q1-1.5*IQR
upper_limit = Q3+1.5*IQR

print(lower_limit)
print(upper_limit)

print("If any data point is less than lower_limit or if any data point is more than upper_limit - It is a outlier")

for i in age:
    if i<lower_limit or i>upper_limit:
        print(i , " : The value is a outlier")
        age.remove(i)

print("Final clean age data", age)



# Violin plot

age=[10,15,45,36,98,81,68,75,79,91,5,9,19,-989 , -765, 36,98,36,98,81,68,75,79,91,5,9,19,81,68,75,79,91,5,9,19,36,98,81,68,75,79,91,5,9,19, 451 ,28]

sns.violinplot(age)
plt.show()




age_data=[10,15,45, 36,98,81,68,75,79,91,5,9,19,28]
sns.violinplot(age_data)
plt.show()


#Heat Map

data=[[1,2,3],[4,5,6],[7,8,9]]
sns.heatmap(data, annot=True)

plt.show()




data=[[1,2,3],[4,5,6],[7,8,9]]
sns.heatmap(data, annot=True , cmap="plasma")

plt.show()






data=[[1,2,3],[4,5,6],[7,8,9]]
sns.heatmap(data, annot=True , cmap="coolwarm")

plt.show()








