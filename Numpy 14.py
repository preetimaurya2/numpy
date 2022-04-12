#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input("14. How to add a border (filled with 0's) around an existing array");get_ipython().run_line_magic('pinfo', 'array')


# In[7]:


import numpy as np
a=np.ones((10,10))
x=np.pad(a,pad_width=1,mode='constant',constant_values=0)
print(x)

