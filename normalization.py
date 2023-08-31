#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df = pd.read_csv('covid_toy (1).csv')
df


# In[3]:


from sklearn.preprocessing import LabelEncoder


# In[4]:


lb = LabelEncoder()


# In[5]:


df['gender'] = lb.fit_transform(df['gender'])
df['cough'] = lb.fit_transform(df['cough'])
df['city'] = lb.fit_transform(df['city'])
df['has_covid'] = lb.fit_transform(df['has_covid'])


# In[6]:


df.head()


# In[7]:


from sklearn.model_selection import train_test_split
x = df.drop(columns = ['has_covid'],axis = 1)
y = df['has_covid']


# In[8]:


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2 ,random_state = 34)


# In[9]:


np.round(x_train.describe(),1)


# In[10]:


from sklearn.preprocessing import MinMaxScaler


# In[11]:


mn = MinMaxScaler()


# In[12]:


x_train_mn = mn.fit_transform(x_train)
x_train_mn


# In[13]:


x_train_new = pd.DataFrame(x_train_mn,columns = x_train.columns)


# In[14]:


x_train_new


# In[15]:


np.round(x_train_new.describe(),1)


# In[ ]:





# In[16]:


#2


# In[17]:


import pandas as pd
import numpy as np


# In[18]:


df = pd.read_csv('C:\\Users\\welcome\\Downloads\\DataFrame\\placement.csv')


# In[19]:


df.head()


# In[20]:


x = df.drop(columns = ['placed'],axis = 1)
y = df['placed']


# In[21]:


from sklearn.model_selection import train_test_split


# In[22]:


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2 ,random_state = 99)


# In[23]:


np.round(x_train.describe(),1)


# In[24]:


from sklearn.preprocessing import MinMaxScaler


# In[25]:


mn = MinMaxScaler()


# In[ ]:





# In[ ]:





# In[26]:


x_train_mn  = mn.fit_transform(x_train)


# In[27]:


x_train_new = pd.DataFrame(x_train_mn,columns = x_train.columns)


# In[28]:


x_train_new


# In[29]:


np.round(x_train_new.describe())


# In[ ]:





# In[30]:


#3


# In[31]:


import pandas as pd
import numpy as np


# In[32]:


df = pd.read_csv("C:\\Users\\welcome\\Downloads\\DataFrame\\supply_chain.csv")
df


# In[33]:


df.info()


# In[34]:


df = df.drop(['Customer demographics','Location','Inspection results','Transportation modes','Routes','Supplier name','Shipping carriers','SKU','Product type'],axis = 1)
df.head()


# In[35]:


df.shape


# In[36]:


x = df.drop(columns = ['Revenue generated'],axis = 1)
y = df['Revenue generated']


# In[37]:


from sklearn.model_selection import train_test


# In[ ]:


from sklearn.preprocessing import StandardScaler


# In[ ]:


st = StandardScaler()


# In[ ]:


x_train_scaled = st.fit_transform(x_train)


# In[ ]:


x_train_scaled


# In[ ]:


x_train_new = pd.DataFrame(x_train_scaled , columns = x_train.columns)


# In[ ]:


x_train_new


# In[ ]:


}

