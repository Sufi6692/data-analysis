# 1. Import the required packages

# data reading and manipulation packages
import numpy as np
import pandas as pd


# data visualization packages
import matplotlib.pyplot as plt
import seaborn as sns

#machine learning related packages
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score


## 2. Reading and exploring the data

"""
1. Import the dataset
2. Check the shape, info, datatype of the columns.
3. Check for missing values and handle them.
4. Check for duplicates and handle them
5. Do the encoding of the categorical columns.
6. Check for outliers and deal with them
7. Any necessary visualizations.
"""

data = pd.read_csv("Boston.csv")

print(data.head()) #print the top 5 rows of the data for a quick inspection


"""
- CRIM per capita crime rate by town
- ZN proportion of residential land zoned for lots over 25,000 sq.ft.
- INDUS proportion of non-retail business acres per town
- CHAS Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
- NOX nitric oxides concentration (parts per 10 million)
- RM average number of rooms per dwelling
- AGE proportion of owner-occupied units built prior to 1940
- DIS weighted distances to five Boston employment centres
- RAD index of accessibility to radial highways
- TAX full-value property-tax rate per 10,000usd
- PTRATIO pupil-teacher ratio by town
- B 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
- LSTAT % lower status of the population

"""


print(data.shape) #print the total number of rows and columns present in the data
print(data.dtypes)  #print the datatype of values in each column


print(data.isnull().sum())#print the total number of missing values in each column

# Check for duplicates

print(data.duplicated().sum()) #print the number of duplicate row in the data

data.drop_duplicates(inplace = True)  #drop the duplicate rows (if any)

# Check and remove outliers

# function to check outliers and remove them from the given columns

def remove_outliers(data,columns):
    for column in columns:
        if column in data.columns:
            Q1 = data[column].quantile(0.25)
            Q3 = data[column].quantile(0.75)
            IQR = Q3 -Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            data = data[(data[column] >= lower_bound) & (data[column] <= upper_bound)]
    return data

data_without_outlier = remove_outliers(data, data.columns)

print(data.shape) #Original data


print(data_without_outlier.shape) #dataframe without outlier and we lost lot of rows while outlier cleaning
 


"""
There are two ways in which we can deal with outliers:

1. **Outlier Removal (we did this above)**: Means removing the rows which have outliers. The problem with this approach is that we can loose lots of data while doing this.

2. **Data Transformation** : We don't remove the outliers but instead we transform the columns having outliers in such a way that outliers don't behave as outliers.
  - 2.1. Square root transformation.
  - 2.2. Log Transformation.
  - 2.3. Box-Cox Transformation.

"""





"""
### **3. Machine Learning Process**

1. Create X and y variables. Store input columns in X and output column in y.
2. Split the data into training and testing sets.
3. Standardize/Scale the data.
4. Apply the ML Algorithm on the data.
5. Check the performance of the model.
6. Necessary improvements in the model to increase its performance/accuracy.

"""

X = data.drop(columns = 'medv')  # store all the input columns
y = data['medv']  #store the output column

#split the dataset into training and testing data

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=100)


# Apply Liner Regression Algorithm on the training data

lin_reg = LinearRegression()
lin_reg.fit(X_train,y_train)  # training process starts here

print(lin_reg.coef_)  #m1 to m13

print(lin_reg.intercept_ ) # C value

y_pred = lin_reg.predict(X_test)

print(pd.DataFrame({'Actual': y_test, "Predicted": y_pred}))


print(r2_score(y_test, y_pred))


"""
#### **Performance metrics used in Regression**

1. **R2 Score** (also called R_squared).
2. **Adjusted R2 Score**.
3. **Mean Squared Error** (MSE).
4. **Root Mean Squared Error** (RMSE).

"""

print(r2_score(y_test, y_pred))




mse = mean_squared_error(y_test, y_pred)

print(mse)

rmse = np.sqrt(mse) #mse ** 0.5
print(rmse)



### **Checking VIF score for multicollinearity**


from statsmodels.stats.outliers_influence import variance_inflation_factor

vif = pd.DataFrame()
vif['Features'] = X_train.columns
vif['VIF'] = [variance_inflation_factor(X_train.values, i) for i in range(X_train.shape[1])]
vif['VIF'] = round(vif['VIF'], 2)
vif = vif.sort_values(by = "VIF", ascending = False)
vif








































































































