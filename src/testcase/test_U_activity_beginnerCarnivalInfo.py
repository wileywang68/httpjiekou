#coding=utf-8
import json
import sys
import unittest
from public.getuserToken import *
from tools.settings import *
import requests

reload(sys)
sys.setdefaultencoding('utf8')

class testActivityBeginnerCarnivalInfo(unittest.TestCase):

    '''/activity/beginnerCarnivalInfo开服嘉年华信息'''

    url='http://192.168.5.111:8590/activity/beginnerCarnivalInfo'

    def setUp(self):
        self.postdata={
            'd':{},
            'seq':100,
            'rseq':100,
            't':read_token()
        }

    def test1_activity_beginnerCarnivalInfo(self):
        '''正常参数'''
        self.postdata['seq']=102
        self.postdata['rseq']=102
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

if __name__ =='__main__':
    unittest.main()