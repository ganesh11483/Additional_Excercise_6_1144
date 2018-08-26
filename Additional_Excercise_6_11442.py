
# coding: utf-8

# In[8]:


import numpy as np
import pandas as pd


# In[9]:


movies=pd.read_csv('C:\\Users\\Ganesh_Prasad2\\Downloads\\ml-20m\\ml-20m\\movies.csv')


# In[10]:


tags=pd.read_csv('C:\\Users\\Ganesh_Prasad2\\Downloads\\ml-20m\\ml-20m\\tags.csv')


# In[11]:


ratings=pd.read_csv('C:\\Users\\Ganesh_Prasad2\\Downloads\\ml-20m\\ml-20m\\ratings.csv')


# In[12]:


type(tags)


# In[13]:


tags


# In[14]:


tags['userId']


# In[15]:


type(tags['userId'])


# In[16]:


tags['userId'].describe()


# In[17]:


tags.iloc[0]


# In[18]:


tags.iloc[11]


# In[19]:


tags.iloc[2000]


# In[20]:


tags.index


# In[21]:


tags.columns


# In[22]:


ratings.describe()


# In[23]:


filter_rating=ratings.filter(items=['rating'])


# In[24]:


filter_rating.query('rating > 4')


# In[25]:


ratings.isnull().sum()


# In[26]:


tags.isnull().sum()


# In[27]:


movies.isnull().sum()


# In[28]:


generes = movies.filter(items=['genres'])


# In[29]:


df_filtered = movies[movies.genres == 'Animation']


# In[30]:


df_filtered


# In[31]:


ratings['rating'].mean()


# In[32]:


INNERJOIN = movies.merge(ratings,how='inner',on='movieId')


# In[33]:


INNERJOIN[INNERJOIN.genres == 'Comedy'].query('rating > 4').head()


# In[34]:


genresList=INNERJOIN['genres']


# In[35]:


genresList.str.split(pat='|')


# In[39]:


INNERJOIN['title'].str[-6:]


# In[56]:


INNERJOIN[pd.to_datetime(INNERJOIN['timestamp'],unit='s') > '2015-02-01']


# In[65]:


tags.sort_values(['timestamp'],ascending=True)

