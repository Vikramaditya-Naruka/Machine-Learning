#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df =pd.read_csv("C:\\Users\\welcome\\Downloads\\DataFrame\\covid_toy (1).csv")


# In[3]:


df.head()


# In[4]:


x = df.drop(columns = ['has_covid','fever','age'] ,axis = 1)


# In[5]:


x.head(10)


# In[6]:


y = df['has_covid']


# In[7]:


from sklearn.model_selection import train_test_split


# In[8]:


x_train ,x_test , y_train,y_test = train_test_split(x,y,test_size = 0.2 , random_state = 56)


# In[9]:


x_train.shape


# In[10]:


x_test.shape


# In[11]:


y_train.shape


# In[12]:


y_test.shape


# In[13]:


from sklearn.preprocessing import OrdinalEncoder


# In[14]:


oe = OrdinalEncoder(categories=[['Male','Female'],['Mild','Strong'],['Kolkata','Delhi','Mumbai','Bangalore']])


# In[15]:


oe


# In[16]:


oe.fit(x_train)


# In[17]:


x_train = oe.transform(x_train)


# In[18]:


oe.categories_


# In[19]:


x_train


# In[ ]:




