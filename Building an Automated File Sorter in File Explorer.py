#!/usr/bin/env python
# coding: utf-8

# # Automatic file sorter in File Explorer

# In[22]:


import os, shutil


# In[23]:


path = r"D:/My stuff/Data Analyst/Python practise/"


# In[24]:


file_name = os.listdir(path)


# In[34]:


Folder_names = ['csv fies','image files','text files']

for loop in range(0,3):
    if not os.path.exists(path+ Folder_names[loop]):
        os.makedirs(path + Folder_names[loop])
        
for file in file_name:
    if ".csv" in file and not os.path.exists(path + "csv files/"+ file):
        shutil.move(path + file,path + "csv files/"+ file)
    elif ".png" in file and not os.path.exists(path + "image files/"+ file):
        shutil.move(path + file,path + "image files/"+ file)
    elif ".txt" in file and not os.path.exists(path + "text files/"+ file):
        shutil.move(path + file,path + "text files/"+ file)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




