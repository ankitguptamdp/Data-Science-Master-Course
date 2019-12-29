# 11. Interactive Plots Using Matplotlib

# In[119]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[121]:


X = pd.read_csv('../../Csv Files/Linear_X_Train.csv')
Y = pd.read_csv('../../Csv Files/Linear_Y_Train.csv')

theta = np.load('../../NumPy Files/ThetaList.npy')
# 100, 2
T0 = theta[:,0]
T1 = theta[:,1]

plt.ion()
for i in range(0,50,3):
    y_ = T1[i]*X + T0[i]
    
    # Points
    plt.scatter(X,Y)
    # Line
    plt.plot(X,y_,'red')
    plt.draw()
    plt.pause(1) # For one second
    plt.clf() # Destroys the previous object
