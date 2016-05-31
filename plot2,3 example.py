
# coding: utf-8

# In[139]:

#%matplotlib inline
import numpy as np
from sympy import *
import matplotlib.pyplot as plt


# In[140]:

V4_16 = [4,6,8,10,12,14,16]


# In[141]:

d0 = [1.015,1.570,2.102,2.648,3.153,3.648,4.195]
d30 = [0.825,1.258,1.715,2.140,2.53,2.970,3.387]
d60 = [0.378,0.575,0.768,0.993,1.131,1.345,1.528]
d90 = [0.034,0.049,0.060,0.071,0.082,0.096,0.120]
D = [d0,d30,d60,d90]


# In[142]:

plt.plot(V4_16,D[0],label = 'theta = 0')
plt.xlabel('Volt')
plt.ylabel('I [A]')
plt.title('theta = 0 to pi/2')
plt.plot(V4_16,D[1],label = 'theta = pi/6')
plt.plot(V4_16,D[2],label = 'theta = pi/3')
plt.plot(V4_16,D[3],label = 'theta = pi/2')
plt.legend(loc='upper left')


# In[143]:

R_1 = []
for d in D:
    R_1 = R_1 +[(d[6] - d[0])/12]


# In[144]:

R_1


# In[145]:

R = [] # 4.136504654,
for r in R_1:
    R = R + [1/r]
R
Rmore = [R[0]] + [4.136504654] + [R[1]] + [6.349206349] + [R[2]] + [25.53191489] + [R[3]]
Rmore


# In[146]:

x =  np.linspace(0,(3.14159265358979)/2 -0.15, num = 100,endpoint=False)
y1 =np.cos(x)
y = []
for c in y1:
    y =y + [2/(c**2)]
y    


# In[147]:

plt.plot([0,pi/12,pi/6,pi/4,pi/3,pi*5/12,pi/2],Rmore,'o--r',label = 'theta,R')
plt.plot(x,y,label = 'theta , c/Intensity')
plt.legend(loc ='upper left')  
plt.title('theta and resistance')
plt.xlabel('theta [rad]')
plt.ylabel('resistance [ohm]')


# In[148]:

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')


# In[149]:

theta = np.linspace(-4* np.pi, 4*np.pi,100)
z = np.linspace(-2,2,100)
r = z**2 + 1


# In[150]:

x= r*np.sin(theta)
y= r*np.cos(theta)


# In[151]:

Z =  np.array([1,2])


# In[152]:

X = Z *np.array([3,4])


# In[153]:

X


# In[154]:

ax.plot(x,y,z, label = 'parametic curve')
ax.legend()
plt.show()


# In[156]:




# In[ ]:



