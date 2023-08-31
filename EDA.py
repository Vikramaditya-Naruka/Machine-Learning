#!/usr/bin/env python
# coding: utf-8

# # EDA ==> Exploratory Data Analysis

# # 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv("covid_toy (1).csv")
df


# In[3]:


df.columns


# In[4]:


sns.countplot(x = df['has_covid'])


# In[5]:


df['has_covid'].value_counts()


# In[6]:


df['has_covid'].value_counts().plot(kind = 'bar')


# In[7]:


df


# In[8]:


df['cough'].value_counts().plot(kind = 'bar')
df['cough'].value-counts().plot(kind = 'bar')


# In[ ]:


df['cough'].value_counts()


# In[ ]:


df['cough'].value_counts().plot(kind = 'pie',autopct = '%.2f')


# In[ ]:


df['has_covid'].value_counts().plot(kind = 'pie',autopct = '%.2f')


# In[ ]:


plt.hist(df['age'])


# In[ ]:


plt.hist(['fever'])


# In[ ]:


sns.displot(df['age'])


# In[ ]:


sns.distplot(df['fever'])


# In[ ]:


sns.distplot(df['fever'])


# In[ ]:


sns.distplot(df['fever'], hist = False)


# In[ ]:


sns.distplot(df['age'], hist = False)


# In[ ]:


df['age'].describe()


# In[ ]:


sns.boxplot(df['age'] )


# In[ ]:


f = pd.read_csv('tips.csv')
f


# # bivariative analysis

# In[ ]:


#1. scatterplot(Numerical column - Numerical column)


# In[ ]:


sns.scatterplot(x = f['total_bill'],
               y = f['tip'])


# In[ ]:


#2. scatterplot(Numerical column - categorical column)
sns.scatterplot(x=f['total_bill'],y=f['tip'] , hue = f['sex'])


# In[ ]:


sns.scatterplot(x=f['total_bill'],y=f['tip'] ,data = f, hue = f['sex'])


# In[ ]:


sns.scatterplot(x=f['total_bill'],y=f['tip'] ,data = f, hue = f['sex'],style = f['smoker'])


# In[ ]:


sns.scatterplot(x=f['total_bill'],y=f['tip'] , hue = f['sex'],style = f['smoker'])


# In[ ]:


sns.barplot(x = f['time'],y = f['total_bill'])


# In[ ]:


sns.distplot(df[df["has_covid"] == "Yes"]['age'],hist = False)


# In[ ]:





# In[ ]:


p = pd.crosstab(df['has_covid'],df['cough'])
p


# In[ ]:


sns.heatmap(p)


# # pandas profilling

# In[ ]:


import pandas as pd


# In[ ]:


pip install pandas-profiling


# In[ ]:


from pandas_profiling import ProfileReport
prof = ProfileReport(f)
prof.to_file(output_file = "view.html")


# In[ ]:


from ydata_profiling import ProfileReport
prof = ProfileReport(f)
prof.to_file(output_file = "v.html")


# In[ ]:





# In[ ]:





# In[ ]:




