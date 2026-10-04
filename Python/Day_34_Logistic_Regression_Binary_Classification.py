# LogisticRegression model implementation in Python

# Problem Statement:

# The person had taken the fixed deposit/term deposit or not? The person will subscribe or not?

# Yes / No

# Import The Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# you can import this way also 
# from google.colab import files
# uploaded = files.upload()


df = pd.read_csv('bank-additional-full-1.csv', delimiter=';')

# separate the independent and dependent variables ==>sep
# delimiter is used to separate the columns in the dataset==> delimiter

print(df.head())

print(df.info())

"""
Each column description

age--	Customer age

job--	Type of job/occupation

marital--	Marital status

education--	Education level

default--	Has credit in default or not

housing--	Has housing loan or not

loan--	Has personal loan or not

contact--	Type of communication used

month--	Month of last contact

day_of_week--	Day of week of last contact

duration--	Duration of last contact, in seconds

campaign--	Number of contacts during current campaign

pdays--	Days since previous campaign contact (999 = not previously contacted)

previous--	Number of contacts before current campaign

poutcome--	Outcome of previous marketing campaign

emp.var.rate--	Employment variation rate

cons.price.idx--	Consumer price index

cons.conf.idx--	Consumer confidence index

euribor3m--	3-month Euribor interest rate

nr.employed--	Number of employees/economic employment indicator

y	Target-- whether customer subscribed to term deposit (yes/no)

"""



# Logistic Regression  ---> Classify yes or no
# Binary classification 

# EDA -(exploratory Data Analysis) - Understanding the data

"""

- Null values
- Duplicates
- Outliers
- Encoding


"""

#EDA - identifies/reads/finds/understands
#data preprocessing - cleans/drops/duplicates/outliers


#Null values
#null value < 30% --- drop it ---> this the threshold 
#100 -30 --> we have to be very careful

print(df.isnull().sum())

print(df.isnull().sum().sum())

# we can drop it -- Yes we can drop it here

print(df.columns)

for i in df.columns:
  if(df[i].dtype=='str'):
    df[i]=df[i].fillna(df[i].mode()[0])
  else:
    df[i]=df[i].fillna(df[i].mean())

print(df.isnull().sum())

print(df.isnull().sum().sum())

print(df.shape)


# duplicates
print(df.duplicated().sum())


df.drop_duplicates(inplace=True)


print(df.duplicated().sum())


print(df.columns)

df.info()


for i in df.columns:
   if(df[i].dtype!='str'):
     plt.boxplot(df[i])
     plt.title(i)
     plt.show()



# remove it outliers

print(df['pdays'].value_counts())


print(df['previous'].value_counts())

outliers=['duration','campaign','cons.conf.idx']


# remove outliers

for i in outliers:

  q1=df[i].quantile(0.25)
  q3=df[i].quantile(0.75)
  IQR=q3-q1
  lb =q1-1.5*IQR
  ub =q3+1.5*IQR
  df=df[(df[i]>=lb) &(df[i]<=ub)]


for i in outliers:
  plt.boxplot(df[i])
  plt.title(i)
  plt.show()


print(df.shape)


# encoding ---> categorical to numerical

from sklearn.preprocessing import LabelEncoder

print(df.info())

le=LabelEncoder()
for i in df.columns:
  if(df[i].dtype=='str'):
    df[i]=le.fit_transform(df[i])

    print(df.info())


# Model Building

"""
# importing lib necessary for model building
# splitting the data into train and test(x,y)
# split the data into train and test
#training 
#test
#evaluate the model

"""

print(df)


# 1 spliting the data
# x and y

x = df.drop(columns='y')
y = df['y']

print(x)

print(y)



# splitting into train and testing 

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)


print('x-train',x_train)
print('x-test',x_test)

print('y-train',y_train)
print('y-test',y_test)

print('x-train shape',x_train.shape)
print('y-train shape',y_train.shape)
print('x-test shape',x_test.shape)
print('y-test shape',y_test.shape)


# 3 training 

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(x_train,y_train)

yp=model.predict(x_test)

print('yp',yp)

# 5 evaluate the model

from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

print('Accuracy:', accuracy_score(y_test, yp))
print('Confusion Matrix:')
print(confusion_matrix(y_test, yp))
print('Classification Report:')
print(classification_report(y_test, yp))



#precision-->how many times the instances predicted as positive was actually positive
#predicted positive-->actually positive

#tn-6382-actual :-ve predicted: -ve
#fp-117 actua: -ve predicted: +ve
#fn-363 actual :+ve predicted:-ve
#tp-248 actual: +ve , predicted : +ve


#class 0: tn
#actual:
#pe: tn and fn
#tn/tn+fn


6382/(6382+363)


#class 1:
#pre: fp,tp
#actual:tp
#tp/fp+tp

#tn-6382-actual :-ve predicted: -ve
#fp-117 actua: -ve predicted: +ve
#fn-363 actual :+ve predicted:-ve
#tp-248 actual: +ve , predicted : +ve




248/(248+117)




#recall--->how many tmes out of all actual positives did the model get it right
#real positive-->predicted right






#tn-6382-actual :-ve predicted: -ve
#fp-117 actua: -ve predicted: +ve
#fn-363 actual :+ve predicted:-ve
#tp-248 actual: +ve , predicted : +ve


#class 0:
#u got it right-tn
#actual -ve -tn+fp


6382/(6382+117)





#class 1
#we got-tp
#actual-tp,fn
#tp/tp+fn





248/(248+363)





#f1 score-->harmonic mean of recall an precision



#f1=2*(p*r)/(p+r)




print(classification_report(y_test,yp))



#class 0
2*(0.95*0.98)/(0.95+0.98)


#class 1
2*(0.68*0.41)/(0.68+0.41)


























































