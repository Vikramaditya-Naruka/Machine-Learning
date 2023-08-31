#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv("Attrition.csv")


# In[3]:


df


# In[4]:


pip install pandas-profiling


# In[ ]:


from pandas_profiling import ProfileReport
prof = ProfileReport(df)
prof.to_file(output_file = "Attrition.html")


# In[ ]:


df.head()


# In[ ]:


df.dropna()


# In[ ]:


df.value_counts()


# In[ ]:


df.values


# In[ ]:


df.columns


# In[ ]:





# In[ ]:


df


# In[ ]:


df["Att"] = df['Attrition'] = df['Attrition'].where(df['Attrition'] == "Yes", other = None)
df


# In[ ]:


df = df.dropna()


# In[ ]:


df


# In[ ]:


df['Department']


# In[ ]:


df['Department'].info()


# In[ ]:


df['Department']


# In[ ]:


#df['Department'] = df['Department'] = df['Department'].where(df['Department'] == "Research & Development", other = None)


# In[ ]:


df


# In[ ]:


np.unique(df['Department'],return_counts = True)


# In[ ]:


np.unique(df['EducationField'],return_counts = True)


# In[ ]:


np.unique(df['PerformanceRating'],return_counts = True)


# In[ ]:


np.unique(df['YearsSinceLastPromotion'],return_counts = True)


# In[ ]:


np.unique(df['OverTime'],return_counts = True)


# In[ ]:


df.columns


# In[ ]:


np.unique(df['DistanceFromHome'],return_counts = True)


# In[ ]:


np.unique(df['YearsSinceLastPromotion'],return_counts = True)


# In[ ]:


np.unique(df['PerformanceRating'],return_counts = True)


# In[ ]:


np.unique(df['PercentSalaryHike'],return_counts = True)


# In[ ]:


from pandas_profiling import ProfileReport
prof = ProfileReport(df)
prof.to_file(output_file = "Attritionafteryes.html")


# In[ ]:





# In[ ]:





# In[ ]:


df = pd.read_csv("Attrition.csv")
df


# In[ ]:


df["Attno"] = df['Attrition'] = df['Attrition'].where(df['Attrition'] == "No", other = None)
df


# In[ ]:


df = df.dropna()
df


# In[ ]:


np.unique(df['Department'],return_counts = True)


# In[ ]:


np.unique(df['EducationField'],return_counts = True)


# In[ ]:


np.unique(df['PerformanceRating'],return_counts = True)


# In[ ]:


np.unique(df['YearsSinceLastPromotion'],return_counts = True)


# In[ ]:


np.unique(df['OverTime'],return_counts = True)


# In[ ]:


np.unique(df['DistanceFromHome'],return_counts = True)


# In[ ]:


np.unique(df['YearsSinceLastPromotion'],return_counts = True)


# In[ ]:


np.unique(df['PerformanceRating'],return_counts = True)


# In[ ]:


np.unique(df['PercentSalaryHike'],return_counts = True)


# In[ ]:


np.unique(df['Gender'],return_counts = True)


# In[ ]:


df.describe()


# In[ ]:


from pandas_profiling import ProfileReport
prof = ProfileReport(df)
prof.to_file(output_file = "AttritionafterNo.html")


# In[ ]:





# In[ ]:




