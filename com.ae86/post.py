import urllib,urllib.request,urllib.response,urllib.parse

values = {
    "username":"123@qq.com",
    "password":"xxxx"
}

data = urllib.parse.urlencode(values).encode(encoding='utf-8')
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib.request.Request(url,data)
response = urllib.request.urlopen(request)
print(response.read())