
# coding: utf-8

# In[3]:

f1 = 1
f2 = 2
f = 0
s=2
while f < 4000000:
    f = f2 + f1
    f1 = f2
    f2 = f
    if f%2 == 0:
        s += f
print s

