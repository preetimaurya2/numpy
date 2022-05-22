#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('42.  How to randomly place p elements in a 2D array');get_ipython().run_line_magic('pinfo', 'array')


# In[17]:


import numpy as np

a=np.zeros((5,5))
a.put(np.random.choice(np.arange(5*5),3,replace=False),4)
print(a)

