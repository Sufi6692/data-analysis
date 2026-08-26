#Visualization library
import matplotlib.pyplot as plt
import seaborn as sns

"""
Different types of chats

1. Bar chart
2. Line plot
3. Pie chart
4. Scatter plot
5. Histogram plot
6. Box plot
7. Area plot
8. Heat map etc etc


"""

## Bar plot

# When you need to compare multiple values at once 

days = ["Monday","Tuesday","Wednesday","Thursday","Friday"]  #Data for X axis
sales_amount = [1200, 600, 1200, 780, 1400] # Data for y axis


plt.bar(days, sales_amount)
plt.show() # To display the bar chart in the output box


day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"] #Data for x axis
sales_amount = [1200, 600, 1200, 780, 1400] # Data for y axis

plt.bar(days,sales_amount)

plt.title(" Bar chart to compare the sales amount of our store during weekdays" ) # To add a title to this plot
plt.xlabel("Days") # To write something on x axis
plt.ylabel("Sales Amount") # To write something on y axis

plt.show() # To display the bar chart in the output box



days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
sales_amount = [1200, 600, 1200, 780, 1400]

plt.barh(days , sales_amount , color="red")   # plt.barh To draw horizontal bar chart  , color= To change the color of plot

plt.title(" Bar chart to compare the sales amount of our store during weekdays" )
plt.xlabel("Days")
plt.ylabel("Sales Amount")

plt.show()


days = ["Monday" ,"Tuesday" ,"Wednesday" ,"Thursday" ,"Friday"]
sales_amount = [1200 , 600 , 1200 , 780 , 1400]

plt.bar(days , sales_amount , color=["red" ,"pink" ,"green" ,"purple" ,"#ff1500"])
plt.title(" Bar chart to compare the sales amount of our store during weekdays" )
# Change font size shape and format
plt.xlabel("Days" , fontsize=15 , fontweight="bold")
plt.ylabel("Sales Amount" , color="Red")

plt.grid(True)  # To draw the grid lines

plt.show()



# Stacked bar chart

categories=["A",'B',"C"]
value_1 = [10,20,30]
value_2 = [5,15,20]

plt.bar(categories , value_1 , label="Bar 1")
plt.bar(categories , value_2 , label="Bar 2")

plt.title("Stacked bar plot")
plt.legend()
plt.show()



# Side by Side bar chart
import numpy as np

days=["Mon","Tue","Wed"]

male=[10,14,12]
female=[23,45,19]

x=np.arange(len(days))

plt.bar( x - 0.25/2  , male , 0.25 , label="male")
plt.bar( x + 0.25/2 , female , 0.25 , label="female")

plt.legend()
plt.show()


year=["2010" ,"2015" ,"2020" ,"2025" ]
profit=[1000 , 5000 , 3000 , 8000]

plt.plot( year , profit)
plt.show()


year=["2010" ,"2015" ,"2020" ,"2025" ]
profit=[1000 , 5000 , 3000 , 8000]

plt.plot( year , profit , marker="o")
plt.show()




from matplotlib.lines import lineStyles
year=["2010" ,"2015" ,"2020" ,"2025" ]
profit=[1000 , 5000 , 3000 , 8000]

plt.plot( year , profit , marker="^" , color="red" , linestyle="dashed")

plt.title ("Dashed line plot with red color and triangle marker to compare the sales of our company")
plt.xlabel(" Year ")
plt.ylabel (" Profit")
plt.show()





# Draw a line plot with 2 lines to compare multiple company data at once

Year = ["2000" ,"2005" ,"2010" ,"2015" ,"2020" ,"2025"]  # For X axis

Google_profit = [1000 ,2000 ,1500 ,1700, 2600 , 3000]  # For Y axis
Meta_profit = [2000 ,1500 ,1800 ,2700, 3400 , 2000]    # For Y axis


plt.plot( Year , Google_profit , marker="^" , color="red" , label="Google Profit")
plt.plot( Year , Meta_profit , marker="o" , color="blue" , label="Meta Profit")

plt.legend()  # To display the labels of lines , label="Google Profit" , label="Meta Profit"

plt.grid(True)
plt.show()


import matplotlib.pyplot as plt

x = ["Monday","Tuesday","Wednesday"]
y = [10,15,8]

plt.plot(x,y,marker ="o")

for i , value in enumerate(y):
    plt.text(x[i], y[i], str(value), ha="center", va ="bottom")
plt.show()


category=["0-17" ,"18-25" ,"26-50" ,"51-75" ,"76-100+"]
values=[15,35,20,20,10]

plt.pie(values , labels=category)

plt.title("Population age wise distribution")
plt.show()




category=["0-17" ,"18-25" ,"26-50" ,"51-75" ,"76-100+"]
values=[15,35,20,20,10]

plt.pie(values , labels=category , autopct="%0.0f%%")  # autopct="%0.0f%%" upto 0 decimal place

plt.title("Population age wise distribution")
plt.show()






category=["0-17" ,"18-25" ,"26-50" ,"51-75" ,"76-100+"]
values=[15,35,20,20,10]

plt.pie(values , labels=category , autopct="%0.2f%%")  # "%0.2f%%" upto 2 decimal place

plt.title("Population age wise distribution")
plt.show()







category=["0-17" ,"18-25" ,"26-50" ,"51-75" ,"76-100+"]
values=[15,35,20,20,10]

plt.pie(values , labels=category , autopct="%0.0f%%" , explode=[0,0, 0.25 ,0, 0])

plt.title("Population age wise distribution")
plt.show()





category=["0-17" ,"18-25" ,"26-50" ,"51-75" ,"76-100+"]
values=[15,35,20,20,10]

plt.pie(values , labels=category , autopct="%0.0f%%" , explode=[0,0, 0.25 ,0,0] , shadow=True)

plt.title("Population age wise distribution")
plt.show()





age=[10,20,30,40,50,60,70,80,90,100]
weight=[15,50,55,61,75,84,66,88,87,59]

plt.scatter( age , weight)

plt.grid(True)
plt.show()








age=[10,20,30,40,50,60,70,80,90,100]
weight=[15,50,55,61,75,84,66,88,87,59]

plt.scatter( age , weight , color="red" , marker="*" , s=200)

plt.grid(True)
plt.show()







age=[10,20,30,40,50,60,70,80,90,100]

weight=[15,50,55,61,75,84,66,88,87,59]
height=[12,56,78,45,79,56,89,98,123,100]

plt.scatter( age , weight , color="red" , marker="*" , s=200 , label="Weight")
plt.scatter( age , height , color="green" , marker="^" , s=300 , label="height")

plt.grid(True)
plt.legend()
plt.show()








age=[10,20,30,40,50,60,70,80,90,100]

weight=[15,50,55,61,75,84,66,88,87,59]
height=[12,56,78,45,79,56,89,98,123,100]

plt.scatter( age , weight , color="red" , marker="*" , s=200 , label="Weight")
plt.scatter( age , height , color="green" , marker="^" , s=300 , label="height")

plt.grid(True)
plt.legend(loc="lower right" , title="Legend table" , fontsize=12)
'''
loc; supported values are 'best', 'upper right', 'upper left', 'lower left', 'lower right', 'right', 'center left',
'center right', 'lower center', 'upper center', 'center'
'''
plt.show()















