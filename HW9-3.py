# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 20:21:54 2020

@author: User
"""
num1=int(input("請輸入數字1:"))
num2=int(input("請輸入數字2:"))
n=2
abclist=[]
while 1<n <= num1 and 1<n<=num2:
    if num1%n==0 and num2%n==0:
     abclist.append(n)
     print (n)
     n+=1
    else:
        n+=1
print("最大公因數:",max(abclist))        