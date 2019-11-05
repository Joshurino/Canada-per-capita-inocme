#!/usr/bin/env python
# coding: utf-8

# In[26]:


#import different library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model


# In[27]:


#dataframe to read data
df=pd.read_csv("canada_per_capita_income.csv")
df


# In[40]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.xlabel('Year')
plt.ylabel('per capita income (US$))')
plt.scatter(df.year,df.income,color="green",marker="+")
plt.plot(df.year,reg.predict(df[['year']]),color="blue")


# In[29]:


reg=linear_model.LinearRegression()
reg.fit(df[['year']],df.income)


# In[30]:


#Predict per capita income for year 2017
reg.predict([[2017]])


# In[31]:


reg.predict([[2020]])


# In[32]:


reg.coef_


# In[33]:


reg.intercept_


# In[34]:


#y=mx+c where m=coefficient and c=intercept
828.46507522*2020-1632210.7578554575


# In[37]:


new_income=pd.read_csv("income_data.csv")
new_income


# In[38]:


new_income.head(3)


# In[44]:


p=reg.predict(new_income)
p


# In[45]:


new_income['inocme']=p
new_income


# In[46]:


new_income.to_csv("final_income.csv")


# In[ ]:




