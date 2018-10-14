#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/14 22:34
# @Author  : Jason Chan
# @Site    : 
# @File    : html_downloader.py
# @Software: PyCharm
import urllib2


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            print("response.getcode()=", response.getcode())
            return None
        return response.read()
