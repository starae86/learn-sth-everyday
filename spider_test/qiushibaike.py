#!/usr/bin/env python
# -*-coding:utf-8 -*-

import urllib, urllib.request, urllib.error
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
try:
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<div.*?author clearfix">.*?'
                         '<h2>(.*?)</h2>.*?''<div.*?content".*?<span>(.*?)</span>.*?</a>(.*?)'
                         '<div class="stats".*?number">(.*?)</i>', re.S)
    # pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?' +
    #                      'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',
    #                      re.S)
    items = re.findall(pattern, content)
    for item in items:
        haveImg = re.search("img", item[2])
        if not haveImg:
            print(item[0], item[1], item[3], '\n')
            # print(response.read().decode('utf-8'))
except urllib.error.URLError as e:
    if hasattr(e, "code"):
        print(e.code)
    if hasattr(e, 'reason'):
        print(e.reason)
