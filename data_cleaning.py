# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 00:27:25 2020

@author: Xkfal
"""
import pandas as pd

df = pd.read_csv("job_data.csv")

## Couple of things we need to do here to clean data
## We need to remove rows that are no longer shown on glassdoor ie: headquarters and competitors
## Then we need to fix some things with our data ie: fix company name
## Then we will make our data a little more useful to us
df1 = df



df.head()

#Remove unneeded columns
df = df.drop_duplicates()

df = df.drop("Headquarters", axis=1)
df = df.drop("Competitors", axis=1)
df = df.drop(df.columns[0], axis=1)
df = df.drop_duplicates()
##Fix Company Name
df['Company Name'] = df['Company Name'].str.replace('\d+', '')
df['Company Name'] = df['Company Name'].str[:-1]

##Change Years founded to Age

df['Age'] = 2020 - pd.to_numeric(df['Founded'])
df.Age = df.Age.replace({2021: 0})


##Drop Jobs with no salary estimaate because they are useless to us
df = df[df['Salary Estimate'] != 1]

##We are going to add estimates as their own columns to make things easier, these will be in thousands
salary= df['Salary Estimate'].apply(lambda x: x.split("(")[0])
salary = salary.str.replace("$",'').str.replace("K",'')
df['Salary Estimate'] = salary
df['Salary Estimate'] = salary
salary = salary.str.split("-", n = 1, expand = True) 
df['minSalary'] = salary[0]
df['maxSalary'] = salary[1]

## We should look into job description now

##python
df['python_count'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df['python_count'].value_counts()
##java
df['java_count'] = df['Job Description'].apply(lambda x: 1 if 'java' in x.lower() else 0)
df['java_count'].value_counts()
##sql
df['sql_count'] = df['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() else 0)
df['sql_count'].value_counts()
##R
df['python_count'] = df['Job Description'].apply(lambda x: 1 if ' r ' in x.lower() else 0)
df['python_count'].value_counts()
##spark
df['spark_count'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df['spark_count'].value_counts()
##aws
df['aws_count'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df['aws_count'].value_counts()

df['excel_count'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df['excel_count'].value_counts()

df.to_csv('clean_data.csv', index = False)
df_in = pd.read_csv('clean_data.csv')



