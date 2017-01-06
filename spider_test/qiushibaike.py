#!/usr/bin/python
# -*-coding:utf-8 -*-

import urllib
import urllib.request
import urllib.error
import re


# 糗百爬虫类
class QSBK:
    # 初始化方法，定义一些变量
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        # 初始化header
        self.headers = {'User-Agent': self.user_agent}
        # 存放段子的变量，每个元素是每一页的段子
        self.stories = []
        # 存放程序时候继续的变量
        self.enable = False

    # 传入某一页的索引索取页面代码
    def getPage(self, pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            # 构造请求的request
            request = urllib.request.Request(url, headers=self.headers)
            # 获取页面代码
            response = urllib.request.urlopen(request)
            # 页面转码
            pageCode = response.read().decode('utf-8')
            return pageCode
        except urllib.error.URLError as e:
            if hasattr(e, 'reason'):
                print(u'连接糗百失败，原因是：', e.reason)
                return None

    # 传入页码，返回不带图片的段子列表
    def getPageItems(self, pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print('页面加载失败。。。')
            return None
        pattern = re.compile(
            '<div.*?author clearfix">.*?<h2>(.*?)</h2>.*?<div.*?content".*?<span>(.*?)</span>.*?</a>(.*?)<div class="stats".*?number">(.*?)</i>',
            re.S)

        items = re.findall(pattern, pageCode)
        # print(items)
        # 存储段子
        pageStories = []
        # 遍历正则匹配的信息
        for item in items:
            # 是否含有图片
            haveImg = re.search("img", item[2])
            # 不含有图片就把它加到list中
            if not haveImg:
                replaceBR = re.compile('<br/>')
                text = re.sub('<br/>', '\n', item[1])
                # items[0]是作者信息,items[1]是段子内容，items[3]是赞数
                pageStories.append(item)
                # pageStories.append(text)
                # pageStories.append(items[3])
                return pageStories

    # 加载并提取页面内容，加入到列表中
    def loadPage(self):
        # 如果当前未看的页数少于2页，则加载新一页
        if self.enable == True:
            if len(self.stories) < 2:
                # 获取新一页
                pageStories = self.getPageItems(self.pageIndex)
                # 将该页的段子存放在全局list中
                if pageStories:
                    self.stories.append(pageStories)
                    print(len(self.stories))
                    # 索引加一
                    self.pageIndex += 1

    # 调用该方法，每次敲回车输出一个段子
    def getOneStroy(self, pageStories, page):
        # 便利一页的段子
        for story in pageStories:
            # 等待用户输入
            Input = input()
            # 每当输入回车，判断一次是否要加载页面
            self.loadPage()
            # 输入q结束程序
            if Input == 'q':
                self.enable = False
                return
            print('第%d页\t发布人:%s\t赞数:%s\n%s' % (page, story[0], story[3], story[1]))

    # 开始方法
    def start(self):
        print('正在读取糗事百科，按回车查看新段子，q退出')
        # 使变量置为True，程序可以正常运行
        self.enable = True
        # 先加载一页内容
        self.loadPage()
        # print(self.stories)
        # 局部变量，控制当前读到了第几页
        nowPage = 0
        while self.enable:
            if len(self.stories) > 0:
                # 从全局list中获取第一页的段子
                pageStories = self.stories[0]
                # 当前读取到的页数+1
                nowPage += 1
                # 将全局list中的第一个元素删除，因为已经取出
                del self.stories[0]
                # 输出该页的段子内容
                self.getOneStroy(pageStories, nowPage)
                # for story in self.stories:
                #     nowPage+=1
                #     self.getOneStroy(story,nowPage)


spider = QSBK()
spider.start()
