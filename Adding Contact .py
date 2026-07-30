#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Adding Contact--------------------------------------------------------------------------------------------------------------------

 if choice == '1':
     print("----------Add contact------------")
     name = input("Enter Name")
     phone_number = input("Enter Phone number")

     new_contact = Contact(name,phone_number)
     contact_list.append(new_contact)

     print("\nContact Added Sucessfully")
     #break

