#!/usr/bin/env python
# coding: utf-8

# In[ ]:


3. How to find the memory size of any array 


# In[ ]:


import numpy as np
a=np.zeros(10)
print(a.size)
print(a.itemsize)
print('memory size',(a.size)*(a.itemsize))

