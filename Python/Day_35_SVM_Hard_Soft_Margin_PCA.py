import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

X1 = np.array([
    [2,2],
    [2,3],
    [3,2],
    [3,3],
    [7,7],
    [7,8],
    [8,7],
    [8,8],


])

y = np.array([
    0,0,0,0,
    1,1,1,1
])




from sklearn.svm import SVC
model = SVC(kernel ='linear', C=100000) ## Hard margin -> I want correctly classified points
model.fit(X1,y)

print('Support Vectors')
print(model.support_vectors_) ## The points which are closest to my decision boundary


w = model.coef_[0]
b = model.intercept_[0]

print('w = ',w)
print('b = ',b)

## Visualizing
plt.figure(figsize=(10,8))

plt.scatter(
    X1[:,0],        #Class A values
    X1[:,1],        #Class B values
    c=y,            # Means the color of each point is determined by the class label
    s=100
)

plt.scatter(
    model.support_vectors_[:,0],
    model.support_vectors_[:,1],
    s = 200,
    edgecolors='black',
    label = 'Support Vectors'
)


## Draw decision boundary and margins

X_range = np.linspace(1,9,100)
w1 = w[0]
w2 = w[1]


decision_boundary = -(w1 * X_range + b)/w2

margin = 1 /np.sqrt(w1**2 + w2**2)

upper_margin = decision_boundary + margin
lower_margin = decision_boundary - margin

## Soft margin
X = np.array([
    [2,2],
    [2,3],
    [3,2],
    [3,3],
    [7,7],
    [7,8],
    [8,7],
    [8,8],

    [6,6]  ## misclassified point
])

y = np.array([
    0,0,0,0,
    1,1,1,1,
    0
])


model = SVC(kernel = 'linear', C=1)
model.fit(X,y)


# Visualizing 
plt.figure(figsize = (10,8))


plt.scatter(
    X[:,0],          # Class A values
    X[:,1],          # Class B values
    c=y,             ## Means the color of each point is determined by the class label
    s=100            ## Make the point larger

)

plt.scatter(
    model.support_vectors_[:,0],
    model.support_vectors_[:,1],
    s=200,
    edgecolors='black'
    label = 'Support Vectors'

)


w = model.coef_[0]
b = model.intercept_[0]

X_range = np.linspace(1,9,100)

w1 = w[0]
w2 = w[1]


decision_boundary = -(w1 * X_range +b)/w2


margin = 1 / np.sqrt(w**2 + w2**2)


upper_margin = decision_boundary + margin
lower_margin = decision_boundary - margin


plt.plot(
    X_range,
    decision_boundary,
    label = 'Decision Boundary'

)

plt.plot(
    X_range,
    upper_margin,
    '--',
    label = 'Upper Margin'

)


plt.plot(
    X_range,
    lower_margin,
    '--',
    label = 'Lower Margin'

)

plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Soft-Margin SVM')
plt.legend()
plt.show()


from sklearn.datasets import load_wine


wind = load_wine

df = pd.DataFrame(
    wine.data,
    columns= wine.feature_names

)


df['target'] = wine.target


df.head()


X = wine.data
y = wind.target

print(x.shape)

from sklearn.model_selection import train_test_split
X_train , X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42,stratify=y)


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = SVC(kernel='linear')

model.fit(X_train_scaled,y_train)

y_pred = model.predict(X_test_scaled)


from sklearn.metrics import accuracy_score
score = accuracy_score(y_test, y_pred)
print(score)



## 13 features --> PCA ---> PC1 , PC2 ---> 2 D graph


from sklearn.decomposition import PCA
pca = PCA(n_components=2)



X_pca = pca.fit_transform(X_train_scaled)
print(X_train_scaled.shape)
print(X_pca.shape)



plt.figure(figsize=(10,7))

plt.scatter(
    X_pca[:,0],
    X_pca[:,1],
    c = y_train,
    s = 80
)
plt.xlabel('Principal component 1')
plt.ylabel('Principal component 2')
plt.title('Wine dataset')
plt.show()




svm_pca = SVC (
    kernel = 'linear',C=1
)
svm_pca.fit(X_pca,y_train)





X_min = X_pca[:,0].min() - 1
X_max = X_pca[:,0].max() + 1

y_min = X_pca[:,1].min() - 1
y_max = X_pca[:,1].max() + 1





xx , yy = np.meshgrid(
    np.linspace(X_min,X_max,500),
    np.linspace(y_min,y_max,500)
)




grid = np.c_[xx.ravel() , yy.ravel()]






Z = svm_pca.predict(grid)

Z = Z.reshape(xx.shape)




plt.figure(figsize=(10,8))

plt.contourf(
    xx,yy,Z,alpha=0.2
)
plt.scatter(
    X_pca[:,0],
    X_pca[:,1],
    c = y_train,
    s=80
)

plt.xlabel('PC1')
plt.ylabel('PC2')

plt.title('SVM DB')
plt.show()



























































































