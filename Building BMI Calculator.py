#!/usr/bin/env python
# coding: utf-8

# # BMI Calculator 

# In[18]:


name = input("Enter your name: ")

weight = int(input("Enter your weight in pounds: "))

height = int(input("Enter your height in inches: "))

BMI = (weight * 703) / (height * height)

print(BMI)

if BMI > 0:
    if(BMI<18.5):
        print(name + ",You are underweight.")
    elif (BMI<=24.9):
        print(name + ",You are normal weight.")
    elif (BMI<29.9):
        print(name + ",You are overweight.You need to exercise more and stop sitting and writing so many python tutorials")
    elif (BMI<34.9):
        print(name + ",You are obese.")
    elif (BMI<39.9):
        print(name + ",You are severely obese.")
    else :
        print(name + ",You are morbidly obese")
else:
    print("Enter the valid informations")


# In[ ]:





# In[ ]:





# In[ ]:


# Formula
BMI = (weight in pounds * 703) / (height in inches * height in inches)


# In[ ]:


# Informations

under 18.5  underweight  Minimal
18.5 - 24.9  Normal weight  Minimal
25 - 29.9  Overweight  Increased
30 - 34.9  Obese  High
35 - 39.9  Severly Obese  Very high
40 - over  Morbidly Obese  Extremely High


# In[ ]:





# In[ ]:





# In[ ]:


#Calculator

if BMI > 0:
    if(BMI<18.5):
        print(name + ",You are underweight.")
    elif (BMI<=24.9):
        print(name + ",You are normal weight.")
    elif (BMI<29.9):
        print(name + ",You are overweight.")
    elif (BMI<34.9):
        print(name + ",You are obese.")
    elif (BMI<39.9):
        print(name + ",You are severely obese.")
    else :
        print(name + ",You are morbidly obese")
else:
    print("Enter the valid informations")


# In[ ]:





# In[ ]:




