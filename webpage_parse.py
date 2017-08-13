#coding=utf-8
"""
对抓取网页的解析
"""
import re
import urllib2

import log
import config_load

class WebpageParse(object):
    """
        weppage parse
        """
    def __init__(self):
        self.logger=log.init_log("./log/mini_spider_log")


    def get_target_urls(self, content):
        """
        get target url list match the pattern
                Args:
                    url_list:url list
                    pattern: the url pattern
                Return:
                    url lists
        """
        reg=r'(?<=href=).*?\.html'
        urlgre=re.compile(reg)
        urllists=list()
        urllists =re.findall(urlgre, content)

    #for urllist in urllists:
        #urllist=urllist.replace('\'','')
        #urllist = urllist.replace('\"', '')
        #print urllist
        return urllists
"""
url="http://pycm.baidu.com:8081/"
res=urllib2.urlopen(url)
content=res.read()
wp=WebpageParse()
#lists=list()
wp.get_target_urls(content)
"""





