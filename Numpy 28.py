#!/usr/bin/env python
# coding: utf-8

# In[ ]:


28. How to compute ((A+B)*(-A/2)) in place (without copy)?


# In[4]:


import numpy as np
A=np.ones(3)*1
B=np.ones(3)*2
c=np.add(A,B,out=B)
d=np.divide(A,2,out=A)
e=np.multiply(c,d)
print(e)

