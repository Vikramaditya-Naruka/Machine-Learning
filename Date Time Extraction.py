#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv("C:\\Users\\welcome\\Downloads\\DataFrame\\ecommerce_data.csv")


# In[3]:


df.head()


# In[4]:


df.info()


# # Working of Dates

# In[5]:


df['date'] = pd.to_datetime(df['date'])
df['date'] 


# # 1.Extract year

# In[6]:


df['date_year'] = df['date'].dt.year
df.sample(3)


# # 2.Extract month

# In[7]:


df['date_month'] =df['date'].dt.month
df.sample(2)


# 

# # 3. Month name

# In[8]:


df['month_name'] =df['date'].dt.month_name()
df.sample(2)


# # 4.Extractio

# In[9]:


df['date_days'] = df['date'].dt.day


# In[10]:


df.sample(4)


# # 5.day of week

# In[11]:


df['date of weeks'] = df['date'].dt.dayofweek
df.sample(3)


# # 6.dayofweek name

# In[12]:


df['date_day'] = df['date'].dt.day_name()


# In[13]:


df.sample(5)


# # is weekend

# In[14]:


df['date_is_weekend'] = np.where(df['date_day'].isin(['Sunday','Saturday']),1,0)


# In[15]:


df['date_is_weekend']


# In[16]:


df.sample(9)


# # Extract Week of the Year

# In[17]:


df['date_week'] = df['date'].dt.week

df.sample(5)


# In[18]:


df['quarter'] = df['date'].dt.quarter


# In[19]:


df.sample(4)


# # Extract time elapsed between dates

# In[20]:


import datetime

today = datetime.datetime.today()
today


# In[21]:


today - df['date']


# In[22]:


(today - df['date']).dt.days


# 

# In[23]:


import pandas as pd
import numpy as np


# In[24]:


df = pd.read_csv("C:\\Users\\welcome\\Downloads\\DataFrame\\click.csv")
df


# In[25]:


df['Timestamp'] = pd.to_datetime(df['Timestamp'])


# In[26]:


df['hour'] = df['Timestamp'].dt.hour
df.sample(1)


# In[27]:


df['minute'] = df['Timestamp'].dt.minute
df.sample(2)


# In[28]:


df['second'] = df['Timestamp'].dt.second
df.sample(2)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[29]:


import pandas as pd
import numpy as np


# In[ ]:


df = pd.read_excel("C:\\Users\\welcome\\Downloads\\DataFrame\\store.xlsx")
df.head()


# In[ ]:


df['Order Date'] = pd.to_datetime(df['Order Date'])
df.sample(2)


# In[ ]:


df['date_year'] = df['Order Date'].dt.year
df.sample(3)


# In[ ]:


df['date_month'] =df['Order Date'].dt.month
df.sample(2)


# In[ ]:


df['month_name'] =df['Order Date'].dt.month_name()
df.sample(2)


# In[ ]:


df['date_days'] = df['Order Date'].dt.day
df.sample(4)


# In[ ]:


df['date_day'] = df['Order Date'].dt.day_name()
df.sample(4)


# In[ ]:


df['date_is_weekend'] = np.where(df['Order Date'].isin(['Sunday','Saturday']),1,0)
df.sample(5)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




