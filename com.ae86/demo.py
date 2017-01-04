import urllib.request,urllib

response = urllib.request.urlopen('http://www.zhihu.com')
# print(response.read())
with open('e:/360Downloads/xxx/spider/spider.txt','bw') as f:
    f.write(response.read())
