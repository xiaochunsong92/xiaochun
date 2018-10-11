#!/usr/bin/env python 
# -*- coding: UTF-8 -*-
#---------------------------------------------------------
#Project Name: Chinese Name Score
#Version:      v1.0
#Data:         2018/10/06
#Author:       Peter 
#Contact;      xiaochunsong92@163.com
#Copyright:    2018 TianShuiSong LTD. All rights reserved
#---------------------------------------------------------
import re
import sxtwl 
import requests
import time 
from bs4 import BeautifulSoup
Detail = 0
lunar = sxtwl.Lunar()
WX = {'木': 0, '火': 0, '土': 0, '金': 0, '水': 0}
Gan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
Zhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
ShX = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]
ymc = ["十一", "十二", "正", "二", "三", "四", "五", "六", "七", "八", "九", "十" ]
rmc = ["初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十", "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "二十", "廿一", "廿二", "廿三", "廿四", "廿五", "廿六", "廿七", "廿八", "廿九", "三十", "卅一"]

def analyze():
    bazi = []
    shuge_tongji = []
    B = re.match(r'(\d\d\d\d)(\d)(\d)(\d)(\d)(\d)(\d)',birthday)
    total_score = 100
    if B:
        Y = B.group(1)
        if B.group(2) == '0':
            M = B.group(3)
        else: 
            M = B.group(2) + B.group(3)
        if B.group(4) == '0':
            D = B.group(5)
        else: 
            D = B.group(4) + B.group(5)
        if B.group(6) == '0':
            H = B.group(7)
        else:
            H = B.group(6) + B.group(7)
    age = int(current_year) - int(Y) 
    day = lunar.getDayBySolar(int(Y), int(M), int(D))
    gz = lunar.getShiGz(int(D), int(H))
    ytg = Gan[day.Lyear2.tg]
    ydz = Zhi[day.Lyear2.dz]
    mtg = Gan[day.Lmonth2.tg]
    mdz = Zhi[day.Lmonth2.dz]
    dtg = Gan[day.Lday2.tg]
    ddz = Zhi[day.Lday2.dz]
    htg = Gan[gz.tg]
    hdz = Zhi[gz.dz]
    bazi.append(ytg) 
    bazi.append(ydz) 
    bazi.append(mtg) 
    bazi.append(mdz) 
    bazi.append(dtg) 
    bazi.append(ddz) 
    bazi.append(htg) 
    bazi.append(hdz) 
    for i in range(len(bazi)):
        x = bazi[i]
        if x == "甲" or x == "乙" or x == "寅" or x == "卯": 
            WX['木'] += 1
        if x == "丁" or x == "丙" or x == "巳" or x == "午":
            WX['火'] += 1
        if x == "戊" or x == "己" or x == "辰" or x == "丑" or x == "戌" or x == "未":
            WX['土'] += 1
        if x == "庚" or x == "辛" or x == "申" or x == "酉":
            WX['金'] += 1
        if x == "壬" or x == "癸" or x == "亥" or x == "子":
            WX['水'] += 1
    # Analyze name wuxing according to Kangxizidian 
    if fuxing == 0 and fuming == 0:
        keywords = {'wd':last_name}
        keywords1 = {'wd':first_name}
        url = 'http://tool.httpcn.com/KangXi/So.asp'
        r = requests.post(url, data = keywords)
        r.endcoding = 'utf-8'
        r1 = requests.post(url, data = keywords1)
        r1.endcoding = 'utf-8'
        kangxi_result = r.content.decode(r.endcoding)
        kangxi_result1 = r1.content.decode(r1.endcoding)
        soup = BeautifulSoup(kangxi_result, "html.parser")
        soup1 = BeautifulSoup(kangxi_result1, "html.parser")
        #print (soup.find(string=re.compile(u"汉字五行：")))
        kangxi_wx = soup.find(string=re.compile(u"汉字五行："))
        kangxi_bihua = soup.find(string=re.compile(u"康熙笔画："))
        kangxi_wx = re.match(u".*?汉字五行：(.)", kangxi_wx)
        kangxi_bihua = re.match(u".*?康熙笔画：(.)", kangxi_bihua)
        if kangxi_wx:
            kangxi_wx = kangxi_wx.group(1)
        if kangxi_bihua:
            kangxi_bihua = kangxi_bihua.group(1)
        kangxi_wx1 = soup1.find(string=re.compile(u"汉字五行："))
        kangxi_bihua1 = soup1.find(string=re.compile(u"康熙笔画："))
        kangxi_wx1 = re.match(u".*?汉字五行：(.)", kangxi_wx1)
        kangxi_bihua1 = re.match(u".*?康熙笔画：(.)", kangxi_bihua1)
        if kangxi_wx1:
            kangxi_wx1 = kangxi_wx1.group(1)
        if kangxi_bihua1:
            kangxi_bihua1 = kangxi_bihua1.group(1)
        # Calculate shuliwuge 
        tiange = int(kangxi_bihua) + 1
        dige = int(kangxi_bihua1) + 1 
        renge = int(kangxi_bihua) + int(kangxi_bihua1)
        waige = 2
        zongge = int(kangxi_bihua) + int(kangxi_bihua1)
        shugemingli = open('wugeshuli', 'r')
        shugemingli = shugemingli.readlines()
        print('吕十大师五行八字分析')
        print('您的名字: %s %s' %(last_name, first_name))
        print('您的阳历生日: %s' %birthday) 
        print('您的农历生日: %s %s' %(ymc[day.Lmc],rmc[day.Ldi]))
        print('您的生辰八字: %s %s %s %s %s %s %s %s' %(Gan[day.Lyear2.tg], Zhi[day.Lyear2.dz], Gan[day.Lmonth2.tg], Zhi[day.Lmonth2.dz], Gan[day.Lday2.tg], Zhi[day.Lday2.dz], Gan[gz.tg], Zhi[gz.dz]))
        print('您的生辰五行: 金 %s 木 %s 水 %s 火 %s 土 %s' %(WX['金'], WX['木'], WX['水'], WX['火'], WX['土']))
        print('您的名字五行: %s: %s %s: %s' %(last_name, kangxi_wx, first_name, kangxi_wx1))
        print('您的名字五行分析:' )
        for i in WX:
            if (kangxi_wx == i) and (WX[i] == 0):
                print('您的姓 "%s" 大吉，完美补充了您生辰八字里缺的 "%s" ' %(last_name, i))
            elif (kangxi_wx == i) and (WX[i] == 1):
                print('您的姓 "%s" 中吉，您的生辰八字 "%s" 只有1需要补一补' %(last_name, i))
            elif (kangxi_wx == i) and ((WX[i] == 2) or (WX[i] == 3) or (WX[i] == 4)):  
                print('您的姓 "%s" 小吉，您的生辰八字 "%s" 已经够了，不需要再补了。' %(last_name, i))
        for i in WX:
            if (kangxi_wx1 == i) and (WX[i] == 0):
                print('您的名 "%s" 大吉，完美补充了您生辰八字里缺的 "%s" ' %(first_name, i))
            elif (kangxi_wx1 == i) and (WX[i] == 1):
                print('您的名 "%s" 中吉，您的生辰八字 "%s" 只有1需要补一补' %(first_name, i))
            elif (kangxi_wx1 == i) and ((WX[i] == 2) or (WX[i] == 3) or (WX[i] == 4)):  
                print('您的名 "%s" 小吉，您的生辰八字 "%s" 已经够了，不需要再补了。' %(first_name, i))
        for i in WX:
            if (kangxi_wx == i):
                WX[i] += 1 
            if (kangxi_wx1 == i):
                WX[i] += 1 
        for i in WX:
            if WX[i] == 0:
                total_score -= 6
            if WX[i] == 1:
                total_score -= 3
    if fuxing == 1 and fuming == 0:
        keywords = {'wd':last_name_1}
        keywords0 = {'wd':last_name_2}
        keywords1 = {'wd':first_name}
        url = 'http://tool.httpcn.com/KangXi/So.asp'
        r = requests.post(url, data = keywords)
        r.endcoding = 'utf-8'
        r0 = requests.post(url, data = keywords0)
        r0.endcoding = 'utf-8'
        r1 = requests.post(url, data = keywords1)
        r1.endcoding = 'utf-8'
        kangxi_result = r.content.decode(r.endcoding)
        kangxi_result0 = r0.content.decode(r0.endcoding)
        kangxi_result1 = r1.content.decode(r1.endcoding)
        soup = BeautifulSoup(kangxi_result, "html.parser")
        soup0 = BeautifulSoup(kangxi_result0, "html.parser")
        soup1 = BeautifulSoup(kangxi_result1, "html.parser")
        #print (soup.find(string=re.compile(u"汉字五行：")))
        kangxi_wx = soup.find(string=re.compile(u"汉字五行："))
        kangxi_bihua = soup.find(string=re.compile(u"康熙笔画："))
        kangxi_wx = re.match(u".*?汉字五行：(.)", kangxi_wx)
        kangxi_bihua = re.match(u".*?康熙笔画：(.)", kangxi_bihua)
        if kangxi_wx:
            kangxi_wx = kangxi_wx.group(1)
        if kangxi_bihua:
            kangxi_bihua = kangxi_bihua.group(1)
        kangxi_wx0 = soup0.find(string=re.compile(u"汉字五行："))
        kangxi_bihua0 = soup0.find(string=re.compile(u"康熙笔画："))
        kangxi_wx0 = re.match(u".*?汉字五行：(.)", kangxi_wx0)
        kangxi_bihua0 = re.match(u".*?康熙笔画：(.)", kangxi_bihua0)
        if kangxi_wx0:
            kangxi_wx0 = kangxi_wx0.group(1)
        if kangxi_bihua0:
            kangxi_bihua0 = kangxi_bihua0.group(1)
        kangxi_wx1 = soup1.find(string=re.compile(u"汉字五行："))
        kangxi_bihua1 = soup1.find(string=re.compile(u"康熙笔画："))
        kangxi_wx1 = re.match(u".*?汉字五行：(.)", kangxi_wx1)
        kangxi_bihua1 = re.match(u".*?康熙笔画：(.)", kangxi_bihua1)
        if kangxi_wx1:
            kangxi_wx1 = kangxi_wx1.group(1)
        if kangxi_bihua1:
            kangxi_bihua1 = kangxi_bihua1.group(1)
        # Calculate shuliwuge 
        tiange = int(kangxi_bihua) + int(kangxi_bihua0)
        dige = int(kangxi_bihua1) + 1 
        renge = int(kangxi_bihua0) + int(kangxi_bihua1)
        waige = int(kangxi_bihua) + 1
        zongge = int(kangxi_bihua) + int(kangxi_bihua0) + int(kangxi_bihua1)
        shugemingli = open('wugeshuli', 'r')
        shugemingli = shugemingli.readlines()
        print('吕十大师五行八字分析')
        print('您的名字: %s %s' %(last_name, first_name))
        print('您的阳历生日: %s' %birthday) 
        print('您的农历生日: %s %s' %(ymc[day.Lmc],rmc[day.Ldi]))
        print('您的生辰八字: %s %s %s %s %s %s %s %s' %(Gan[day.Lyear2.tg], Zhi[day.Lyear2.dz], Gan[day.Lmonth2.tg], Zhi[day.Lmonth2.dz], Gan[day.Lday2.tg], Zhi[day.Lday2.dz], Gan[gz.tg], Zhi[gz.dz]))
        print('您的生辰五行: 金 %s 木 %s 水 %s 火 %s 土 %s' %(WX['金'], WX['木'], WX['水'], WX['火'], WX['土']))
        print('您的名字五行: %s: %s %s: %s %s: %s' %(last_name_1, kangxi_wx, last_name_2, kangxi_wx0, first_name, kangxi_wx1))
        print('您的名字五行分析:' )
        for i in WX:
            if (kangxi_wx == i) and (WX[i] == 0):
                print('您的姓 "%s" 大吉，完美补充了您生辰八字里缺的 "%s" ' %(last_name_1, i))
            elif (kangxi_wx == i) and (WX[i] == 1):
                print('您的姓 "%s" 中吉，您的生辰八字 "%s" 只有1需要补一补' %(last_name_1, i))
            elif (kangxi_wx == i) and ((WX[i] == 2) or (WX[i] == 3) or (WX[i] == 4)):  
                print('您的姓 "%s" 小吉，您的生辰八字 "%s" 已经够了，不需要再补了。' %(last_name_1, i))
        for i in WX:
            if (kangxi_wx0 == i) and (WX[i] == 0):
                print('您的姓 "%s" 大吉，完美补充了您生辰八字里缺的 "%s" ' %(last_name_2, i))
            elif (kangxi_wx0 == i) and (WX[i] == 1):
                print('您的姓 "%s" 中吉，您的生辰八字 "%s" 只有1需要补一补' %(last_name_2, i))
            elif (kangxi_wx0 == i) and ((WX[i] == 2) or (WX[i] == 3) or (WX[i] == 4)):  
                print('您的姓 "%s" 小吉，您的生辰八字 "%s" 已经够了，不需要再补了。' %(last_name_2, i))
        for i in WX:
            if (kangxi_wx1 == i) and (WX[i] == 0):
                print('您的名 "%s" 大吉，完美补充了您生辰八字里缺的 "%s" ' %(first_name, i))
            elif (kangxi_wx1 == i) and (WX[i] == 1):
                print('您的名 "%s" 中吉，您的生辰八字 "%s" 只有1需要补一补' %(first_name, i))
            elif (kangxi_wx1 == i) and ((WX[i] == 2) or (WX[i] == 3) or (WX[i] == 4)):  
                print('您的名 "%s" 小吉，您的生辰八字 "%s" 已经够了，不需要再补了。' %(first_name, i))
        for i in WX:
            if (kangxi_wx == i):
                WX[i] += 1 
            if (kangxi_wx0 == i):
                WX[i] += 1 
            if (kangxi_wx1 == i):
                WX[i] += 1 
        for i in WX:
            if WX[i] == 0:
                total_score -= 6
            if WX[i] == 1:
                total_score -= 3
    if fuxing == 1 and fuming == 1:
        keywords = {'wd':last_name_1}
        keywords0 = {'wd':last_name_2}
        keywords1 = {'wd':first_name_1}
        keywords2 = {'wd':first_name_2}
        url = 'http://tool.httpcn.com/KangXi/So.asp'
        r = requests.post(url, data = keywords)
        r.endcoding = 'utf-8'
        r0 = requests.post(url, data = keywords0)
        r0.endcoding = 'utf-8'
        r1 = requests.post(url, data = keywords1)
        r1.endcoding = 'utf-8'
        r2 = requests.post(url, data = keywords2)
        r2.endcoding = 'utf-8'
        kangxi_result = r.content.decode(r.endcoding)
        kangxi_result0 = r0.content.decode(r0.endcoding)
        kangxi_result1 = r1.content.decode(r1.endcoding)
        kangxi_result2 = r2.content.decode(r1.endcoding)
        soup = BeautifulSoup(kangxi_result, "html.parser")
        soup0 = BeautifulSoup(kangxi_result0, "html.parser")
        soup1 = BeautifulSoup(kangxi_result1, "html.parser")
        soup2 = BeautifulSoup(kangxi_result2, "html.parser")
        #print (soup.find(string=re.compile(u"汉字五行：")))
        kangxi_wx = soup.find(string=re.compile(u"汉字五行："))
        kangxi_bihua = soup.find(string=re.compile(u"康熙笔画："))
        kangxi_wx = re.match(u".*?汉字五行：(.)", kangxi_wx)
        kangxi_bihua = re.match(u".*?康熙笔画：(.)", kangxi_bihua)
        if kangxi_wx:
            kangxi_wx = kangxi_wx.group(1)
        if kangxi_bihua:
            kangxi_bihua = kangxi_bihua.group(1)
        kangxi_wx0 = soup0.find(string=re.compile(u"汉字五行："))
        kangxi_bihua0 = soup0.find(string=re.compile(u"康熙笔画："))
        kangxi_wx0 = re.match(u".*?汉字五行：(.)", kangxi_wx0)
        kangxi_bihua0 = re.match(u".*?康熙笔画：(.)", kangxi_bihua0)
        if kangxi_wx0:
            kangxi_wx0 = kangxi_wx0.group(1)
        if kangxi_bihua0:
            kangxi_bihua0 = kangxi_bihua0.group(1)
        kangxi_wx1 = soup1.find(string=re.compile(u"汉字五行："))
        kangxi_bihua1 = soup1.find(string=re.compile(u"康熙笔画："))
        kangxi_wx1 = re.match(u".*?汉字五行：(.)", kangxi_wx1)
        kangxi_bihua1 = re.match(u".*?康熙笔画：(.)", kangxi_bihua1)
        if kangxi_wx1:
            kangxi_wx1 = kangxi_wx1.group(1)
        if kangxi_bihua1:
            kangxi_bihua1 = kangxi_bihua1.group(1)
        kangxi_wx2 = soup2.find(string=re.compile(u"汉字五行："))
        kangxi_bihua2 = soup2.find(string=re.compile(u"康熙笔画："))
        kangxi_wx2 = re.match(u".*?汉字五行：(.)", kangxi_wx2)
        kangxi_bihua2 = re.match(u".*?康熙笔画：(.)", kangxi_bihua2)
        if kangxi_wx2:
            kangxi_wx2 = kangxi_wx2.group(1)
        if kangxi_bihua2:
            kangxi_bihua2 = kangxi_bihua2.group(1)
        # Calculate shuliwuge 
        tiange = int(kangxi_bihua) + int(kangxi_bihua0)
        dige = int(kangxi_bihua1) + int(kangxi_bihua2) 
        renge = int(kangxi_bihua0) + int(kangxi_bihua1)
        waige = int(kangxi_bihua) + int(kangxi_bihua2)
        zongge = int(kangxi_bihua) + int(kangxi_bihua0) + int(kangxi_bihua1) + int(kangxi_bihua2)
        shugemingli = open('wugeshuli', 'r')
        shugemingli = shugemingli.readlines()
        print('吕十大师五行八字分析')
        print('您的名字: %s %s' %(last_name, first_name))
        print('您的阳历生日: %s' %birthday) 
        print('您的农历生日: %s %s' %(ymc[day.Lmc],rmc[day.Ldi]))
        print('您的生辰八字: %s %s %s %s %s %s %s %s' %(Gan[day.Lyear2.tg], Zhi[day.Lyear2.dz], Gan[day.Lmonth2.tg], Zhi[day.Lmonth2.dz], Gan[day.Lday2.tg], Zhi[day.Lday2.dz], Gan[gz.tg], Zhi[gz.dz]))
        print('您的生辰五行: 金 %s 木 %s 水 %s 火 %s 土 %s' %(WX['金'], WX['木'], WX['水'], WX['火'], WX['土']))
        print('您的名字五行: %s: %s %s: %s %s: %s %s: %s' %(last_name_1, kangxi_wx, last_name_2, kangxi_wx0, first_name_1, kangxi_wx1, first_name_2, kangxi_wx2))
        print('您的名字五行分析:' )
        for i in WX:
            if (kangxi_wx == i) and (WX[i] == 0):
                print('您的姓 "%s" 大吉，完美补充了您生辰八字里缺的 "%s" ' %(last_name_1, i))
            elif (kangxi_wx == i) and (WX[i] == 1):
                print('您的姓 "%s" 中吉，您的生辰八字 "%s" 只有1需要补一补' %(last_name_1, i))
            elif (kangxi_wx == i) and ((WX[i] == 2) or (WX[i] == 3) or (WX[i] == 4)):  
                print('您的姓 "%s" 小吉，您的生辰八字 "%s" 已经够了，不需要再补了。' %(last_name_1, i))
        for i in WX:
            if (kangxi_wx0 == i) and (WX[i] == 0):
                print('您的姓 "%s" 大吉，完美补充了您生辰八字里缺的 "%s" ' %(last_name_2, i))
            elif (kangxi_wx0 == i) and (WX[i] == 1):
                print('您的姓 "%s" 中吉，您的生辰八字 "%s" 只有1需要补一补' %(last_name_2, i))
            elif (kangxi_wx0 == i) and ((WX[i] == 2) or (WX[i] == 3) or (WX[i] == 4)):  
                print('您的姓 "%s" 小吉，您的生辰八字 "%s" 已经够了，不需要再补了。' %(last_name_2, i))
        for i in WX:
            if (kangxi_wx1 == i) and (WX[i] == 0):
                print('您的名 "%s" 大吉，完美补充了您生辰八字里缺的 "%s" ' %(first_name_1, i))
            elif (kangxi_wx1 == i) and (WX[i] == 1):
                print('您的名 "%s" 中吉，您的生辰八字 "%s" 只有1需要补一补' %(first_name_1, i))
            elif (kangxi_wx1 == i) and ((WX[i] == 2) or (WX[i] == 3) or (WX[i] == 4)):  
                print('您的名 "%s" 小吉，您的生辰八字 "%s" 已经够了，不需要再补了。' %(first_name_1, i))
        for i in WX:
            if (kangxi_wx2 == i) and (WX[i] == 0):
                print('您的名 "%s" 大吉，完美补充了您生辰八字里缺的 "%s" ' %(first_name_2, i))
            elif (kangxi_wx2 == i) and (WX[i] == 1):
                print('您的名 "%s" 中吉，您的生辰八字 "%s" 只有1需要补一补' %(first_name_2, i))
            elif (kangxi_wx2 == i) and ((WX[i] == 2) or (WX[i] == 3) or (WX[i] == 4)):  
                print('您的名 "%s" 小吉，您的生辰八字 "%s" 已经够了，不需要再补了。' %(first_name_2, i))
        for i in WX:
            if (kangxi_wx == i):
                WX[i] += 1 
            if (kangxi_wx0 == i):
                WX[i] += 1 
            if (kangxi_wx1 == i):
                WX[i] += 1 
            if (kangxi_wx2 == i):
                WX[i] += 1 
        for i in WX:
            if WX[i] == 0:
                total_score -= 6
            if WX[i] == 1:
                total_score -= 3
    if fuxing == 0 and fuming == 1:
        keywords = {'wd':last_name}
        keywords1 = {'wd':first_name_1}
        keywords2 = {'wd':first_name_2}
        url = 'http://tool.httpcn.com/KangXi/So.asp'
        r = requests.post(url, data = keywords)
        r.endcoding = 'utf-8'
        r1 = requests.post(url, data = keywords1)
        r1.endcoding = 'utf-8'
        r2 = requests.post(url, data = keywords2)
        r2.endcoding = 'utf-8'
        kangxi_result = r.content.decode(r.endcoding)
        kangxi_result1 = r1.content.decode(r1.endcoding)
        kangxi_result2 = r2.content.decode(r1.endcoding)
        soup = BeautifulSoup(kangxi_result, "html.parser")
        soup1 = BeautifulSoup(kangxi_result1, "html.parser")
        soup2 = BeautifulSoup(kangxi_result2, "html.parser")
        #print (soup.find(string=re.compile(u"汉字五行：")))
        kangxi_wx = soup.find(string=re.compile(u"汉字五行："))
        kangxi_bihua = soup.find(string=re.compile(u"康熙笔画："))
        kangxi_wx = re.match(u".*?汉字五行：(.)", kangxi_wx)
        kangxi_bihua = re.match(u".*?康熙笔画：(.)", kangxi_bihua)
        if kangxi_wx:
            kangxi_wx = kangxi_wx.group(1)
        if kangxi_bihua:
            kangxi_bihua = kangxi_bihua.group(1)
        kangxi_wx1 = soup1.find(string=re.compile(u"汉字五行："))
        kangxi_bihua1 = soup1.find(string=re.compile(u"康熙笔画："))
        kangxi_wx1 = re.match(u".*?汉字五行：(.)", kangxi_wx1)
        kangxi_bihua1 = re.match(u".*?康熙笔画：(.)", kangxi_bihua1)
        if kangxi_wx1:
            kangxi_wx1 = kangxi_wx1.group(1)
        if kangxi_bihua1:
            kangxi_bihua1 = kangxi_bihua1.group(1)
        kangxi_wx2 = soup2.find(string=re.compile(u"汉字五行："))
        kangxi_bihua2 = soup2.find(string=re.compile(u"康熙笔画："))
        kangxi_wx2 = re.match(u".*?汉字五行：(.)", kangxi_wx2)
        kangxi_bihua2 = re.match(u".*?康熙笔画：(.)", kangxi_bihua2)
        if kangxi_wx2:
            kangxi_wx2 = kangxi_wx2.group(1)
        if kangxi_bihua2:
            kangxi_bihua2 = kangxi_bihua2.group(1)
        # Calculate shuliwuge 
        tiange = int(kangxi_bihua) + 1
        dige = int(kangxi_bihua1) + int(kangxi_bihua2) 
        renge = int(kangxi_bihua) + int(kangxi_bihua1)
        waige = int(kangxi_bihua2) + 1
        zongge = int(kangxi_bihua) + int(kangxi_bihua1) + int(kangxi_bihua2)
        shugemingli = open('wugeshuli', 'r')
        shugemingli = shugemingli.readlines()
        print('吕十大师五行八字分析')
        print('您的名字: %s %s' %(last_name, first_name))
        print('您的阳历生日: %s' %birthday) 
        print('您的农历生日: %s %s' %(ymc[day.Lmc],rmc[day.Ldi]))
        print('您的生辰八字: %s %s %s %s %s %s %s %s' %(Gan[day.Lyear2.tg], Zhi[day.Lyear2.dz], Gan[day.Lmonth2.tg], Zhi[day.Lmonth2.dz], Gan[day.Lday2.tg], Zhi[day.Lday2.dz], Gan[gz.tg], Zhi[gz.dz]))
        print('您的生辰五行: 金 %s 木 %s 水 %s 火 %s 土 %s' %(WX['金'], WX['木'], WX['水'], WX['火'], WX['土']))
        print('您的名字五行:  %s: %s %s: %s %s: %s' %(last_name, kangxi_wx, first_name_1, kangxi_wx1, first_name_2, kangxi_wx2))
        print('您的名字五行分析:' )
        for i in WX:
            if (kangxi_wx == i) and (WX[i] == 0):
                print('您的姓 "%s" 大吉，完美补充了您生辰八字里缺的 "%s" ' %(last_name, i))
            elif (kangxi_wx == i) and (WX[i] == 1):
                print('您的姓 "%s" 中吉，您的生辰八字 "%s" 只有1需要补一补' %(last_name, i))
            elif (kangxi_wx == i) and ((WX[i] == 2) or (WX[i] == 3) or (WX[i] == 4)):  
                print('您的姓 "%s" 小吉，您的生辰八字 "%s" 已经够了，不需要再补了。' %(last_name, i))
        for i in WX:
            if (kangxi_wx1 == i) and (WX[i] == 0):
                print('您的名 "%s" 大吉，完美补充了您生辰八字里缺的 "%s" ' %(first_name_1, i))
            elif (kangxi_wx1 == i) and (WX[i] == 1):
                print('您的名 "%s" 中吉，您的生辰八字 "%s" 只有1需要补一补' %(first_name_1, i))
            elif (kangxi_wx1 == i) and ((WX[i] == 2) or (WX[i] == 3) or (WX[i] == 4)):  
                print('您的名 "%s" 小吉，您的生辰八字 "%s" 已经够了，不需要再补了。' %(first_name_1, i))
        for i in WX:
            if (kangxi_wx2 == i) and (WX[i] == 0):
                print('您的名 "%s" 大吉，完美补充了您生辰八字里缺的 "%s" ' %(first_name_2, i))
            elif (kangxi_wx2 == i) and (WX[i] == 1):
                print('您的名 "%s" 中吉，您的生辰八字 "%s" 只有1需要补一补' %(first_name_2, i))
            elif (kangxi_wx2 == i) and ((WX[i] == 2) or (WX[i] == 3) or (WX[i] == 4)):  
                print('您的名 "%s" 小吉，您的生辰八字 "%s" 已经够了，不需要再补了。' %(first_name_2, i))
        for i in WX:
            if (kangxi_wx == i):
                WX[i] += 1 
            if (kangxi_wx1 == i):
                WX[i] += 1 
            if (kangxi_wx2 == i):
                WX[i] += 1 
        for i in WX:
            if WX[i] == 0:
                total_score -= 6
            if WX[i] == 1:
                total_score -= 3
    print('您的数格命理: %s: %s %s: %s %s: %s %s: %s %s: %s' %('天格', tiange, '地格', dige, '人格', renge, '外格', waige, '总格', zongge))
    print('您的数格命理分析:')
    print('天格:')
    for i in range(len(shugemingli)):
        a = shugemingli[i]
        tiange_jiedu = re.match(str(tiange) + '(\D)(.*)', a)
        if tiange_jiedu:
            tiange_jiedu1 = tiange_jiedu.group(1) 
            tiange_jiedu2 = tiange_jiedu.group(2) 
            shuge_tongji.append(tiange_jiedu2)
            print (tiange_jiedu1 + tiange_jiedu2)
            if Detail:
                #print (tiange_jiedu1 + tiange_jiedu2)
                print (shugemingli[i+1],end="")
                print (shugemingli[i+2],end="")
                print (shugemingli[i+3],end="")
                print (shugemingli[i+4],end="")

    print('地格:')
    for i in range(len(shugemingli)):
        a = shugemingli[i]
        dige_jiedu = re.match(str(dige) + '(\D)(.*)', a)
        if dige_jiedu:
            dige_jiedu1 = dige_jiedu.group(1) 
            dige_jiedu2 = dige_jiedu.group(2) 
            shuge_tongji.append(dige_jiedu2)
            print (dige_jiedu1 + dige_jiedu2)
            if Detail:
                #print (dige_jiedu1 + dige_jiedu2)
                print (shugemingli[i+1],end="")
                print (shugemingli[i+2],end="")
                print (shugemingli[i+3],end="")
                print (shugemingli[i+4],end="")
    print('人格:')
    for i in range(len(shugemingli)):
        a = shugemingli[i]
        renge_jiedu = re.match(str(renge) + '(\D)(.*)', a)
        if renge_jiedu:
            renge_jiedu1 = renge_jiedu.group(1) 
            renge_jiedu2 = renge_jiedu.group(2) 
            shuge_tongji.append(renge_jiedu2)
            print (renge_jiedu1 + renge_jiedu2)
            if Detail:
                #print (renge_jiedu1 + renge_jiedu2)
                print (shugemingli[i+1],end="")
                print (shugemingli[i+2],end="")
                print (shugemingli[i+3],end="")
                print (shugemingli[i+4],end="")
    print('外格:')
    for i in range(len(shugemingli)):
        a = shugemingli[i]
        waige_jiedu = re.match(str(waige) + '(\D)(.*)', a)
        if waige_jiedu:
            waige_jiedu1 = waige_jiedu.group(1) 
            waige_jiedu2 = waige_jiedu.group(2) 
            shuge_tongji.append(waige_jiedu2)
            print (waige_jiedu1 + waige_jiedu2)
            if Detail:
                #print (waige_jiedu1 + waige_jiedu2)
                print (shugemingli[i+1],end="")
                print (shugemingli[i+2],end="")
                print (shugemingli[i+3],end="")
                print (shugemingli[i+4],end="")
    print('总格:')
    for i in range(len(shugemingli)):
        a = shugemingli[i]
        zongge_jiedu = re.match(str(zongge) + '(\D)(.*)', a)
        if zongge_jiedu:
            zongge_jiedu1 = zongge_jiedu.group(1) 
            zongge_jiedu2 = zongge_jiedu.group(2) 
            shuge_tongji.append(zongge_jiedu2)
            print (zongge_jiedu1 + zongge_jiedu2)
            if Detail:
                #print (zongge_jiedu1 + zongge_jiedu2)
                print (shugemingli[i+1],end="")
                print (shugemingli[i+2],end="")
                print (shugemingli[i+3],end="")
                print (shugemingli[i+4],end="")
    # Calculate wugeshuli score
    for i in range(len(shuge_tongji)):
        if shuge_tongji[i] == '凶':
            total_score -= 3
        if shuge_tongji[i] == '半':
            total_score -= 1
    print('您的姓名最终得分:', total_score)
    print('您的运势分析:')
    if age < 100:
        print('事业: 千里之行始于足下，您的事业还没有开始，脚踏实地的做好现在的每一件事，在%s年之后会有一次大运，把握好机会，可保10年基本面，是下一步提升阶级的重要基础。错过此次大运，只有除有贵人相助，否则难以追赶。' %str(19 - age))
        print('财富: 小富之家，30岁之前衣食无忧，不用操心。30岁之后，如事业有成，可保中晚年平安。如事业五大的建树，家庭婚姻会出现2-3次危机，会有5年左右的波折期间，顺利趟过，可保晚年安详。生活中易多结交慷慨之士，乐善好施，积攒福保，方可免于常年劳逸奔波之苦。')
        print('爱情: 真正的爱情还未到来，最多只是懵懂的初恋，请珍惜爱过的每一个人，虽然她不是和你享受走过一生的人，但是至少在最美的时候遇见你。')
        print('子孙: 考虑子孙为时尚早，积累自身福报，子孙自然享福。')
        print('官运: 如进入体制内需贵人相助，否则虽可保一世平安，但难有更大成就。在工作中需谨言慎行，大嘴巴会耽误你的升迁。 ')
if __name__=='__main__':
    print('天水讼姓名测试系统')
    print('北京天水讼科技有限公司荣誉出品') 
    # Default setting
    last_name  = '王科' 
    first_name = '木讼'
    birthday   = '2011010102'
    sex        = '男'
    last_name_l = []
    first_name_l = []
    fuxing = 0
    fuming = 0
    current_time = time.strftime("%Y%m%d%H%M%S",time.localtime())
    current_year = time.strftime("%Y",time.localtime())
    if len(last_name) == 2:
        fuxing = 1 
        for i in last_name:
            last_name_l.append(i) 
        last_name_1 =  last_name_l[0]
        last_name_2 =  last_name_l[1]
    if len(last_name) > 2:
        print("not support!")   
    if len(first_name) == 2:
        fuming = 1 
        for i in first_name:
            first_name_l.append(i) 
        first_name_1 = first_name_l[0]
        first_name_2 = first_name_l[1]
    if len(first_name) > 2:
        print("not support!")   
    #Real test 
    #last_name  = input('您的姓:')
    #first_name = input('您的名:')
    #birthday   = input('您的生日:')
    #sex        = input('您是先生还是女士:')
    analyze()

