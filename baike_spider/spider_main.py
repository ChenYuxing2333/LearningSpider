#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/14 22:34
# @Author  : Jason Chan
# @Site    : 
# @File    : spider_main.py
# @Software: PyCharm
import url_manager, html_downloader, html_parser, html_outputer

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManger()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' % (count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_url(new_urls)
                self.outputer.collect_data(new_data)
                # 只爬100条
                if count == 100:
                    break

                count = count + 1
            except:
                print 'craw failed'
        # 爬完了
        print 'craw finished'
        self.outputer.output_html()

# 编写模块的主入口
if __name__ == "__main__":
    # 爬虫入口页面
    # root_url = 'https://baike.baidu.com/item/Python/407313'
    root_url = 'http://baike.baidu.com/item/Python'
    obj_spider = SpiderMain()
    # 启动爬虫
    obj_spider.craw(root_url)
