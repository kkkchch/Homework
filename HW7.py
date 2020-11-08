# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 00:21:07 2020

@author: User
"""
#要把字串print出來時 在字串內容之後加 .upper() 的話，英文字會變成大寫
str0= "abcde"
print(str0.upper())

#要把字串print出來時 在字串內容之後加 .lower() 的話，英文字會變成小寫
str1= "ABCDE"
print(str1.lower())

#要把字串print出來時 在字串內容之後加 .title() 的話，第一個字會變成大寫
str2= "defg"
print(str2.title())

#要把字串print出來時 在字串內容之後加 .swapcase() 的話，字串大小寫會互換
str3= "ApPlepIE"
print(str3.swapcase())

#要把字串print出來時 在其後加.rstrip() ，將刪除尾端多餘的空白
str4= "applepie       "
print(str4.rstrip(),"Hi")

#若要刪除字串開始端多餘的空白 則在print字串後加.lstrip()
str5="      applepie"
print(str5.lstrip())

#刪除頭尾兩端多於空白則用.strip()
str6="         applepie            "
print(str6.strip())

#要使字串在指定寬度中致中對齊 則使用.center(寬度)
print(str2.center(20))

#向右對齊則為 .rjust(寬度)
print(str2.rjust(20))

#向左則為 .ljust(寬度)
print(str2.ljust(20))

#向右對齊，左邊空格補0 使用.zfill(數值)
print(str2.zfill(20))

























