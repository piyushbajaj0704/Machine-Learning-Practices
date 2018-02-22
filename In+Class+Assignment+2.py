
# coding: utf-8

# In[1]:


from sklearn import datasets


# In[2]:


wine = datasets.load_wine()


# In[9]:


print(wine.feature_names)


# In[10]:


wine


# In[12]:


from sklearn.datasets import load_wine


# In[13]:


X, Y = load_wine(return_X_y=True)


# In[14]:


type(X)


# In[15]:


type(Y)


# In[16]:


X.ndim


# In[17]:


Y.ndim


# In[18]:


X.shape


# In[19]:


Y.shape


# In[21]:


from sklearn.model_selection import train_test_split


# In[22]:


X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.30, random_state=1)


# In[23]:


from sklearn.tree import DecisionTreeClassifier


# In[24]:


dtree = DecisionTreeClassifier()


# In[25]:


print(dtree.fit(X_train, y_train))


# In[28]:


print(dtree.predict(X_test))


# In[66]:


y_pred_train = dtree.predict(X_train)


# In[67]:


y_pred_test = dtree.predict(X_test)


# In[68]:


from sklearn.metrics import accuracy_score


# In[71]:


print('Accuracy: %.2f' % accuracy_score(y_test, y_pred_test))


# In[72]:


print('Accuracy: %.2f' % accuracy_score(y_train, y_pred_train))


# In[46]:


from sklearn.ensemble import BaggingClassifier


# In[47]:


tree = DecisionTreeClassifier(criterion='gini', random_state=100, max_depth=None)


# In[49]:


bag = BaggingClassifier(base_estimator=tree, n_estimators=100, max_samples=1.0, max_features=4, bootstrap=True, 
                        bootstrap_features=False, n_jobs=1, random_state=1)


# In[74]:


bag_fit_pred_train = bag.predict(X_train)


# In[75]:


print(bag_fit_pred_train)


# In[76]:


bag_fit_pred_test = bag_fit.predict(X_test)


# In[77]:


print(bag_fit_pred_test)


# In[78]:


print('Accuracy: %.2f' % accuracy_score(y_test, bag_fit_pred_test))


# In[79]:


print('Accuracy: %.2f' % accuracy_score(y_train, y_pred_train))

