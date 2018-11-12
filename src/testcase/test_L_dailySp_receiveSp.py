#coding=utf-8
import json
import sys
import unittest
from public.getuserToken import *
from tools.settings import *
import requests

reload(sys)
sys.setdefaultencoding('utf8')

class testDailySpReceiveSp(unittest.TestCase):

    '''/dailySp/receiveSp每日上线领体力'''

    url='http://192.168.5.111:8590/dailySp/receiveSp'

    def setUp(self):
        self.postdata={
            'd':{},
            'seq':100,
            'rseq':100,
            't':read_token()
        }

    def test1_dailySp_receiveSp(self):
        '''正常参数'''
        self.postdata['seq']=102
        self.postdata['rseq']=102
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test2_dailySp_receiveSp_isreceive(self):
        '''奖励已领取'''
        self.postdata['seq']=105
        self.postdata['rseq'] = 105
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1 and '奖励已领取' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

if __name__ =='__main__':
    unittest.main()