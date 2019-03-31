
# import packages

# 系统相关
import os
import sys
import json
import time

# JSON
import json

# 处理网页抓取

import urllib
from urllib import request
from bs4 import BeautifulSoup

# 网页字符集检测
import chardet

# variable

# ========================

# class
class web_discovery:

    # 构造者函数
    def __init__(self,url):

        # variable - level 1
        # 需要扫描的网页地址
        self.url = url

        # variable - level 2
        # WEB 响应对象
        self.ObjResponse = request.urlopen(self.url)

        # WEB 下载对象
        self.ObjDownload = urllib.request
        # 下载到本地的位置
        self.LocalPath = ""

        # WEB 对象
        self.ObjHtml = self.ObjResponse.read()
        # WEB 字符集对象
        self.ObjHtmlCharset = chardet.detect(self.ObjHtml)
        # BeautifulSoup 对象
        self.ObjBeautifulSoup = BeautifulSoup(self.ObjHtml,'lxml')
        # BeautifulSoupPretty 对象
        self.ObjBeautifulSoupPretty = self.ObjBeautifulSoup.prettify()

    # function

    # End - Class
    pass

# do

if __name__ == "__main__":

    # variable - level 1
    # 要下载的位置
    download_directory = "download_data/"

    # 要抓取的网页
    target_url = "https://www.zhihu.com/question/306126586/answer/607889154"

    # do
    wd = web_discovery(target_url)

    # variable - level 2
    listVideo = wd.ObjBeautifulSoup.findAll('a',attrs={"class" : "video-box"})

    for video in listVideo:

        # variable
        purpose_name = video.get('data-name')
        purpose_url = video.get('href')

        # 具体视频对应的ID号码
        purpose_url_id = str(purpose_url)[::-1].split('/')[0][::-1]

        # 知乎XHR地址
        xhr_zhihu = "https://lens.zhihu.com/api/v4/videos/"
        xhr_purpose = xhr_zhihu+purpose_url_id

        # do

        # 二级分析 - 针对二级URL做分析
        wd_level_2 = web_discovery(xhr_purpose)

        download_data_string = wd_level_2.ObjHtml

        # 分析JSON的XHR数据
        download_data_json = json.loads(download_data_string)
        download_url = download_data_json['playlist']['LD']['play_url']

        # 执行文件下载阶段
        download_path = download_directory + purpose_url_id + ".mp4"

        # display
        print("==============================================")
        print("Video Name is【" + purpose_name + "】")
        print("Video URL  is【" + purpose_url + "】")
        print("Video ID   is【" + purpose_url_id + "】")
        print("XHR   URL  is【" + xhr_purpose + "】")
        print("Download URL:【" + download_url + "】")
        print("Save Dir  is:【" + download_path + "】")
        print("------------")
        print("Execute：【Download】= Begin")

        # do
        wd_level_2.ObjDownload.urlretrieve(download_url,download_path)

        # display
        print("Execute：【Download】= Done")
        print("")

# done