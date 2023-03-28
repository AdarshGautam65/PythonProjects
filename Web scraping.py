#!/usr/bin/env python
# coding: utf-8

# # Amazon Web scraping
# 

# In[1]:


# import libraries

from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime


# In[10]:


# Connect to your website

URL = 'https://www.amazon.in/DUDEME-Programmer-Coding-Developer-T-Shirt/dp/B08SF4HF9J/ref=sr_1_1?keywords=data+science+t+shirt&qid=1679223859&sprefix=on+data+t-s%2Caps%2C222&sr=8-1'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

title = soup2.find(id='productTitle').get_text()

T2 = soup2.find(id='bylineInfo').get_text()

print(title)
print(T2)



# In[13]:


title = title.strip()
T2 = T2.strip()

print(title)
print(T2)


# In[25]:


import datetime

today = datetime.date.today()

print(today)


# In[38]:


import csv

header = ['title','T2','data']
data = [title, T2, today]

with open('Amazonwebscrapper.csv','w', newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


# In[40]:


import pandas as pd

df = pd.read_csv(r'C:\Users\grace\Desktop\Amazonwebscrapper.csv')

print(df)


# In[36]:


# Now we are appending data to csv

with open('Amazonwebscrapper.csv','a+', newline='',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[43]:


def check_price():
    URL = 'https://www.amazon.in/DUDEME-Programmer-Coding-Developer-T-Shirt/dp/B08SF4HF9J/ref=sr_1_1?keywords=data+science+t+shirt&qid=1679223859&sprefix=on+data+t-s%2Caps%2C222&sr=8-1'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

    title = soup2.find(id='productTitle').get_text()

    T2 = soup2.find(id='bylineInfo').get_text()
    
    title = title.strip()
    T2 = T2.strip()
    
    import datetime
    
    today = datetime.date.today()
    
    import csv

    header = ['title','T2','data']
    data = [title, T2, today]
    
    with open('Amazonwebscrapper.csv','a+', newline='',encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
        
    

    


# In[53]:


while(True):
    check_price()
    time.sleep(5)


# In[54]:


import pandas as pd

df = pd.read_csv(r'C:\Users\grace\Desktop\Amazonwebscrapper.csv')

print(df)


# In[ ]:




