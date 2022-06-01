#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('44.  How to sort an array by the nth column');get_ipython().run_line_magic('pinfo', 'column')


# In[1]:


import numpy as np

a = np.random.randint(0,10,(3,3))
print(a)
print(a[a[:,1].argsort()])

