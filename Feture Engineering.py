#!/usr/bin/env python
# coding: utf-8
Data ==> dependent data == > data which dependent another data
         independent data == > data which is not dependent another datadata trained == >  underfitting == >  the model which is not proper trained the given data , the accuracy is low that data
                   overfitting == > the model which is trained only given data and the accuracy is high only the given data  memorization ==> when the model is trained the given data and only give the solution of on the basis of data
generalization ==> the model also perform on the unseen data
# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("covid_toy (1).csv")


# In[3]:


df


# In[4]:


df.shape


# In[5]:


x = df.drop(columns = ["has_covid"])


# In[6]:


x.shape


# In[7]:


y  = df["has_covid"]


# In[8]:


y.shape


# In[9]:


from sklearn.model_selection import train_test_split


# In[10]:


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 42)


# In[11]:


x_train


# In[12]:


x_train.shape


# In[13]:


x_test.shape


# In[14]:


y_train


# In[15]:


y_train.shape


# In[16]:


y_test.shape


# In[ ]:





# In[ ]:





# In[17]:


df1 = pd.read_csv("tips.csv")


# In[18]:


df1.head()


# In[19]:


df1.shape


# In[20]:


x = df1.drop(columns = ['total_bill'])


# In[21]:


x.shape


# In[22]:


y = df1['total_bill']


# In[23]:


y.shape


# In[24]:


from sklearn.model_selection import train_test_split


# In[25]:


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2 ,random_state = 42)


# In[26]:


x_train


# In[27]:


x_train.shape


# In[28]:


x_test.shape


# In[29]:


y_train.shape


# In[30]:


y_test.shape


# In[ ]:





# In[ ]:





# In[31]:


df2 = pd.read_csv("cars.csv")


# In[32]:


df2


# In[33]:


df2.shape


# In[34]:


x = df2.drop(columns = ['selling_price'], axis = 1)


# In[35]:


y = df2['selling_price']


# In[36]:


x.shape


# In[37]:


y.shape


# In[38]:


from sklearn.model_selection import train_test_split


# In[39]:


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2 ,random_state = 23)


# In[40]:


x_train.shape


# In[41]:


x_test.shape


# In[42]:


y_train.shape


# In[43]:


y_test.shape


# In[ ]:





# In[ ]:





# In[44]:


df3 = pd.read_csv("Attrition.csv")
df3.head()


# In[45]:


x = df3.drop(columns = ['Attrition'])


# In[46]:


x.shape


# In[47]:


y = df3['Attrition']


# In[48]:


y.shape


# In[49]:


from sklearn.model_selection import train_test_split


# In[50]:


x_test ,x_train,y_test,y_train = train_test_split(x,y,test_size = 0.2 ,  random_state = 45)


# In[51]:


x_train.shape


# In[52]:


x_test.shape


# In[53]:


y_train.shape


# In[54]:


y_test.shape


# In[ ]:





# In[ ]:





# In[55]:


df4 = pd.read_csv("placement.csv")
df4.head()


# In[56]:


df4.shape


# In[57]:


x = df4.drop(columns = 'placed')
x.shape


# In[58]:


y = df4['placed']
y.shape


# In[59]:


from sklearn.model_selection import train_test_split


# In[60]:


x_train ,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2, random_state = 56)


# In[61]:


x_train.shape


# In[62]:


x_test.shape


# In[63]:


y_train.shape


# In[64]:


y_test.shape


# In[ ]:





# In[65]:


import pandas as pd
import numpy as np


# In[66]:


df = pd.read_csv("covid_toy (1).csv")


# In[67]:


df.head(2)


# In[68]:


df.shape


# In[69]:


from sklearn.preprocessing import LabelEncoder


# In[70]:


lb = LabelEncoder()


# In[71]:


df['gender'] = lb.fit_transform(df['gender'])
df['cough'] = lb.fit_transform(df['cough'])
df['city'] = lb.fit_transform(df['city'])
df['has_covid'] = lb.fit_transform(df['has_covid'])


# In[72]:


df.head(4)


# In[73]:


x = df.drop(columns = ['has_covid'])


# In[74]:


x.head(1)


# In[75]:


y = df['has_covid']
y.head(1)


# In[76]:


from sklearn.model_selection import train_test_split


# In[77]:


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2 ,random_state = 78)


# In[78]:


x_train.shape


# In[79]:


x_test.shape


# In[80]:


x_train


# In[81]:


y_train.shape


# In[82]:


y_test.shape


# In[83]:


from sklearn.preprocessing import StandardScaler


# In[84]:


sc = StandardScaler()


# In[85]:


x_train_scale = sc.fit_transform(x_train)


# In[86]:


x_train_scale


# In[87]:


np.round(x_train.describe(),1)


# In[88]:


x_train_new = pd.DataFrame(x_train_scale ,columns = x_train.columns)


# In[89]:


x_train_new


# In[90]:


np.round(x_train_new.describe(),1)


# In[ ]:




