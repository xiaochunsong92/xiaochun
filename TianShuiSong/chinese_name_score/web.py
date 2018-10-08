#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import sys
import importlib
#imp.reload(sys)
keywords = {'wd':'金'}
importlib.reload(sys)
url = 'http://tool.httpcn.com/KangXi/So.asp'
#url = 'http://wuxing.bm8.com.cn/'
#url = 'http://xh.5156edu.com/page/z9493m5997j19951.html'
#response = requests.get("http://xh.5156edu.com/page/z9493m5997j19951.html")
#response = requests.get("http://xh.5156edu.com/page/z9493m5997j19951.html")
#response = requests.get(url)
#response.endcoding = 'GB2312'
r = requests.post(url, data = keywords)
#r.endcoding = 'GB2312'
r.endcoding = 'utf-8'
#r.endcoding = 'GB18030'
#r.errors = 'ignore'
#print (r.text)
print (r.content.decode(r.endcoding))
#print (r.content)
#print (response.apparent_encoding)
#print (response.content.decode(response.endcoding))
