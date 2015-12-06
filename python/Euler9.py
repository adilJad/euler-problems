
# coding: utf-8

# In[7]:

a = 0
b = 0
c = 0
cont = True
while a<1000:
    a += 1
    b=1
    while b <= a:
        b += 1
        c = 1000 - (a+b)
        x = a**2 + b**2
        if x == c**2:
            cont = False
            break
    if not cont:
        break

print a, b, c, a**2, b**2, c**2, a+b+c, a*b*c

