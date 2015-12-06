
# coding: utf-8

# In[2]:

def isPrime(n):
    if n == 2:
        return True
    if n%2 == 0:
        return False
    r = int(n**(0.5))
    for i in range(3, r+1):
        if n%i == 0:
            return False
    
    return True


# In[ ]:

s = 0
for i in range(2,2000000):
    if isPrime(i):
        s += i
print s

