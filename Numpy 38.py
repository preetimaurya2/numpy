#!/usr/bin/env python
# coding: utf-8

# In[ ]:


38. Create a structured array with `x` and `y` coordinates covering the [0,1]x[0,1] area


# In[1]:


import numpy as np

Z = np.zeros((5,5), [('x',float),('y',float)])
Z['x'], Z['y'] = np.meshgrid(np.linspace(0,1,5), np.linspace(0,1,5))
print(Z)

