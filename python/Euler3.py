
# coding: utf-8

# In[21]:

def isPrimeFactor(n):
    if n == 2:
        return True
    if n%2 == 0:
        return False
    r = int(n**(0.5))
    for i in range(3, r):
        if n%i == 0:
            return False
    
    return True


# In[27]:

isPrimeFactor(97)


# In[29]:

x = 600851475143
i = int(x**(0.5))
mf = 1
while(i >= 2):
    if x%i == 0:
        if isPrimeFactor(i):
            mf = i
            break
    i -= 1

print mf

