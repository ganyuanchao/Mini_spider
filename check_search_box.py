"""
@Project: monster-case
@File: check_search_box.py
@Author: ganyuanchao <ganyuanchao@baidu.com>
@Date: 2017-08-01 15:05:05
@Last Modified by: ganyuanchao
@Last Modified time: 2017-08-01 18:22:03
@Description: check Wise resultpage bottom search box, case id is 4
"""

from case.wise.wise_base import WiseCase


class SearchBoxCase(WiseCase):
    """
    Wise Search Box Case
    """
    def init(self):
        """
        Init SearchBoxCase
        """
        self.data = r''
        super(SearchBoxCase, self).init()
        
    def run(self, data):
        """
        run func
        """
        self.data = data
        self.logger.info(r'Begin to check, input: %s' % str(data))
        self.check_search_box()
        self.logger.info(r'End')

   def check_search_box(self):
        """
        check
        """
        info = self.data['info']
        if not info:
            item = {'status' : False, 'url' : r'', 'snapshot' = r'', 'message' : r'No query' }
            self.log_output(item)
            return 1

         for  url in info[r'query']:
             # get page
             page_res = self.get_page(url, verify=False, timeout=2)
             ret = page_res[r'status']

             if no ret:
                 msg = r'Cannot open url'
                 item = {'status' : ret, 'url' : url, 'snapshot' : r'', 'message' : msg}
                 self.log_output(item)
                 return 1
             
             #check page
             page = page_res[r'result']
             snapshot = self.get_snapshot(page)
             check_keyword_se-bn = page.exist(r'#se-bn')
             if not check_keyword_se-bn:
                 msg = r'Fail, se-bn [%s]' % str(check_keyword_se-bn)
                 item = {'status' : False, 'url' : url, 'snapshot' : snapshot, 'message' : msg}
                 self.log_output(item)
             msg = r'Pass'
             item = {'status' : True, 'url' : url, 'snapshot' : snapshot, 'message' : msg}
             self.log_output(item)
         return 0

   def log_output():
       """fmt log output"""
       fmt = 'status[%(status)s] url[%(utl)s] snapshot[%(snapshot)s] message[%(message)s]'
       info['logoid'] = self.logoid
       if info['status']:
           self.logger.info(fmt, info)
       else:
            self.logger.error(fmt, info)