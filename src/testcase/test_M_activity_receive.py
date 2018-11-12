#coding=utf-8
import json
import sys
import unittest
from public.getuserToken import *
from tools.settings import *
import requests

reload(sys)
sys.setdefaultencoding('utf8')

class testActivityReceive(unittest.TestCase):

    '''/activity/receive新手福利红包'''

    url='http://192.168.5.111:8590/activity/receive'

    def setUp(self):
        self.postdata={
            'd':{},
            'seq':100,
            'rseq':100,
            't':read_token()
        }

    def test1_activity_receive(self):
        '''正常参数'''
        d=json.dumps({"name":"NoobFund","id":101})
        self.postdata['d']=d
        self.postdata['seq']=102
        self.postdata['rseq']=102
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test2_activity_receive(self):
        '''为达成条件的奖励'''
        d=json.dumps({"name":"NoobFund","id":105})
        self.postdata['d']=d
        self.postdata['seq']=104
        self.postdata['rseq']=104
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1 and '未达成条件，不能领取奖励' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

    def test3_activity_receive_dnull(self):
        '''参数为空'''
        self.postdata['seq']=106
        self.postdata['rseq'] = 106
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1 and '客户端数据错误，请稍后重试' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

    def test4_activity_receive_isreceive(self):
        '''奖励已领取'''
        d=json.dumps({"name":"NoobRedPacket","id":2})
        self.postdata['d']=d
        self.postdata['seq']=108
        self.postdata['rseq']=108
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1 and '活动奖励已领取' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

    def test5_activity_receive_notexsit(self):
        '''奖励id不存在'''
        d=json.dumps({"name":"NoobRedPacket","id":10})
        self.postdata['d']=d
        self.postdata['seq']=109
        self.postdata['rseq']=109
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

if __name__ =='__main__':
    unittest.main()