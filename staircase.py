#!/usr/bin/env python
# coding: utf-8

# In[130]:


import numpy as np


# In[151]:


step = 0
a = []
for i in range(1,1000):
    step=0
    for i in range(0,1000):
        out = np.random.randint(1,7)
        if out < 4 and step!=0:
            step = step -1
        if out >= 4 and out < 6:
            step = step+1
        if out == 6: 
            m = np.random.randint(1,7)
            step = step+m
    a.append(step) 

b = np.mean(a)
b


# In[ ]:





# In[ ]:





# In[ ]:




