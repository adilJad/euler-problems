
# coding: utf-8

# In[7]:

r = 1
yes = False
for i in range(1,21):
    if r%i != 0:
        for j in range(2,i+1):
            m = r*j
            if m%i==0:
                r=m
                break
print r

