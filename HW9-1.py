# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 20:27:09 2020

@author: User
"""
abclist=[]
thing=2
while thing!="exit":
    thing= input("請輸入要購買的清單，結束購買請輸入exit:")
    if thing != "exit":
        abclist.append(thing)
        print (thing)
    else:
        print (abclist)

        


















