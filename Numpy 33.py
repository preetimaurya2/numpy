#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('33.How to sum a small array faster than np.sum');get_ipython().run_line_magic('pinfo', 'np.sum')


# In[2]:


import numpy as np
a=np.arange(10)

print(np.sum(a))

print(sum(a))

print(np.add.reduce(a))

