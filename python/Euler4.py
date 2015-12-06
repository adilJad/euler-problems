
# coding: utf-8

# In[83]:

def isPalindromic(n):
    p = True
    s = str(n)
    m = int(len(s) / 2)
    l = len(s) - 1
    for i in range(0,m):
        if s[i] != s[l-i]:
            p = False
            break
    return p


# In[88]:

isPalindromic(906609)


# In[99]:

i=999
j=999
m=0
maxpal=0
br = False
while (i >= 100):
    j=999
    while (j >= 100):  
        m = i*j
        if isPalindromic(m):
            if m > maxpal:
                maxpal = m
        j=j-1
    i=i-1
print maxpal

