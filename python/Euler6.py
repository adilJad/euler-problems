
# coding: utf-8

# In[1]:

s1 = 0
s2 = 0
r = 0
for i in range(1,101):
    s1 += i
    s2 += i**2
r = (s1**2) - s2

print r

