
# coding: utf-8

# In[33]:

i = 1
s = 0
m = 0
while m < 1000:
    s += m
    m = i*3
    i+=1
    
i = 1
m = 0
while m < 1000:
    s += m
    if i%3 > 0:
        m = i*5
    else:
        m=0
    i+=1
        
print s


# In[22]:

s=0
for i in range(1,1000):
    if (i%3 == 0) or (i%5 == 0):
        s+=i
print s

