# encoding: UTF-8
"""
实现抓取线程
"""
import threading
import time
import Queue
import urllib2

import log
import config_load
import webpage_saves
import webpage_parse


#创建新类继承threading.Thread，重写threading.Thread的run方法
class MyThread(threading.Thread):
    """
        spider thread
        Attributes:
            logger: log information
            queue: the url queue waiting to be cralwed
            conf_dict["max_depth"]: spider's max_depth
            conf_dict["target_url"]: The target url patter
            conf_dit["crawl_interval"]: the parse interval
            conf_dict["crawl_timeout"]: urlopen time out
            conf_dict["output_directory"]: the directory to save url content
        """
    def __init__(self,queue,conf_dict):
        threading.Thread.__init__(self)
        self.queue=queue
        self.output_directory=conf_dict['output_directory']
        self.max_depth = conf_dict['max_depth']
        self.crawl_interval = conf_dict['crawl_interval']
        self.crawl_timeout = conf_dict['crawl_timeout']
        self.target_url = conf_dict['target_url']
        self.thread_stop=False
        self.logger=log.init_log("./log/mini_spider_log")

    def  run(self):
        while not self.thread_stop:
            try:
                #获取队列中的url，timeout等待时间
                url=self.queue.get(timeout=self.crawl_timeout)
                self.logger.info("get the url waiting from queue is %s"%url)
            except Queue.Empty:
                self.logger.info("%s is empty"%self.getName())#当前线程为空
                self.thread_stop=True
                continue
            #判断url是否有效
            if url is None or url=="":
                self.queue.task_done()
                continue
            #抓取url的内容
            content=webpage_saves.WebpageSaves().GetUrl(url)
            if content is None or content=="":
                continue

            target_urls=webpage_parse.WebpageParse().get_target_urls(content)
            #保存满足要求的url的content
            #print self.output_directory#保存的路径
            #对抓取到的网页进行处理
            try:
                for target_url in target_urls:
                    target_url = url + "/"+target_url
                    #print target_url
                    target_url = target_url.replace('\'', '')
                    target_url = target_url.replace('\"', '')
                    print target_url
                    webpage_saves.WebpageSaves().Save(target_url,self.output_directory)
            except urllib2.HTTPError, e:
                self.logger.error("%s Webpage happened error and can't open"%e.reason)
                self.stop()
    def stop(self):
        self.thread_stop=True

"""
url='http://pycm.baidu.com:8081'
queue=Queue.Queue(10)
queue.put(url)
conf = config_load.LoadConfig()
conf_dict = {}
conf_dict = conf.loads('spider.conf')
thread=MyThread(queue,conf_dict)
thread.start()
"""




