# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 23:01:46 2020

@author: User
"""
print("請輸入三個數字:")
a=input()
b=input()
c=input()
if int(a)>int(b)>int(c):
    print (a,b,c)
elif int(a)>int(c)>int(b):
    print (a,c,b)
elif int(b)>int(c)>int(a):
    print (b,c,a)
elif int(b)>int(a)>int(c):
    print (b,a,c)
elif int(c)>int(a)>int(b):
    print (c,a,b)
elif int(c)>int(b)>int(a):
    print (c,b,a)    
    