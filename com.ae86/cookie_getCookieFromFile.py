# ！/usr/bin/env python
# -*-coding:utf-8 -*-

import http.cookiejar as cookiejar
import urllib.request as request

cookie = cookiejar.MozillaCookieJar()
cookie.load('cookie.txt',ignore_expires=True,ignore_discard=True)
req=request.Request('http://www.baidu.com')
opener = request.build_opener(request.HTTPCookieProcessor(cookie))
response = opener.open(req)
print(response.read())

