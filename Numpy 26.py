#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('26. How to get the dates of yesterday, today and tomorrow');get_ipython().run_line_magic('pinfo', 'tomorrow')


# In[1]:


import numpy as np

a=np.datetime64('today')
b=np.datetime64('today')-np.timedelta64(1)
c=np.datetime64('today')+np.timedelta64(1)
print('today',a)
print('yesterday',b)
print('tomorrow',c)

