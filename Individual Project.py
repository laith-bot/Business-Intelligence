#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd
Location = "C:/Laith's Documents/ISM 4402/datasets/axisdata.csv"
df = pd.read_csv(Location)

df.head()


# In[24]:


#1. Average cars sold per month

df_mean = df["Cars Sold"].mean()

df_mean


# In[25]:


#2. Max cars sold per month

df_max = df["Cars Sold"].max()

df_max


# In[26]:


#3. Min cars sold per month

df_min = df["Cars Sold"].min()

df_min


# In[27]:


#4. Average cars sold per month by gender

NumFour = df['Cars Sold'].groupby(df['Gender'])

NumFour.mean()


# In[28]:


#5. Average hours worked by people selling more than three cars per month

cars = df['Cars Sold'] > 3

cars

df_cars = df[cars]

df_cars["Hours Worked"].mean()


# In[29]:


#6. Average years of experience

Exp_mean = df["Years Experience"].mean()

Exp_mean


# In[30]:


#7. Average years of experience for people selling more than three cars per month

#based on #5 Code

df_cars["Years Experience"].mean()


# In[31]:


#8. Average cars sold per month sorted by whether they have had sales training

ST = df['SalesTraining'] == 'Y'

ST

df_ST = df[ST]

df_ST["Cars Sold"].mean()


# In[32]:


import matplotlib.pyplot as plt

Visual1 = df['Cars Sold'].groupby(df['SalesTraining'])

Visual1.count().plot(kind='bar')


# In[42]:


Visual2 = df['Cars Sold'].groupby(df['Years Experience'])

Visual2.count().plot(kind='bar')


# In[ ]:





# In[ ]:




