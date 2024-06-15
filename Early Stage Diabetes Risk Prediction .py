#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Importing the required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 


# In[3]:


#uploading the dataset
df = pd.read_csv("Dataset for Diabetes Prediction/diabetes_data_upload.csv")


# In[4]:


df 


# In[5]:


#Defining the column values
df.columns


# In[6]:


#list out name of the columns 
list(df.columns)


# In[7]:


#First 5 rows 
df.head()


# In[8]:


#Last 5 rows
df.tail()


# In[9]:


#get information as data types null values 
df.info()


# In[10]:


#describe given data 
#describe outliers 
#Box Plot 
df.describe()


# In[11]:


#Check the age count 
df["Age"].value_counts()


# In[12]:


#check whether Defined Function is not null or not ?
df.isnull()


# In[13]:


#In following categorial graph shows in males and females data who are going to have a risk of pre-diabetes in future 
fg = sns.catplot(x='Gender',y ='Age',data = df,aspect = 1,hue = 'class')
fg.set_xlabels("Risk of Pre-diabetes")


# In[14]:


#Group by the male and female count 
df.groupby(['Gender','Age'])['Gender'].count()


# In[15]:


#Group By the early symptoms of diabetes
symptoms=df.groupby(['Polyuria','Polydipsia','sudden weight loss','weakness','Polyphagia','Genital thrush','visual blurring','Itching','Irritability','delayed healing','partial paresis','muscle stiffness','Alopecia','Obesity','class'])['Gender'].count()


# In[16]:


sns.catplot(x='Gender',y ='Age',data =df,aspect=1.5)
plt.show()


# In[17]:


#checking max age until the risk of pre-diabetes is there 
df['Age'].max()


# In[18]:


#checking min age of risk of pre-dibetics is there 
df['Age'].min()


# In[19]:


symptoms


# In[22]:


#Reseting the symtoms 
symptoms = symptoms.reset_index(name='Symptoms')


# In[23]:


symptoms


# In[24]:


symptoms.plot(kind="bar")


# In[25]:


#Box Plot Representation
sns.boxplot(df['Age'])


# In[26]:


#Checking the outliers from that range
df[df['Age']==90]


# In[ ]:




