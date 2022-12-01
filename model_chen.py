#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


df = pd.read_csv('train.csv')


# In[5]:


df["Fare"] = pd.to_numeric(df["Fare"])
df.dtypes


# In[6]:


df1 = df.drop(['Name','Ticket','Cabin','PassengerId','Embarked'],axis = 1)


# In[7]:


df1['Sex'] = df['Sex'].map({'male': 1, 'female': 0})
df1


# In[8]:


df2=df1.dropna()
df2


# In[9]:


df2.dtypes


# In[10]:


#génération du model
from sklearn.model_selection import train_test_split


# In[11]:


y = df2.Survived
x = df2.drop(['Survived'], axis = 1)

x_train,x_test, y_train, y_test = train_test_split(x,y,test_size = .2, random_state = 42)


# In[12]:


print (x_train.shape,x_test.shape)
print (df2.shape)


# In[13]:


print (y_train.sample(10))


# In[14]:


#create first model
from sklearn.ensemble import RandomForestClassifier


# In[15]:


# random_state = le hazard à 23
# max_features = le nombre de colonne selectionner par itération au hazard
# n_estimators nb d'arbre
rf = RandomForestClassifier(n_estimators = 100, random_state = 23, max_features = 2)


# In[16]:


rf.fit(X = x_train, y = y_train)


# In[ ]:




