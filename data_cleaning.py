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
df = df[df['Salary Estimate'] != '-1']
df = df[~df['Salary Estimate'].str.contains('Employer Provided Salary')]

##We are going to add estimates as their own columns to make things easier, these will be in thousands
salary= df['Salary Estimate'].apply(lambda x: x.split("(")[0])
salary = salary.str.replace("$",'').str.replace("K",'')

df['Salary Estimate'] = salary
df['Salary Estimate'] = salary

salary_split = salary.str.split("-", n = 1, expand = True) 

df['min_salary'] = salary_split[0]
df['max_salary'] = salary_split[1]
df['average_salary'] = salary_split.astype(float).mean(axis=1)


##Lets start categorizing our jobs


##Lets parse our the titles
def title_parser(title):
    if "data scientist" in title.lower():
        return "data scientist"
    elif "analyst" in title.lower():
        return "analyst"
    elif "machine learning" in title.lower():
        return "mle"
    elif "researcher" in title.lower():
        return "researcher"
    elif "manager" in title.lower():
        return "manager"
    elif "director" in title.lower():
        return "director"
    else: 
        return "na"
    
df["simplified_title"] = df["Job Title"].apply(lambda x: title_parser(x))
df.simplified_title.value_counts()

def seniority_parser(title):
    if 'sr' in title.lower() or 'senior' in title.lower() or 'sr' in title.lower() or 'lead' in title.lower() or 'principal' in title.lower():
        return 'senior' 
    elif 'jr' in title.lower() or 'jr.' in title.lower() or 'junior' in title.lower() or 'associate' in title.lower():
        return 'junior'
    else:
        return 'na'
df['seniority'] = df['Job Title'].apply(lambda x: seniority_parser(x))
df.seniority.value_counts()

def state_parser(loc):
    split = loc.split(",")
    if( 'Los Angeles' in loc):
        return ' CA'
    elif( 'Maryland' in loc):
        return ' MD'
    elif( 'Missouri' in loc):
        return ' MO'
    elif( 'Utah' in loc):
        return ' UT'
    elif( 'Illinois' in loc):
        return 'IL'
    elif( 'New Jersey' in loc):
        return ' NJ'
    elif( 'Colorado' in loc):
        return ' CO'
    elif( 'California' in loc):
        return ' CA'
    elif(len(split) >1):
        return split[1]
    elif('United States' in loc):
        return ' na'
    else: return split[0]
df['State']= df['Location'].apply(lambda x: state_parser(x))
df['State'].value_counts()

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
df['r_count'] = df['Job Description'].apply(lambda x: 1 if ' r ' in x.lower() else 0)
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



