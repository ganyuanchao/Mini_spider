#coding=utf-8
"""
获取url的内容并且保存

"""
import os
import re
import urllib2

import log

class WebpageSaves(object):
    """
    webpageSaves
    """
    def __init__(self):
        self.logger=log.init_log("./log/mini_spider_log")
    def GetUrl(self, url):
        if url is None or url == "":
            return
        res=urllib2.urlopen(url)
        content=res.read()
        self.logger.info("download %s" % url)
        return content

    def Save(self, url, output_path):
        if url is None or url == "":
            return
        if not os.path.exists(output_path):
            os.mkdir(output_path)
        content = self.GetUrl(url)
        if content is None:
            return
        pattern=re.compile(r'(?<=\://).*?(?=\.html)')
        #这里返回的是一个队列
        urlname=re.findall(pattern, url)
        urlname[0]=urlname[0].replace(':', '.')
        urlname[0] = urlname[0].replace('/', '.')
        #print urlname[0]
        full_file_name = os.path.abspath(output_path) + "\\" +str(urlname[0])
        #print full_file_name
        try:
            f=open(full_file_name,'w+')
            f.write(content)
            self.logger.info("save webpage content into file %s " % full_file_name)
        except:
            self.logger.error("save webpage %s error" % url)
"""
test = WebpageSaves()
output_path='./out_put'
url = "http://pycm.baidu.com:8081/page2.html"
content = test.GetUrl(url)
test.Save(url,output_path)
"""






