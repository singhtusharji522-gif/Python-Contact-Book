#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Contact:
  def __init__(self,name,phone_number):
     self.name = name
     self.phone_number = phone_number

  def display(self):
    print("Name = ",self.name,"\nPhone number = ",self.phone_number)

