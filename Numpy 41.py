#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('41. What is the equivalent of enumerate for numpy arrays');get_ipython().run_line_magic('pinfo', 'arrays')


# In[5]:


import numpy as np

a=np.arange(9).reshape(3,3)

for i,j in np.ndenumerate(a):
    print(i,j)
      

