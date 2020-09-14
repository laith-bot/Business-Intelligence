#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
from sqlalchemy import create_engine
db_file = r"C:/Laith's Documents/ISM 4402/datasets/salesdata.db"
engine = create_engine(r"sqlite:///{}"
 .format(db_file))
sql = "select name from sqlite_master"
"where type = 'table';"
sales_data_df = pd.read_sql(sql, engine)
sales_data_df


# In[3]:


get_ipython().run_line_magic('pinfo', 'sales_data_df.read_sql')


# In[16]:


sql = "select name from sqlite_master""where type = 'table';"


# In[ ]:




