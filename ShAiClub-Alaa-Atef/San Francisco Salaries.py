#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv(r"E:\Python\PythonDatasets\Salaries.csv")
data


# # Data Exploration

# In[3]:


data.head()


# In[4]:


data.columns


# In[6]:


data.columns.value_counts()


# In[7]:


data.size


# In[8]:


data.index


# In[11]:


# The number of rows and columns in the dataset
data.shape


# In[10]:


#Checking data types for each column
data.dtypes


# In[13]:


# Checking for the missing values in each column
data.isnull().sum()


# In[14]:


data.info()


# In[16]:


#Dropping Empty columns ('Notes', 'Status')
data.drop(['Notes', 'Status'], axis=1, inplace=True)


# In[17]:


data.describe()


# # Data Cleaning

# In[20]:


#Remove the negative values in columns
series_list = ['BasePay', 'OvertimePay', 'OtherPay', 'TotalPay','TotalPayBenefits','Benefits']
for series in series_list:
    data=data[data[series]>=0]


# In[21]:


data


# In[33]:


#handling missing values
#remove empty cells
data['Benefits'].fillna(0,inplace=True)
data['BasePay'].fillna(0,inplace=True)
data.dropna(inplace = True)


# In[34]:


data.isnull().sum()


# In[35]:


#replacing not provided values in each column to NAN value 
series_list = ['EmployeeName','JobTitle','BasePay', 'OvertimePay', 'OtherPay', 'Benefits','TotalPay','TotalPayBenefits']
for series in series_list:
    for x in data.index:
        if data.loc[x, series]=='Not Provided':
             data.loc[x, series] =pd.NaT


# In[40]:


#remove empty cell in 'EmployeeName' column
data['EmployeeName'].fillna(0,inplace=True)


# In[41]:


data[data.columns].isnull().sum()


# # Descriptive Statistics

# In[22]:


#Finding Mean , Median , Mode
data.describe()


# In[23]:


#Minimum value of total_salary('TotalPay')
min_salary = data['TotalPay'].min()
min_salary


# In[24]:


#Maximum value of total_salary('TotalPay')
max_salary = data['TotalPay'].max()
max_salary


# In[25]:


#Range of salaries
range_salary = max_salary - min_salary
range_salary


# In[28]:


#Calculating Mean
data['TotalPay'].mean()


# In[31]:


#Calculating Mode
data['TotalPay'].mode()[0]


# In[30]:


#Calculating Median
data['TotalPay'].median()


# In[26]:


#Standard Ddeviation  of 'TotalPay'
data['TotalPay'].std()


# In[27]:


#Standard Ddeviation  of 'BasePay'
data['BasePay'].std()


# In[49]:


data.head()


# # Basic Data Visualization

# In[54]:


#Histogram
data.plot.hist()


# # Pie Chart

# In[64]:


# grouping the data by department
departments = data['JobTitle'].value_counts()

plt.figure(figsize=(10, 8))
plt.pie(departments, labels=departments.index, autopct='%1.1f%%', startangle=140)
plt.title('Proportion of Employees in different departments')
plt.axis('equal')
plt.show()


# # Grouped Analysis

# In[68]:


data.groupby(['JobTitle']).agg('mean', 'median','min', 'max')


# In[70]:


data.groupby(['JobTitle']).agg({
    'TotalPay': ['mean', 'median', 'min', 'max'],
    'Year': ['mean', 'median', 'min', 'max']
})


# In[91]:


data.groupby(['JobTitle']).agg({
    'TotalPay': ['mean', 'median', 'min', 'max'],
    'Year': ['mean', 'median', 'min', 'max']
}).sort_values(by=('TotalPay', 'mean'), ascending=False)


# In[72]:


# grouping the data by 'JobTitle' and calculate the average salary for each group
average_salaries = data.groupby('JobTitle')['TotalPay'].mean()
average_salaries


# # Simple Correlation Analysis

# In[74]:


data.head()


# In[76]:


data['BasePay'].corr(data['Year'])


# In[77]:


data['TotalPay'].corr(data['Year'])


# In[78]:


data['BasePay'].corr(data['TotalPay'])  #High correlation


# In[80]:


data['BasePay'].corr(data['Benefits']) #High correlation


# In[81]:


data['BasePay'].corr(data['OvertimePay'])


# In[82]:


data['BasePay'].corr(data['OtherPay'])


# In[83]:


data['TotalPay'].corr(data['Benefits'])


# # Scatter Plot

# In[84]:


#visualizing the relationships
data.plot.scatter(x = 'BasePay', y = 'TotalPay', s=100, c = 'red')


# In[85]:


#visualizing the relationships
data.plot.scatter(x = 'BasePay', y = 'Benefits', s=100, c = 'yellow')


# In[87]:


#visualizing the relationships
data.plot.scatter(x = 'Benefits', y = 'TotalPay', s=100, c = 'blue')

