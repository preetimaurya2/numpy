#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('39. How to find the closest value (to a given scalar) in a vector');get_ipython().run_line_magic('pinfo', 'vector')


# In[1]:


import numpy as np
a=np.random.uniform(1,5,20)
b=4
c=a[np.abs(a-b).argmin()]
print(c)

