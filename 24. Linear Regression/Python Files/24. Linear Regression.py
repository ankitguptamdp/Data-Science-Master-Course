#!/usr/bin/env python
# coding: utf-8

# # 01. Linear Regression

# <img src = '../Images/01. Linear Regression/Image001.png'/>
# <img src = '../Images/01. Linear Regression/Image002.png'/>
# <img src = '../Images/01. Linear Regression/Image003.png'/>
# <img src = '../Images/01. Linear Regression/Image004.png'/>
# <img src = '../Images/01. Linear Regression/Image005.png'/>
# <img src = '../Images/01. Linear Regression/Image006.png'/>
# <img src = '../Images/01. Linear Regression/Image007.png'/>
# <img src = '../Images/01. Linear Regression/Image008.png'/>
# <img src = '../Images/01. Linear Regression/Image009.png'/>
# <img src = '../Images/01. Linear Regression/Image010.png'/>
# <img src = '../Images/01. Linear Regression/Image011.png'/>
# <img src = '../Images/01. Linear Regression/Image012.png'/>
# <img src = '../Images/01. Linear Regression/Image013.png'/>

# # 02. Gradient Descent Implementation

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


X = np.arange(10)
Y = (X-5)**2
print(X, Y)


# **Goal:**
# Given a Function f(x), we want to find the value of x that minimizes f(x).

# ### Visualisation

# In[3]:


plt.plot(X, Y)
plt.show()


# In[4]:


plt.style.use('seaborn')


# In[5]:


plt.plot(X, Y)
plt.ylabel('f(x)')
plt.xlabel('x')
plt.show()


# In[6]:


x = 0 
lr = 0.1 # Learning Rate
error = []

# 50 steps in the downhill direction
plt.plot(X, Y)
for i in range(50):
    grad = 2*(x-5)
    x = x - lr * grad
    y = (x-5)**2
    error.append(y)
    plt.scatter(x, y)
    print(x)
plt.show()


# In[7]:


# Plot the values of error
plt.plot(error)
plt.show()


# In[8]:


x = 0 
lr = 0.1 # Learning Rate
error = []
prev_error = np.inf
# 50 steps in the downhill direction
plt.plot(X, Y)
for i in range(50):
    grad = 2*(x-5)
    x = x - lr * grad
    y = (x-5)**2
    error.append(y)
    plt.scatter(x, y)
    print(x)
    if abs(prev_error-y)<0.0001:
        break
    prev_error = y
    
plt.show()


# <img src = '../Images/02. Gradient Descent Implementation/Image001.png'/>

# # 03. Gradient Descent Algorithm

# <img src = '../Images/03. Gradient Descent Algorithm/Image001.png'/>
# <img src = '../Images/03. Gradient Descent Algorithm/Image002.png'/>
# <img src = '../Images/03. Gradient Descent Algorithm/Image003.png'/>

# # 04. Gradient Descent Update Rule for Regression

# <img src = '../Images/04. Gradient Descent Update Rule for Regression/Image001.png'/>
# <img src = '../Images/04. Gradient Descent Update Rule for Regression/Image002.png'/>
# <img src = '../Images/04. Gradient Descent Update Rule for Regression/Image003.png'/>
# <img src = '../Images/04. Gradient Descent Update Rule for Regression/Image004.png'/>
# <img src = '../Images/04. Gradient Descent Update Rule for Regression/Image005.png'/>
# <img src = '../Images/04. Gradient Descent Update Rule for Regression/Image006.png'/>
# <img src = '../Images/04. Gradient Descent Update Rule for Regression/Image007.png'/>
# <img src = '../Images/04. Gradient Descent Update Rule for Regression/Image008.png'/>
# <img src = '../Images/04. Gradient Descent Update Rule for Regression/Image009.png'/>

# # 05. Data Preparation

# In[9]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ### Section 1. Load and Visualise the Data
# - Download
# - Load
# - Visualise
# - Normalisation

# In[10]:


# Load
X = pd.read_csv('../Csv Files/Linear_X_Train.csv')
Y = pd.read_csv('../Csv Files/Linear_Y_Train.csv')
print(X.head())
print(Y.head())


# In[11]:


# Visualise
plt.scatter(X,Y)
plt.show()


# In[12]:


plt.style.use('seaborn')


# In[13]:


plt.scatter(X,Y)
plt.show()


# In[14]:


X.shape


# In[15]:


Y.shape


# In[16]:


type(X)


# In[17]:


