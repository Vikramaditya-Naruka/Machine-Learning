#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a = [1,2,3,4]
type(a)


# In[3]:


b = np.array(a)
b


# In[4]:


# !pip install numpy


# In[5]:


a = [[2,3,4],[234,56,7],[35,6,8]]
b = np.array(a)
b


# In[6]:


print("Total shape = ",b.shape)
print("Total dimension =", b.ndim)


# # pre-defined Functions in Numpy

# In[7]:


# (1). zeros() ==> by this function we can create an array with all the values zeros

a = np.zeros(5)
a


# In[8]:


a = np.zeros((3,3))
a


# In[9]:


a.ndim


# In[10]:


# (2). ones() ==> By this method we can create an array all the values is 1.

a = np.ones(5)
a


# In[11]:


a.ndim


# In[12]:


a  = np.ones((2,2))
a


# In[13]:


a.shape  # 2 rows and 2 columns


# In[14]:


a.ndim # for direction


# In[15]:


# (3). eye() ==> BY this method we can create an array in which diagonal elements
a = np.eye(3,4)
a


# In[16]:


a = np.eye(4,4)
print(a)
a.ndim


# In[17]:


# 4. diag() ==> 
a = np.diag([1,45,6,7,3,5,66])
a


# In[18]:


a.ndim


# # Random Module

# In[19]:


#5. Random Module

# (a). randint()
# a = np.random.ranint(min_number,max_number,total_elements)

a = np.random.randint(1,10,2)
a


# In[ ]:





# In[20]:


a,b,c = map(int,input().split())
d = np.random.randint(a,b,c)
d


# In[ ]:


#(b). rand() ==>  it will generate random numbers between 0 to 1

a = np.random.rand(5)
a


# In[ ]:


a = np.random.rand(2,3)
a


# In[ ]:


a.ndim


# In[ ]:


a.shape


# In[ ]:


a = np.random.rand(2,3,4)
a


# In[ ]:


print(a.ndim)
print(a.shape)


# In[ ]:


# Reshape ==>  n(rows)*n(columns) = n(Total_elements)
a = np.random.randint(1,60,12)
a


# In[ ]:


a.shape


# In[ ]:


a.ndim


# In[ ]:


a = a.reshape(2,6)
a


# In[ ]:


a = a.reshape(6,2)
a


# In[ ]:


a = a.reshape(3,4)
a


# In[21]:


a = a.reshape(4,3)
a


# In[22]:


a = a.reshape(1,12)
a


# In[23]:


a = a.reshape(12,1)
a


# # #Principal of -1 

# In[28]:


a = a.reshape(-1,2)
a


# In[29]:


a.shape


# In[30]:


a = a.reshape(4,-1)
a


# In[31]:


a.shape


# In[32]:


np.random.seed(20)
a = np.random.randint(1,10,3)
a


# In[33]:


np.random.seed(40)
a = np.random.randint(1,10,3)
a


# In[34]:


a = np.random.randn(5)
a


# In[35]:


a = np.array([1,2,3,4]).reshape(2,2)
b = np.array([5,6,7,8]).reshape(2,2)
c = a+b
d = a.dot(b)
print(c)
print(d)
e


# In[36]:


a = np.random.randint(5,6,12)
a


# In[37]:


a = a.reshape(3,4)
a


# In[38]:


a = a.reshape(2,6)
a


# In[39]:


a = a.reshape(6,2)
a


# In[40]:


a =[[5,5,5,5],[5,5,5,5],[5,5,5,5]]
b = np.array(a)
b


# 

# # View VS Copy

# In[41]:


# view  ==>
# copy ==> copy the data and make changes without any changes the original value


# In[42]:


a = np.array([10,20,40,50,50,50,30,55])
print(a)
b = a[3:6]
b


# In[43]:


b[:] = 0
print(b)
a


# In[44]:


a = np.array([10,20,40,50,50,50,30,55])
print(a)
b = a[3:6].copy()
b


# In[45]:


b[:] = 0
print(b)
a


# # Conditional Selection

# In[46]:


a = np.arange(20,21)
a


# In[47]:


a>10


# In[48]:


a<10


# In[49]:


b = a>10
print(b)
a[b]


# In[50]:


c = a<=10
a[c]


# In[51]:


a = np.arange(1,16)
b = a%2 == 0 
a[b]


# # Operations on Array

# In[52]:


a = np.arange(1,5)
a


# In[53]:


a+2


# In[54]:


a**2


# In[55]:


a


# In[56]:


a =a.reshape(2,2)
a


# In[57]:


b = np.array([5,6,7,8]).reshape(2,2)
b


# In[58]:


a+b


# In[59]:


a-b


# In[60]:


b-a


# In[61]:


a.dot(b)


# In[62]:


a/b


# In[63]:


a*b


# In[64]:


b/a


# In[65]:


c = np.array([10,23,57,0,7,4,])
# min ==> for minimum value
np.min(c)


# In[66]:


# for checking index of minimum value
np.argmin(c)


# In[67]:


# max ==> for maximum value
np.max(c)


# In[68]:


#for checking index of maximum value
np.argmax(c)


# In[69]:


# sqrt() ==> for square root 
np.sqrt(c)


# In[70]:


# sin() = sin@ values
np.sin(c)


