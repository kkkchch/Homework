# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 22:46:46 2020

@author: User
"""
print ("請輸入三個數字:a,b,c來判斷可否組成三角形")
a= input ("a")
b= input ("b")
c= input ("c")

if a+b>c:
    print (int(a)+int(b)+int(c))

elif a+c>b:
    print (int(a)+int(b)+int(c))

elif b+c>a:
    print (int(a)+int(b)+int(c))
    
else: 
    print("無法組成三角形")












