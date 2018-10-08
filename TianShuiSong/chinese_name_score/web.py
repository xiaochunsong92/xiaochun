#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import sys
keywords = {'word':'金'}
url = 'http://wuxing.bm8.com.cn/'
#url = 'http://xh.5156edu.com/page/z9493m5997j19951.html'
#response = requests.get("http://xh.5156edu.com/page/z9493m5997j19951.html")
#response = requests.get("http://xh.5156edu.com/page/z9493m5997j19951.html")

#response.endcoding = 'GB2312'
r = requests.post(url, data = keywords)
r.endcoding = 'GB18030'
#r.errors = 'ignore'
#print (r.text)
print (r.content.decode(r.endcoding))
#print (response.apparent_encoding)
#print (response.content.decode(response.endcoding))
