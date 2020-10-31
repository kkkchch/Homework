# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 23:20:58 2020

@author: User
"""
print ("請選擇轉換模式:")
mode=input("a為華氏轉攝氏 b為相反")
tem=input("請輸入溫度:")
if (mode=="a"):
    ans1=(int(tem)-32)/(9/5)
    print ("攝氏",ans1,"度")
    
else:
        ans2=(int(tem)*(9/5)+32)
        print ("華氏",ans2,"度")


































