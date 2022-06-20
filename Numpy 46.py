#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('46. How to tell if a given 2D array has null columns');get_ipython().run_line_magic('pinfo', 'columns')


# In[19]:


import numpy as np
a=[[np.nan,1,2],[3,4,5],[7,9,np.nan]]
np.any(np.isnan(a).any(axis=0))

