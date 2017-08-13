#coding=utf-8
"""
File: mini_spider.py
Author: ganyuanchao@baidu.com
Date: 2017/7/26
"""
import sys
import getopt
import Queue

import log
import config_load
import crawl_thread

logger=log.init_log("./log/mini_spider_log")
def usage():
    """
    help information
    """
    print(u"""
    -c / --config :配置文件
    -h / --help :使用帮助
    -v / --version :版本号
    """)


def main():
    #--------------------------对命令行参数的处理------------------------------------
    if len(sys.argv) <= 1:
        logger.info('没有输入参数,请输入命令行参数')
        usage()
        sys.exit()
    try:
        opts,args = getopt.getopt(sys.argv[1:],"c:hv",["config=","help","version"])
    except getopt.GetoptError:
        logger.error("Get opt failed")
        usage()
        sys.exit()
    for option,value in opts:
        if  option in ("-h","--help"):
            logger.info("No Help Message")
            usage()
            sys.exit()
        elif option in ("-v","--version"):
            logger.info("The version is 2.7")
            print ' The version is 2.7'
            sys.exit()
        if option in ("-c","--config"):
            conf_file=value
        else:
            logger.info("please input information")
            usage()
            sys.exit()
    
    #------------------------配置文件的处理-----------------------------
    conf=config_load.LoadConfig()
    con_dict={}
    # conf_file从命令行的‘-c‘处输入，输入的value就是配置文件
    #conf_dict=conf.loads(conf_file)
    conf_dict=conf.loads('spider.conf')

    #-----------------------读取种子文件-------------------------------
    urls=list()
    file=open(conf_dict["url_list_file"], 'r')
    while 1:
        line = file.readline().strip('\n')
        urls.append(line)
        if not line:
            break

    #---------------------从种子文件中抓取url并且保存满足要求的url内容--------------
    queue=Queue.Queue(10)
    print "---------The url of the seed is crawled as follows------------"
    for url in urls:
        queue.put(url)
        print url
    print "----------The crawled pages' url as follows----------"

    thread_list=[]
    for i in range(conf_dict["thread_count"]):
        thread=crawl_thread.MyThread(queue,conf_dict)
        thread.setDaemon(True)
        thread.start()
        thread_list.append(thread)
    while 1:
        alive=False
        for i in range(conf_dict["thread_count"]):
            alive=thread_list[i].join()
        if not alive:
            break
"""
 thread=crawl_thread.myThread(queue,conf_dict)
 thread.start()
"""
if __name__ == '__main__':
   main()
   print "-------Complete the web page parse and save, thank you for your use---------"