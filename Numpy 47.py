#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('47. How to get the diagonal of a dot product');get_ipython().run_line_magic('pinfo', 'product')


# In[16]:


import numpy as np
a = np.random.randint(0,11,(3,3))
b = np.random.randint(0,11,(3,3))

np.diag(np.dot(a,b))

