#!/usr/bin/env python
# coding: utf-8

# In[ ]:


15. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal


# In[1]:


import numpy as np
a=np.diag([1,2,3,4],k=-1)
print(a)


# In[ ]:




