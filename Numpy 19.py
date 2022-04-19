#!/usr/bin/env python
# coding: utf-8

# In[ ]:


19. Normalize a 5x5 random matrix


# In[1]:


import numpy as np
a=np.random.random((5,5))
b = (a - a.min()) / (a.max()-a.min())
print(b)

