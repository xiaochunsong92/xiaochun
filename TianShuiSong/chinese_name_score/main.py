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
from bs4 import BeautifulSoup
lunar = sxtwl.Lunar()
WX = {'木': 0, '火': 0, '土': 0, '金': 0, '水': 0}
Gan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
Zhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
ShX = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]
ymc = ["十一", "十二", "正", "二", "三", "四", "五", "六", "七", "八", "九", "十" ]
rmc = ["初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十", "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "二十", "廿一", "廿二", "廿三", "廿四", "廿五", "廿六", "廿七", "廿八", "廿九", "三十", "卅一"]

def analyze():
    bazi = []
    B = re.match(r'(\d\d\d\d)(\d)(\d)(\d)(\d)(\d)(\d)',birthday)
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
    #for i in range(len(shugemingli)):
    #    a = shugemingli[i]
    #    tiange_jiedu = re.match(str(tiange) + '(\D.*)', a)
    #    if tiange_jiedu:
    #        tiange_jiedu = tiange_jiedu.group(1) 
    #        print (tiange_jiedu)
    #        print (shugemingli[i+1])
    #        print (shugemingli[i+2])
    #        print (shugemingli[i+3])
    #        print (shugemingli[i+4])
    print('吕十大师五行八字分析')
    print('您的名字: %s %s' %(last_name, first_name))
    print('您的阳历生日: %s' %birthday) 
    print('您的农历生日: %s %s' %(ymc[day.Lmc],rmc[day.Ldi]))
    print('您的生辰八字: %s %s %s %s %s %s %s %s' %(Gan[day.Lyear2.tg], Zhi[day.Lyear2.dz], Gan[day.Lmonth2.tg], Zhi[day.Lmonth2.dz], Gan[day.Lday2.tg], Zhi[day.Lday2.dz], Gan[gz.tg], Zhi[gz.dz]))
    print('您的生辰五行: 金 %s 木 %s 水 %s 火 %s 土 %s' %(WX['金'], WX['木'], WX['水'], WX['火'], WX['土']))
    print('您的名字五行: %s: %s %s: %s' %(last_name, kangxi_wx, first_name, kangxi_wx1))
    print('您的数格命理: %s: %s %s: %s %s: %s %s: %s %s: %s' %('天格', tiange, '地格', dige, '人格', renge, '外格', waige, '总格', zongge))
    print('您的数格命理分析:')
    print('天格:')
    for i in range(len(shugemingli)):
        a = shugemingli[i]
        tiange_jiedu = re.match(str(tiange) + '(\D.*)', a)
        if tiange_jiedu:
            tiange_jiedu = tiange_jiedu.group(1) 
            print (tiange_jiedu)
            print (shugemingli[i+1],end="")
            print (shugemingli[i+2],end="")
            print (shugemingli[i+3],end="")
            print (shugemingli[i+4],end="")
    print('地格:')
    for i in range(len(shugemingli)):
        a = shugemingli[i]
        dige_jiedu = re.match(str(dige) + '(\D.*)', a)
        if dige_jiedu:
            dige_jiedu = dige_jiedu.group(1) 
            print (dige_jiedu)
            print (shugemingli[i+1],end="")
            print (shugemingli[i+2],end="")
            print (shugemingli[i+3],end="")
            print (shugemingli[i+4],end="")
    print('人格:')
    for i in range(len(shugemingli)):
        a = shugemingli[i]
        renge_jiedu = re.match(str(renge) + '(\D.*)', a)
        if renge_jiedu:
            renge_jiedu = renge_jiedu.group(1) 
            print (renge_jiedu)
            print (shugemingli[i+1],end="")
            print (shugemingli[i+2],end="")
            print (shugemingli[i+3],end="")
            print (shugemingli[i+4],end="")
    print('外格:')
    for i in range(len(shugemingli)):
        a = shugemingli[i]
        waige_jiedu = re.match(str(waige) + '(\D.*)', a)
        if waige_jiedu:
            waige_jiedu = waige_jiedu.group(1) 
            print (waige_jiedu)
            print (shugemingli[i+1],end="")
            print (shugemingli[i+2],end="")
            print (shugemingli[i+3],end="")
            print (shugemingli[i+4],end="")
    print('总格:')
    for i in range(len(shugemingli)):
        a = shugemingli[i]
        zongge_jiedu = re.match(str(zongge) + '(\D.*)', a)
        if zongge_jiedu:
            zongge_jiedu = zongge_jiedu.group(1) 
            print (zongge_jiedu)
            print (shugemingli[i+1],end="")
            print (shugemingli[i+2],end="")
            print (shugemingli[i+3],end="")
            print (shugemingli[i+4],end="")

if __name__=='__main__':
    print('天水讼姓名测试系统')
    print('北京天水讼科技有限公司荣誉出品') 
    # Default setting
    last_name  = '王' 
    first_name = '木'
    birthday   = '2018010102'
    sex        = '男'
    # Real test 
    #last_name  = input('您的姓:')
    #first_name = input('您的名:')
    #birthday   = input('您的生日:')
    #sex        = input('您是先生还是女士:')
    analyze()