# In[71]:


np.cos(c)


# In[72]:


np.tan(c)


# # linspace()

# In[73]:


# linspace() ==> this function returns vaues between a give =n range and with a same gap between consicutive elements
a = np.linspace(1,2,5)
a


# In[74]:


np.random.seed(19)
a = np.random.randint(1,21,9).reshape(3,3)
a


# In[75]:


np.sum(a)


# In[76]:


np.sum(a,axis = 1)


# In[77]:


np.sum(a,axis = 0)


# In[78]:


np.argmin(a)


# In[79]:


np.argmax(a)


# In[80]:


# sum the all elements step by step
# cumalitive sum of a,b,c,d  = a, a+b , a+b+c , a+b+c+d
np.cumsum(a)


# In[81]:


a


# # np.unique(arr,return_index = True , return_counts = True)
# 
# 1. The array with unique values
# 
# 2. the array with respective index value
# 
# 3. the array with counting of frequency

# In[82]:


a = np.array([10,23,4,5,1,2,3,123,1,2,3,1,2,3,5,5,6,6,78,])
np.unique(a , return_index = True , return_counts = True)


# # Horizontal and Vertical Stacking

# In[83]:


a = np.array([1,2,3,4])
b = np.array([5,6,7,8])


# In[84]:


np.hstack((a,b))


# In[85]:


np.vstack((a,b))


# # Questions

# In[86]:


#import the numpy

import numpy as np


# In[87]:


#create an array of 10 random integers

np.random.seed(19)
a = np.random.randint(1,10,10)
a


# In[88]:


#create an array of element of 10-20

b = np.arange(10,21)
b


# In[89]:


#create an array which contain value 5 , 10 times.

a = np.ones(10)+1
b = np.ones(10)+2
c = np.ones(10)+7
d = np.ones(10)+5
e = np.ones(10)+3
f = np.array([a,b,c,d,e])
f


# In[90]:


#create a one dimensional array and convert that into 3*3 matrix

a = np.array([[1,2,3,4,5,6,7,8,9]])
a.reshape(3,3)


# In[91]:


#create a 2D array of size 3*3 but all elements should be between 0 to 1.

a = np.random.randint(0,2,9).reshape((3,3))
print(a)
a.ndim


# In[92]:


#concatenate 2D array horizontally and vertically

a = np.array([2,3,35,4]).reshape((2,2))
b = np.array([2,3,35,4]).reshape((2,2))


# In[93]:


np.hstack((a,b))


# In[94]:


np.vstack((a,b))


# In[ ]:





# In[ ]:





# In[ ]:





# # A complete overview

# In[95]:


import pandas as pd
file = pd.read_csv("data.csv")
file


# In[96]:


file.info()


# In[97]:


file.describe()


# In[98]:


file['Value']


# In[99]:


file['Value'][0] = 2000


# In[100]:


file.head()


# In[101]:


file['Year'][2:5] = None


# In[102]:


file.head()


# In[103]:


file


# In[104]:


file.isnull()


# In[105]:


file.isnull().sum()


# In[106]:


file.dropna() #remove missing value


# In[107]:


df = file


# In[108]:


df


# In[109]:


file['Year'][2:5] = "2020"


# In[110]:


file.loc[1:10 , 'Year']               # [raw_range , column_name]


# In[111]:


file.loc[1:10 , ['Year','Units']]   


# In[112]:


df.iloc[1:10 , 1:3] # [raw_range , column_range_index]


# In[113]:


df.iloc[1:10 , [1,2,3]]


# # How to drop a column

# In[114]:


df.drop(columns = ['Year'],axis = 1)


# In[115]:


df.to_csv("new.csv",index = False) # save the data in file


# In[116]:


impo = df['Value'] > 50000
impo


# # How to upload our data

# In[ ]:


import pandas as pd 
df = pd.read_csv('placement.csv')
df


# In[ ]:


df.head(12)


# In[ ]:


df.tail(10)


# In[ ]:


df.describe()


# In[ ]:


df.info()


# In[ ]:


df  =df.rename(columns = {'cgpa': "percantage" , "resume_score": "score","placed": "place"})
df


# In[ ]:


g = df.filter(items = ['score','place'])
g


# In[ ]:


df.max()


# In[117]:


df.min()


# In[118]:


df.value_counts()


# In[119]:


df.count


# In[120]:


n = df.iloc[1:11,:3]
n


# In[121]:


df.axes


# In[122]:


df.dtypes


# In[123]:


df.empty


# In[124]:


df.ndim


# In[125]:


df.shape


# In[126]:


df.size


# In[127]:


df.values


# In[128]:


df.sort_values(by = 'score')


# In[ ]:


df.sort_index


# In[ ]:


df.abs()


# In[ ]:


df.sum()


# In[ ]:


from collections import Counter

my_list = [1, 2, 2, 3, 4, 4, 5]
counter = Counter(my_list)
unique_count = len(counter)  #Count of unique elements
unique_count

1.) difference between series and dataframe

2.) what is differnce between implace =True and implace = False

3.) what is difference between dropna vs fillna

4.) what is difference between pivot and pivot table

5.) what do you mean by groupby

6.) what is difference between crosstab and pivot table

7.) what does reset_index .why we use it reset_index

8.) how you get only values in your data frame


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




