# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 21:04:11 2021

@author: User
"""
result=5
def adding():
    print(a+b)

def minoring():
    print(a-b)
    
def multiplying():
    print(a*b)
    
def modifying():
    print(a/b)
    


a=int(input('請輸入第一個數值:'))
b=int(input('請輸入第二個數值:'))
print("1為相加 2為相減 3為相乘 4為相除")
choice=5
while choice:
    
    choice=input("請輸入動作選項:")
    if choice =="1":
        adding()
    if choice=="2":
        minoring()   

    if choice=="3":
        multiplying()  
        
    if choice=="4":
        modifying()
    break