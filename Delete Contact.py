#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Delete Contact -----------------------------------------------------------------------------------------------------------------------

  elif choice == '3':
      delete_name = input("Enter the name you want to delete")
      found = False
      for contact in contact_list:
          if contact.name.lower() == delete_name.lower():
             contact_list.remove(contact)
              found =True

             print("Conatct deleted")
             break
          else:
              if not found:
                  print("Contact not found")

