#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
读取配置文件
"""
import log
import ConfigParser

class LoadConfig(object):

    def __init__(self):
        self.url_list_file = ''
        self.output_directory = ''
        self.max_depth = ''
        self.crawl_interval = ''
        self.target_url = ''
        self.thread_count = ''
        self.crawl_timeout = ''
        # 日志保存到./log/mini_spider_log.log和./log/mini_spider_log.log.wf，按天切割，保留7天
        self.logger = log.init_log("./log/mini_spider_log")

    def loads(self, conf_file):
        """
                load spider conf file
                Args:
                    conf_file: conf file
                Return:
                    conf_dict: conf dict
                """
        try:
            conf = ConfigParser.ConfigParser()
            conf.read(conf_file)
            conf_dict = {}
            self.url_list_file = conf.get('spider', 'url_list_file')
            conf_dict['url_list_file'] = self.url_list_file
            self.output_directory = conf.get('spider', 'output_directory')
            conf_dict['output_directory'] = self.output_directory
            self.max_depth = conf.get('spider', 'max_depth')
            conf_dict['max_depth'] = int(self.max_depth)
            self.crawl_interval = conf.get('spider', 'crawl_interval')
            conf_dict['crawl_interval'] = int(self.crawl_interval)
            self.target_url = conf.get('spider', 'target_url')
            conf_dict['target_url'] = self.target_url
            self.crawl_timeout = conf.get('spider', 'crawl_timeout')
            conf_dict['crawl_timeout'] = int(self.crawl_timeout)
            self.thread_count = conf.get('spider', 'thread_count')
            conf_dict['thread_count'] = int(self.thread_count)
            return conf_dict
        except ConfigParser.Error:
            self.logger.error("conf_file load failed, please check it")
"""
conf=Load_Config()
conf.loads("spider.conf")
print conf.url_list_file
print conf.output_directory
print conf.max_depth
print conf.crawl_interval
print conf.target_url
print conf.crawl_timeout
print conf.thread_count
"""