#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd 


# In[2]:


df = pd.read_csv("covid_toy (1).csv")


# In[3]:


df.head() 


# In[4]:


df.shape


# In[5]:


from sklearn.preprocessing import LabelEncoder 


# In[6]:


lb = LabelEncoder() 


# In[7]:


df['gender'] = lb.fit_transform(df['gender'])
df['cough'] = lb.fit_transform(df['cough'])
df['city'] = lb.fit_transform(df['city'])
df['has_covid'] = lb.fit_transform(df['has_covid'])


# In[8]:


df


# In[ ]:





# In[ ]:





# In[9]:


x = df.drop(columns = ['has_covid'] , axis = 1) 


# In[10]:


x.shape


# In[11]:


x


# In[12]:


y = df['has_covid']


# In[13]:


y.shape


# In[14]:


from sklearn.model_selection import train_test_split 


# In[15]:


x_train , x_test , y_train , y_test = train_test_split(x,y,test_size = 0.2 , random_state = 42)


# In[16]:


x_train


# In[17]:


x_test


# In[18]:


x_test.shape


# In[19]:


y_train


# In[20]:


y_train.shape


# In[21]:


y_test.shape


# In[22]:


df


# In[23]:


from sklearn.preprocessing import StandardScaler 


# In[24]:


sc = StandardScaler() 


# In[25]:


x_train_scaled = sc.fit_transform(x_train) 


# In[26]:


x_train_scaled


# In[27]:


np.round(x_train.describe() , 1) 


# In[28]:


x_train_new = pd.DataFrame(x_train_scaled , columns = x_train.columns) 


# In[29]:


x_train_new


# In[30]:


np.round(x_train_new.describe() , 1) 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




