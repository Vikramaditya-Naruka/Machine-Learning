#!/usr/bin/env python
# coding: utf-8
                                              outlier 
                                             1.trimming 
                                              2.capping
# In[59]:


import pandas as pd
import numpy as np


# In[34]:


df = pd.read_csv("C:\\Users\\welcome\\Downloads\\DataFrame\\newplacementdata.csv")
df.head()


# In[35]:


# even = ((n/2)+((n/2)+1))/2
# odd = ((n/2)+1)


# In[36]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[37]:


plt.figure(figsize = (15,5))
plt.subplot(121)
sns.distplot(df['cgpa'])
plt.subplot(122)
sns.distplot(df['placement_exam_marks'])
plt.show()


# In[38]:


df['placement_exam_marks'].describe()


# In[39]:


sns.boxplot(x = df['placement_exam_marks'])


# In[40]:


#finding the IQR
percentile25 = df['placement_exam_marks'].quantile(0.25)
percentile75 = df['placement_exam_marks'].quantile(0.75)


# In[41]:


percentile25


# In[42]:


percentile75


# In[43]:


IQR = percentile75-percentile25
IQR


# In[44]:


upper_limit = percentile75+1.5*IQR
lower_limit = percentile25-1.5*IQR


# In[45]:


upper_limit


# In[46]:


lower_limit


# # Finding our Outliers

# In[47]:


df[df['placement_exam_marks']>upper_limit]


# In[48]:


df[df['placement_exam_marks']<lower_limit]


# # Trimming (outlier Removing technique 1)

# In[49]:


new_df = df[df['placement_exam_marks']<upper_limit]


# In[50]:


new_df


# # comparision

# In[51]:


plt.figure(figsize=(15,5))
plt.subplot(221)
sns.distplot(x= df['placement_exam_marks'])

plt.subplot(222)
sns.boxplot(x = df['placement_exam_marks'])

plt.subplot(223)
sns.distplot(x = new_df['placement_exam_marks'])

plt.subplot(224)
sns.boxplot(x = new_df['placement_exam_marks'])

plt.show()


# # Capping(Outlier Removing technique 2)

# In[52]:


new_df_cap = df.copy()


# In[ ]:


# min = 5 , max 15

#min  4 , 3, 1


# In[53]:


new_df_cap['placement_exam_marks'] = np.where(
    
   new_df_cap['placement_exam_marks']>upper_limit,
   upper_limit ,
    np.where(
    new_df_cap['placement_exam_marks']< lower_limit,
    lower_limit,
    new_df_cap['placement_exam_marks']
    ))


# In[54]:


new_df_cap


# In[55]:


new_df_cap.shape


# In[56]:


#comparison


# In[57]:


plt.figure(figsize=(15,5))
plt.subplot(221)
sns.distplot(x= df['placement_exam_marks'])

plt.subplot(222)
sns.boxplot(x = df['placement_exam_marks'])

plt.subplot(223)
sns.distplot(x = new_df_cap['placement_exam_marks'])

plt.subplot(224)
sns.boxplot(x = new_df_cap['placement_exam_marks'])

plt.show()


# In[128]:


import pandas as pd
import numpy as np


# In[130]:


df = pd.read_csv('C:\\Users\\welcome\\Downloads\\DataFrame\\tips.csv')


# In[131]:


df.head()


# In[132]:


plt.figure(figsize=(15,5))
plt.subplot(221)
sns.distplot(x= df[])

plt.subplot(222)
sns.boxplot(x = df['size'])


# In[133]:


percentile25 = df['size'].quantile(0.25)
percentile75 = df['size'].quantile(0.75)


# In[134]:


percentile25


# In[135]:


percentile75


# In[136]:


IQR = percentile75-percentile25
IQR


# In[137]:


upper_limit = percentile75+1.5*IQR
lower_limit = percentile25-1.5*IQR


# In[138]:


upper_limit


# In[139]:


lower_limit


# In[140]:


df[df['size']>upper_limit]


# # Trimming

# In[141]:


new_df = df[df['size']<upper_limit]


# In[142]:


new_df


# In[143]:


plt.figure(figsize=(15,5))
plt.subplot(221)
sns.distplot(x= df['size'])

plt.subplot(222)
sns.boxplot(x = df['size'])

plt.figure(figsize=(15,5))
plt.subplot(223)
sns.distplot(x= new_df['size'])

plt.subplot(224)
sns.boxplot(x = new_df['size'])


# # Capping

# In[144]:


new_df_cap = df.copy()


# In[145]:


new_df_cap


# In[146]:


new_df_cap['size'] = np.where(new_df_cap['size']>upper_limit,
                             upper_limit,
                     np.where(new_df_cap['size']<lower_limit,
                             lower_limit
                              ,new_df_cap['size']
                             ))


# In[147]:


new_df_cap


# In[ ]:





# In[ ]:





# In[ ]:




