#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import sys
import importlib
keywords = {'wd':'金'}
url = 'http://tool.httpcn.com/KangXi/So.asp'
r = requests.post(url, data = keywords)
r.endcoding = 'utf-8'
print (r.content.decode(r.endcoding))
