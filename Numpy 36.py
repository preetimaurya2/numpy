#!/usr/bin/env python
# coding: utf-8

# In[ ]:


36.Consider a random 10x2 matrix representing cartesian coordinates, convert them to polar coordinates


# In[4]:


import numpy as np

a=np.random.randint(1,10,(10,2))
b=a[:,0]
c=a[:,1]

r=np.sqrt(b**2+c**2)
print(r)
print('\n')
t=np.arctan(c/b)
print(t)

