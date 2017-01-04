#!/usr/bin/env python
# -*-coding:utf-8-*-
import http.cookiejar as lib
import urllib.request as request

# 声明一个cookieJar对象实例保存cookie
cookie = lib.CookieJar()
# 创建cookie处理器
handler = request.HTTPCookieProcessor(cookie)
# 构造handler
opener = request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print('Name = ' + item.name)
    print('value = ' + item.value)
