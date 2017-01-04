#!/usr/bin/env python
#-*- coding:utf-8 -*-

import http.cookiejar as cookie
import urllib.request as request

filename = 'cookie.txt'
cookie= cookie.MozillaCookieJar(filename)
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)