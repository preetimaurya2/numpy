#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('43.  How to print all the values of an array');get_ipython().run_line_magic('pinfo', 'array')


# In[30]:


import numpy as np

np.set_printoptions(threshold=float('inf'))
a = np.zeros((4,4))
print(a)

