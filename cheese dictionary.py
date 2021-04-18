#!/usr/bin/env python
# coding: utf-8

# In[1]:


Cheese=[3,2,5,6,7,3,2]
Name=['Max','Felix','Alex','Vivan','Ethan','Justine','Troy']

dic = {Name[i]: Cheese[i] for i in range (len(Name))}

print ("The resulting dictionary is: " + str(dic))

