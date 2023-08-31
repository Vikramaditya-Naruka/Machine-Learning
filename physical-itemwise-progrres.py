#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib 
import seaborn as sns


# In[19]:


data = pd.read_excel("physical.xlsx")
data


# In[20]:


#from pandas_profiling import ProfileReport 
#prof = ProfileReport(df)
#prof.to_file(output_file = "physical.html")


# In[21]:


data.isnull().sum()
data = data.dropna()


# In[22]:


data


# In[23]:


data[['TRANCHE','MONTH']].value_counts()


# In[24]:


data.isnull().sum()


# In[25]:


sns.barplot(x = data['OVERALL PROGRESS TILL THIS MONTH(in KM)'],y = data['OVERALL PROGRESS DURING THIS MONTH(in KM)'])


# In[26]:


data.head(5)


# In[27]:


data['TRANCHE'].value_counts()


# In[28]:


data['TRANCHE'].value_counts().plot(kind = "pie")


# In[29]:


data['TRANCHE3'] = data['TRANCHE'].where(data['TRANCHE'] == 'Tranche-III' ,other = None)
#df['Department'] = df['Department'] = df['Department'].where(df['Department'] == "Research & Development", other = None)


# In[30]:


data.head(1)


# In[31]:


data = df


# In[ ]:


df['TRANCHE2'] = df['TRANCHE'].where(df['TRANCHE'] == 'Tranche-II' ,other = None)


# In[ ]:


data.head()


# In[ ]:


df['TRANCHE1'] = df['TRANCHE'].where(df['TRANCHE'] == 'Tranche-I' ,other = None)


# In[ ]:


df.head()


# In[ ]:


data.isnull().sum()


# In[ ]:


data


# In[41]:


#p1 = pd.crosstab(data['OVERALL PROGRESS TILL THIS MONTH(in KM)'],data['TRANCHE1'])
#p1


# In[42]:


#p2 = pd.crosstab(data['OVERALL PROGRESS TILL THIS MONTH(in KM)'],data['TRANCHE2'])
#p2


# In[43]:


#p3 = pd.crosstab(df['OVERALL PROGRESS TILL THIS MONTH(in KM)'],df['TRANCHE3'])
#p3


# In[ ]:


#p1.describe()


# In[ ]:


#p2.describe()


# In[44]:


#p3.describe()


# In[33]:


data.head(1)


# In[ ]:





# # Cumulative Project Progress Over Time

# In[34]:


data['DATE'] = pd.to_datetime(data['MONTH'] + ' ' + data['YEAR'].astype(str), format='%B %Y')

# Calculate cumulative progress for each month
data['CUMULATIVE_PROGRESS'] = data['OVERALL PROGRESS DURING THIS MONTH(in KM)'].cumsum()

plt.figure(figsize=(10, 6))

plt.plot(data['DATE'], data['CUMULATIVE_PROGRESS'], marker='o')

plt.xlabel('Date')
plt.ylabel('Cumulative Progress (in KM)')
plt.title('Cumulative Project Progress Over Time')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.show()


# # distribution

# In[35]:


# Unique Tranches and Modes
unique_tranches = data['TRANCHE'].unique()
unique_modes = data['MODE'].unique()

# Data Visualization
plt.figure(figsize=(14, 8))

# Create a subplot for each combination of Tranche and Mode
for i, tranche in enumerate(unique_tranches):
    for j, mode in enumerate(unique_modes):
        plt.subplot(len(unique_tranches), len(unique_modes), i * len(unique_modes) + j + 1)
        
        # Filter data for the specific Tranche and Mode combination
        subset = data[(data['TRANCHE'] == tranche) & (data['MODE'] == mode)]
        
        plt.plot(subset['DATE'], subset['CUMULATIVE_PROGRESS'], marker='o')
        plt.title(f'Tranche: {tranche}\nMode: {mode}')
        
        plt.xlabel('Date')
        plt.ylabel('Cumulative Progress (in KM)')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()

plt.show()


# # Month-wise Project Progress

# In[36]:


plt.figure(figsize=(12, 6))

# Group data by month and calculate the sum of progress for each month
monthly_progress = data.groupby(['DATE'])['OVERALL PROGRESS DURING THIS MONTH(in KM)'].sum().reset_index()

# Create a bar chart or line chart for month-wise progress
sns.barplot(x='DATE', y='OVERALL PROGRESS DURING THIS MONTH(in KM)', data=monthly_progress)

plt.xlabel('Month')
plt.ylabel('Total Progress (in KM)')
plt.title('Month-wise Project Progress')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


# # Project Delay Over Time

# In[47]:


# Calculate the difference between planned progress and actual progress
data['DELAY'] = data['OVERALL PROGRESS TILL THIS MONTH(in KM)'] - data['CUMULATIVE_PROGRESS']

# Data Visualization
plt.figure(figsize=(10, 6))

plt.plot(data['DATE'], data['DELAY'], marker='o', color='red')

plt.xlabel('Date')
plt.ylabel('Delay in Progress (in KM)')
plt.title('Project Delay Over Time')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.show()


# # Average Monthly Project Progress

# In[ ]:





# # Total Monthly Project Work Done

# In[48]:


# Calculate the total work done per month
monthly_total_work = data.groupby(['DATE'])['OVERALL PROGRESS DURING THIS MONTH(in KM)'].sum().reset_index()

plt.figure(figsize=(12, 6))

# Create a bar chart or line chart for total work done per month
sns.barplot(x='DATE', y='OVERALL PROGRESS DURING THIS MONTH(in KM)', data=monthly_total_work)

plt.xlabel('Month')
plt.ylabel('Total Work Done (in KM)')
plt.title('Total Monthly Project Work Done')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


# Visualization

# In[49]:


# Line Chart: Cumulative Progress Over Time
plt.figure(figsize=(10, 6))
plt.plot(data['DATE'], data['CUMULATIVE_PROGRESS'], marker='o')
plt.xlabel('Date')
plt.ylabel('Cumulative Progress (in KM)')
plt.title('Cumulative Project Progress Over Time')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()




# In[50]:


# Bar Chart: Average Monthly Progress
monthly_average_progress = data.groupby(['DATE'])['OVERALL PROGRESS DURING THIS MONTH(in KM)'].mean().reset_index()
plt.figure(figsize=(12, 6))
plt.bar(monthly_average_progress['DATE'], monthly_average_progress['OVERALL PROGRESS DURING THIS MONTH(in KM)'])
plt.xlabel('Month')
plt.ylabel('Average Progress (in KM)')
plt.title('Average Monthly Project Progress')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[51]:


# Bar Chart: Total Work Done by Tranche
total_work_per_tranche = data.groupby(['TRANCHE'])['OVERALL PROGRESS DURING THIS MONTH(in KM)'].sum().reset_index()
plt.figure(figsize=(10, 6))
plt.bar(total_work_per_tranche['TRANCHE'], total_work_per_tranche['OVERALL PROGRESS DURING THIS MONTH(in KM)'])
plt.xlabel('Tranche')
plt.ylabel('Total Work Done (in KM)')
plt.title('Total Project Work Done by Tranche')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




