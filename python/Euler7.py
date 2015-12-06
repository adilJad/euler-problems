
# coding: utf-8

# In[10]:

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


# In[12]:

i = 0
n=2
while i <= 10001:
    if isPrime(n):
        i+=1
        if i==10001:
            print i,n
    n+=1
    

