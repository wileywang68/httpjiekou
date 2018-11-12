#coding=utf-8
import json
import sys
import unittest
from public.getuserToken import *
from tools.settings import *
import requests

reload(sys)
sys.setdefaultencoding('utf8')

class testActivityReceiveCarnival(unittest.TestCase):

    '''/activity/receiveCarnival领取嘉年华奖励'''

    url='http://192.168.5.111:8590/activity/receiveCarnival'

    def setUp(self):
        self.postdata={
            'd':{},
            'seq':100,
            'rseq':100,
            't':read_token()
        }

    def test1_activity_receiveCarnival(self):
        '''正常参数'''
        d=json.dumps({"id":"102"})
        self.postdata['d']=d
        self.postdata['seq']=102
        self.postdata['rseq']=102
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test2_activity_receiveCarnival(self):
        '''正常参数奖励已领取'''
        d=json.dumps({"id":"102"})
        self.postdata['d']=d
        self.postdata['seq']=103
        self.postdata['rseq']=103
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test3_activity_receiveCarnival_isnotreceive(self):
        '''奖励不可领取'''
        d=json.dumps({"id":"105"})
        self.postdata['d']=d
        self.postdata['seq']=103
        self.postdata['rseq']=103
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test4_activity_receiveCarnival_idnotexsit(self):
        '''奖励id不存在'''
        d=json.dumps({"id":"5555555"})
        self.postdata['d']=d
        self.postdata['seq']=104
        self.postdata['rseq']=104
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test5_activity_receiveCarnival_null(self):
        '''参数空'''
        self.postdata['seq']=105
        self.postdata['rseq']=105
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1 and '客户端数据错误，请稍后重试' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])


if __name__ =='__main__':
    unittest.main()