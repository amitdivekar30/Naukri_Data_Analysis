# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 19:33:14 2020

@author: aad
"""

import csv
from datetime import datetime
import pandas as pd
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time


driver = webdriver.Chrome('chromedriver.exe')

jobs={"roles":[],
     "companies":[],
     "locations":[],
     "experience":[],
     "salary":[],
     "skills":[],
     "Description":[],
     "Roles":[],
     "Education":[]}

for i in range(100):
    driver.get("https://www.naukri.com/data-scientist-jobs-in-india-{}".format(i))
    time.sleep(3)
    lst=driver.find_elements_by_css_selector(".jobTuple.bgWhite.br4.mb-8")
    
    links=[]
    for job in lst:
        driver.implicitly_wait(10)
        
        link= job.find_element_by_css_selector('a.title.fw500.ellipsis').get_attribute('href')
        links.append(link)
                
    for link in links:
        driver.get(link)
        time.sleep(3)
        lst1= driver.find_elements_by_css_selector("section.jd-header")
        lst2= driver.find_elements_by_css_selector("section.job-desc")
        for des in lst1:
            try:
                role=des.find_element_by_css_selector("h1.jd-header-title").text
            except:
                role='None'
            try:
                company=des.find_element_by_css_selector("a.pad-rt-8").text
            except:
                company='None'
            try:
                location=des.find_element_by_css_selector("div.loc").text
            except:
                location='None'
            try:
                exp=des.find_element_by_css_selector("div.exp").text
            except:
                exp='None'
            
            try:
                salary=des.find_element_by_css_selector("div.salary").text
            except:
                salary='None'
                
                
            jobs["roles"].append(role)
            jobs["companies"].append(company)
            jobs["locations"].append(location)
            jobs["experience"].append(exp)
            jobs["salary"].append(salary)
                
        for des1 in lst2:
            try:
                job_desc1=des1.find_element_by_css_selector("div.dang-inner-html").text
            except:
                job_desc1='None'
            try:    
                other_details=des1.find_element_by_css_selector("div.other-details").text
            except:
                other_details='None'
            try:
                education=des1.find_element_by_css_selector("div.education").text
            except:
                education='None'
            try:
                skills=des1.find_element_by_css_selector("div.key-skill").text
            except:
                skills='None'
                
            jobs["Description"].append(job_desc1)
            jobs["Roles"].append(other_details)
            jobs["Education"].append(education)
            jobs["skills"].append(skills)
            
ds=pd.DataFrame.from_dict(jobs)
ds.to_csv('naukri_data_df.csv')