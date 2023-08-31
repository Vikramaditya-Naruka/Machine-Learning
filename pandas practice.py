#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd 


# In[2]:


df = pd.read_csv("C:\\Users\\saurabh\\Desktop\\Newdat\\placement.csv")


# In[ ]:


df


# In[ ]:


df.head()   # top 5 data


# In[ ]:


df.tail() # bottom 5 data 


# In[ ]:


df.describe()  # statically view of data 


# In[ ]:


df.info() # Data type information 


# In[ ]:


top_left_corner_df = df.iloc[:5 , :3]  # iloc[row_range , column_range]
top_left_corner_df


# In[ ]:


s =   df.axes
s


# In[ ]:


p = df.dtypes
p


# In[ ]:


b = df.empty
b


# In[ ]:


i = df.ndim   #number of axes (it is 2) 
i


# In[ ]:


t = df.shape  # shape = n(rows) * n(columns) 
t


# In[ ]:


d = df.size          # row count * column count 
d


# In[ ]:


a = df.values    # get a numpy array for df 
a


# In[ ]:


df = df.copy() 


# In[ ]:


p = df.sort_values(by = 'resume_score')
p


# In[ ]:


r = df.sort_index() 
r


# In[ ]:


x = df.astype(int)        # type conversion 
x


# In[ ]:


s = df.abs() 
s


# In[ ]:


t = df.add(4) 
t


# In[ ]:


s = df.count() 
s


# In[ ]:


p = df.max() 
p


# In[ ]:


q = df.min() 
q


# In[ ]:


r = df.mean() 
r


# In[ ]:


s = df.median() 
s


# In[ ]:


s = df.sum() 
s


# In[ ]:


g = df.filter(items = ['cgpa' , 'placed'])
g


# In[ ]:


s = df.filter(items = [5,6] , axis = 0)
s


# In[ ]:


t = df.filter(like = '5' , axis = 0)
t


# In[ ]:


s = df.to_dict()    # save in dictionary 


# In[ ]:


q = df.to_string()    # save in string


# In[ ]:


idx = df.columns


# In[ ]:


label = df.columns[0]  # first column label 
label


# In[ ]:


p = df.columns.tolist()    # list of column labels 
p


# In[ ]:


q = df.columns.values    # array of column labels
q


# In[ ]:


p = df.rename(columns = {'cgpa':'half_yearly_marks' , 'resume_score':'semester_marks'})  # How to rename a column
p


# In[ ]:


s =p.columns = ['cgpa' , 'resume_score' , 'placed']
s


# In[ ]:


df['half'] = df['cgpa'].where(df['cgpa']>50 , other = 0)
df.head(10)


# In[ ]:


st = df['cgpa'].astype(int)   # Data type conversion 
# st


# In[ ]:





# In[ ]:





# In[ ]:




