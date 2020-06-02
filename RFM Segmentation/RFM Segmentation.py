#!/usr/bin/env python
# coding: utf-8

# <h2 align='center'><a>RFM Segmentation </h2>

# In[ ]:


## Create a table that divide the Recency,Monetary and frequency parameter into 4 quardrants,Also 
## create two columns showing the 1-Status(Active,Risky,Churned), 2- Offers according the description in excel file. 


# In[1]:


import numpy as np
import pandas as pd


# In[2]:


import sys


# In[3]:


import os 

os.getcwd()


# In[4]:


os.chdir("D:\\Python\\Class")


# In[5]:


RFM_Value=pd.read_excel("DATA SET FOR RFM-VALUE BASED SEGMENTATION_AA.xls",sheet_name="Sheet1")


# In[6]:


RFM_Sheet=pd.read_excel("RFM_value.xlsx")
RFM_Sheet


# In[7]:


RFM_Sheet.head()


# In[8]:


RFM_Sheet.rename(index=lambda x:x+1)


# In[9]:


RFM_Sheet1=RFM_Sheet.rename(index= lambda x:x+1) ## index renaming
RFM_Sheet1


# In[10]:


RFM_Sheet1.head()


# In[11]:


RFM_Sheet['Q_Recency']=pd.qcut(RFM_Sheet.Recency,4,labels=['Q1','Q2','Q3','Q4'])
RFM_Sheet['Q_Recency'].head()


# In[12]:


RFM_Sheet['Q_Frequency']=pd.cut(RFM_Sheet.Frequency,[0,1,2,5,201],labels=['Q1','Q2','Q3','Q4'])
RFM_Sheet['Q_Frequency'].head()


# In[13]:


RFM_Sheet['Q_Monetary']=pd.qcut(RFM_Sheet.Monetary,4,labels=['Q1','Q2','Q3','Q4'])
RFM_Sheet['Q_Monetary'].head()


# In[14]:


RFM_Sheet2=RFM_Sheet.assign(Q_Recency=pd.qcut(RFM_Sheet.Recency,4,labels=['Q1','Q2','Q3','Q4']),
                            Q_Frequency=pd.cut(RFM_Sheet.Frequency,[0,1,2,5,201],labels=['Q1','Q2','Q3','Q4']),
                            Q_Monetary=pd.qcut(RFM_Sheet.Monetary,4,labels=['Q1','Q2','Q3','Q4']))


# In[15]:


RFM_Sheet2.head(10)


# In[16]:


RFM_Sheet2=RFM_Sheet.assign(Q_Recency=pd.qcut(RFM_Sheet.Recency,4,labels=['Q1','Q2','Q3','Q4']),
                            Q_Frequency=pd.qcut(RFM_Sheet.Frequency.rank(method='first'),4,labels=['Q1','Q2','Q3','Q4']),
                            Q_Monetary=pd.qcut(RFM_Sheet.Monetary,4,labels=['Q1','Q2','Q3','Q4']))
RFM_Sheet2.head(10)


# In[17]:


RFM_Sheet2['F']=pd.qcut(RFM_Sheet.Frequency.rank(method='first'),4,labels=[1,2,3,4])
RFM_Sheet2['M']=pd.qcut(RFM_Sheet.Monetary,4,labels=[1,2,3,4])
RFM_Sheet2['R']=pd.qcut(RFM_Sheet.Recency,4,labels=[1,2,3,4])


# In[18]:


RFM_Sheet2['F']


# In[19]:


RFM_Sheet2['M']


# In[20]:


RFM_Sheet2['R']


# In[21]:


RFM_Sheet2['RFM_Sheet2_Score']=RFM_Sheet2[['F','M']].sum(axis=1)
RFM_Sheet2['RFM_Sheet2_Score']


# In[22]:


def RFM_Sheet2_level(RFM_Sheet2):
    if RFM_Sheet2['RFM_Sheet2_Score']>=8:
        return 'Premium customer'
    elif((RFM_Sheet2['RFM_Sheet2_Score']>=6) & (RFM_Sheet2['RFM_Sheet2_Score']<=7)):
        return 'Gold customer'
    elif((RFM_Sheet2['RFM_Sheet2_Score']>=4) & (RFM_Sheet2['RFM_Sheet2_Score']<=5)):
        return 'Silver customer'
    else:
        return 'Required Activation'


# In[23]:


def RFM_Sheet2_status(RFM_Sheet2):
    if RFM_Sheet2['R']==1:
        return 'Active'
    elif((RFM_Sheet2['R']>=2) & (RFM_Sheet2['R']<=3)):
        return 'Risky'
    else:
        return 'Churend'


# In[24]:


RFM_Sheet2['RFM_Sheet2_Level'] =RFM_Sheet2.apply(RFM_Sheet2_level,axis=1)
RFM_Sheet2['RFM_Sheet2_Status'] =RFM_Sheet2.apply(RFM_Sheet2_status,axis=1)


# In[25]:


RFM_Sheet2


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




