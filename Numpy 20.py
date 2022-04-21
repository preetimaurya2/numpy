#!/usr/bin/env python
# coding: utf-8

# In[ ]:


20.Create a custom dtype that describes a color as four unsigned bytes (RGBA) 


# In[1]:


import numpy as np
color = np.dtype([("R", np.ubyte),
                  ("G", np.ubyte),
                  ("B", np.ubyte),
                  ("A", np.ubyte)])
print(color)

