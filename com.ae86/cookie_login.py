#! /usr/bin/env python
# -*-coding:utf-8-*-

import urllib,urllib.request,urllib.parse
import http.cookiejar

filename = 'cookie.txt'

cookie = http.cookiejar.MozillaCookieJar(filename)
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
postData = urllib.parse.urlencode({
    'stuid':'starae86',
    'pwd':'starae8604'
}).encode(encoding='utf-8')

loginUrl = 'http://pan.baidu.com/infocenter/nlogin'
result = opener.open(loginUrl,postData)
cookie.save(ignore_discard=True,ignore_expires=True)
url='http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
result = opener.open(url)
print(result.read())