#!/usr/bin/env python
# coding: utf-8

# my_list = [1,2,3]

# In[4]:


my_list


# In[5]:


import numpy as np


# In[32]:


arr = np.array(my_list)
arr


# 

# In[8]:


my_mat = [[1,2,3],[4,5,6],[7,8,9]]


# In[9]:


np.array(my_mat)


# In[12]:


np.arange(0,10)


# In[13]:


np.arange(0,11,2)


# In[14]:


np.zeros(3)


# In[18]:


np.ones(4)


# In[20]:


np.linspace(0,5,10)


# In[21]:


np.eye(4)


# In[22]:


np.random.rand(5)


# In[24]:


np.random.rand(5,5)


# In[25]:


np.random.randint(1,100)


# In[26]:


np.random.randint(1,100,10)


# In[43]:


a = [1,2,3,4,5,6,7,8,9]
a = np.array(a)
a.reshape(3,3)


# In[47]:


a.max()


# In[46]:


a.min()


# In[49]:


a.argmax()


# In[50]:


a.argmin()


# In[52]:


a.dtype


# In[53]:


a


# In[54]:


a[5]


# In[55]:


a[1:5]


# In[56]:


a[:6]


# In[57]:


a[5:]


# In[62]:


b = a.reshape(3,3)


# In[63]:


b


# In[64]:


b[0]


# In[65]:


b[0][1]


# In[66]:


b[2][1]


# In[71]:


b[:2]


# In[72]:


b[:]


# In[73]:


b[:] = 99


# In[74]:


b


# In[ ]:




