# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 16:43:44 2020

@author: Xkfal
"""

import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/Xkfal/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist', 15, False , path, 5)

df