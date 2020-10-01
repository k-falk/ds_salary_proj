# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 16:43:44 2020

@author: Xkfal
"""

import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/Xkfal/Documents/ds_salary_proj/chromedriver"
df1 = gs.get_jobs('data scientist', 300, False , path, 30)

df2 = gs.get_jobs('data scientist', 300, False , path, 30)

df3 = gs.get_jobs('data scientist', 300, False , path, 30)

df = pd.concat([df1,df2,df3])

df.to_csv('C:/Users/Xkfal/Documents/ds_salary_proj/job_data.csv')
df = pd.read_csv('C:/Users/Xkfal/Documents/ds_salary_proj/job_data.csv')