#! /usr/bin/python
# -*-coding:utf-8 -*-
import re
import urllib
import urllib.request
import urllib.error

# 处理页面标签类
class Tool:
    # 去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    # 删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    # 把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    # 将表格制表<td>替换为\t
    replaceTD = re.compile('<td>')
    # 把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    # 将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    # 将其余标签剔除
    removeExtraTag = re.compile('<.*?>')

    def replace(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replacePara, "\n    ", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        # strip()将前后多余内容删除
        return x.strip()


"""
百度贴吧爬虫类
"""


class BDTB:
    # 初始化，传入基地址，是否只看楼主
    def __init__(self, baseUrl, seelZ):
        self.baseUrl = baseUrl
        self.seelZ = '?see_lz=' + str(seelZ)
        self.tool = Tool()

    # 传入页码，获取该页帖子的代码
    def getPage(self, pageIndex):
        try:
            url = self.baseUrl + self.seelZ + '&pn=' + str(pageIndex)
            request = urllib.request.Request(url)
            response = urllib.request.urlopen(request)
            # print(response.read().decode('utf-8'))
            return response.read().decode('utf-8')
        except urllib.error.URLError as e:
            if hasattr(e, 'reason'):
                print('连接错误。。。原因是：', e.reason)
                return None

    # 获取标签
    def getTitle(self):
        page = self.getPage(1)
        pattern = re.compile(r'<h3 class="core_title_txt.*?>(.*?)</h3>')
        result = re.search(pattern, page)
        if result:
            # print(result.group(1))
            return result.group(1).strip()
        else:
            return None

    # 获取帖子总页数
    def getPageNum(self):
        page = self.getPage(1)
        pattern = re.compile(r'<li class="l_reply_num.*?<span class="red">(.*?)</span>')
        result = re.search(pattern, page)
        if result:
            # print(result.group(1))
            return result.group(1).strip()
        else:
            return None

    # 获取每一层楼的内容,传入页面内容
    def getContent(self, page):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
        items = re.findall(pattern, page)
        floor = 1
        for item in items:
            print(floor, r"-----------------------------------"
                         r"-----------------------------------"
                         r"-----------------------------------"
                         r"---------------------------\n")
            print(self.tool.replace(item))
            floor += 1


if __name__ == '__main__':
    baseUrl = 'http://tieba.baidu.com/p/3138733512'
    bdtb = BDTB(baseUrl, 1)
    # bdtb.getPage(1)
    # bdtb.getTitle()
    # bdtb.getPageNum()
    bdtb.getContent(bdtb.getPage(1))