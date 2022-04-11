#!/usr/bin/env python
# coding: utf-8

# In[ ]:


13. Create a 2d array with 1 on the border and 0 inside 


# In[ ]:


import numpy as np
a=np.ones((10,10))
a[1:-1,1:-1]=0
print(a)

