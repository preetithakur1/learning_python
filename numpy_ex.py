#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


np.zeros(10)


# In[5]:


a = np.ones(10)


# In[6]:


a*5


# In[7]:


b = np.arange(10,51)


# In[8]:


b


# In[10]:


np.arange(10,51,2)


# In[11]:


c = [[0,1,2],[3,4,5],[6,7,8]]


# In[12]:


np.array(c)


# In[13]:


np.eye(3,3)


# In[18]:


np.random.rand(1)


# In[20]:


np.random.randn(25)


# In[38]:


(np.arange(100).reshape(10,10)+1)/100


# In[46]:


np.linspace(0,1,20)


# In[53]:


mat = np.arange(1,26).reshape(5,5)
mat


# In[79]:


mat[2:,1:]


# In[84]:


mat[3][4]


# In[109]:


mat[:3,1:2]


# In[110]:


mat[4]


# In[120]:


mat[3:]


# In[129]:


np.sum(mat)


# In[130]:


np.std(mat)


# In[139]:


np.sum(mat,0)


# In[ ]:





# In[ ]:




