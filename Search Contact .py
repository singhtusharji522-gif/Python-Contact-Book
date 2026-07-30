#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Search Contact --------------------------------------------------------------------------------------------------------------------------

  elif choice == '4':
      search_name = input("Enter name = ")
      found = False
      for contact in contact_list:
          if contact.name.lower() == search_name.lower():
             print("\n------------------search Result--------------------")
             contact.display()
             found = True
             break
      if not found:
             print("\ncontact not found")