# Convert X, Y to NumPy arrays
X = X.values
Y = Y.values


# In[18]:


# Normalisation
u = X.mean()
std = X.std()

print(u,std)


# In[19]:


X = (X-u)/std


# In[20]:


plt.scatter(X,Y,color='orange')
plt.title('Marks vs Performance Graph')
plt.xlabel('Hardwork')
plt.ylabel('Performance')
plt.show()


# # 06. Implementing Gradient Descent

# In[25]:


def hypothesis(x, theta):
    # theta = [theta0, theta1]
    y_ = theta[0] + theta[1]*x
    return y_

def gradient(X, Y, theta):
    m = X.shape[0]
    grad = np.zeros((2,))
    for i in range(m):
        x = X[i]
        y_ = hypothesis(x,theta)
        y = Y[i]
        grad[0] += (y_ - y)
        grad[1] += (y_ - y)*x
        
    return grad/m

def error(X, Y, theta):
    m = X.shape[0]
    total_error = 0.0
    for i in range(m):
        y_ = hypothesis(X[i], theta)
        total_error += (y_ - Y[i])**2
    return total_error/m

def gradientDescent(X, Y, max_steps = 100, learning_rate = 0.1):
    theta = np.zeros((2,))
    error_list = []
    for i in range(max_steps):
        # Compute grad
        grad = gradient(X, Y, theta)
        e = error(X,Y,theta)
        error_list.append(e)
        # Update theta
        theta[0] = theta[0] - learning_rate*grad[0]
        theta[1] = theta[1] - learning_rate*grad[1]
    return theta,error_list


# In[26]:


theta,error_list = gradientDescent(X,Y)


# In[27]:


theta


# In[28]:


error_list


# # 07. Making Predictions and Submitting Online Challenge

# In[29]:


y_ = hypothesis(X, theta)
print(y_)


# In[31]:


# Training - Predictions
plt.scatter(X,Y)
plt.plot(X,y_,color='orange',label='Prediction')
plt.legend()
plt.show()


# In[32]:


# Load the test data
x_test = pd.read_csv('../Csv Files/Linear_X_Test.csv').values
y_test = hypothesis(x_test,theta)
y_test.shape


# In[34]:


df = pd.DataFrame(data=y_test,columns=['y'])


# In[35]:


df.to_csv('../Csv Files/y_prediction.csv',index=False)


# # 08. Linear Regression Code - Scoring

# In[36]:


# Score : R2 (R-Squared) or Coefficient of Determination


# In[39]:


def r2_score(Y,y_):
    # Instead of Loop, np.sum is recommende as it is fast
    num = np.sum((Y-y_)**2)
    denom = np.sum((Y-Y.mean())**2)
    score = (1-num/denom)
    return score*100


# In[40]:


r2_score(Y,y_)


# <img src ='../Images/08. Linear Regression Code - Scoring/Image001.png'/>

# # 09. Surface Plots and Contours

# ### Surface Plots are used to
# - Visualise Loss Functions in Machine Learning & Deep Learning
# - Visualise State or State Value Functions in Reinforcement Learning

# In[49]:


# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D


# In[50]:


import matplotlib.pyplot as plt
import numpy as np


# In[51]:


a = np.array([1,2,3])
b = np.array([4,5,6,7])
a,b = np.meshgrid(a,b)
print(a)
print(b)


# In[56]:


fig = plt.figure()
axes = fig.gca(projection='3d')
axes.plot_surface(a,b,a+b)
plt.show()


# In[57]:


fig = plt.figure()
axes = fig.gca(projection='3d')
axes.plot_surface(a,b,a+b,cmap='coolwarm')
plt.show()


# In[58]:


fig = plt.figure()
axes = fig.gca(projection='3d')
axes.plot_surface(a,b,a+b,cmap='rainbow')
plt.show()


# In[59]:


fig = plt.figure()
axes = fig.gca(projection='3d')
axes.plot_surface(a,b,a**2+b**2,cmap='rainbow')
plt.show()


# In[61]:


a = np.arange(-1,1,0.02)
b = a
print(a)
a,b = np.meshgrid(a,b)


# In[63]:


fig = plt.figure()
axes = fig.gca(projection='3d')
axes.plot_surface(a,b,a**2+b**2,cmap='rainbow')
plt.show()


# In[66]:


fig = plt.figure()
axes = fig.gca(projection='3d')
axes.contour(a,b,a**2+b**2,cmap='rainbow')
plt.title('Contour Plot')
plt.show()


# In[ ]:




