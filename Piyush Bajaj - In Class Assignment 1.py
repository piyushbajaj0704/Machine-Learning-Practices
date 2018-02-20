x
# coding: utf-8

# In[2]:


import pandas as pd


# In[20]:


x = [[0,0,0],[0,1,0],[1,0,1],[1,1,0],[1,0,0],[1,1,1],[0,1,1],[0,0,1]]


# In[21]:


y = [1,1,0,1,1,0,0,0]


# In[22]:


X = pd.DataFrame(x,columns=['X1','X2','X3'])


# In[23]:


Y = pd.DataFrame(y,columns=['Y'])


# In[24]:


print(X)
print(Y)


# In[25]:


colX = X.columns[X.columns.str.startswith('X')]


# In[26]:


print(colX)


# In[27]:


colY = Y.columns[Y.columns.str.startswith('Y')]


# In[28]:


print(colY)


# In[36]:


from sklearn.model_selection import train_test_split


# In[37]:


X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.30)


# In[38]:


print(X_train)


# In[39]:


print(y_train)


# In[40]:


from sklearn.tree import DecisionTreeClassifier


# In[41]:


dtree = DecisionTreeClassifier()


# In[42]:


print(dtree.fit(X_train, y_train))


# In[43]:


print(dtree.predict(X_test))


# In[44]:


print(y_test)

