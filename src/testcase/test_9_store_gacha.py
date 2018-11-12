#coding=utf-8
import json
import sys
import unittest
from public.getuserToken import *
from tools.settings import *
import requests

reload(sys)
sys.setdefaultencoding('utf8')

class testStoreGacha(unittest.TestCase):

    '''/store/gacha商城抽卡'''

    url='http://192.168.5.111:8590/store/gacha'

    def setUp(self):
        self.postdata={
            'd':{},
            'seq':100,
            'rseq':100,
            't':read_token()
        }

    def test1_store_gacha_d10(self):
        '''正常参数购买10次'''
        d=json.dumps({"type":10,"id":"A1"})
        self.postdata['d']=d
        self.postdata['seq']=101
        self.postdata['rseq']=101
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test2_store_gacha_d_null(self):
        '''d参数为空'''
        self.postdata['d'] = {}
        self.postdata['seq']=102
        self.postdata['rseq'] = 102
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1 and '客户端数据错误，请稍后重试' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

    def test3_store_gacha_d_error(self):
        '''d参数错误'''
        self.postdata['d'] = 2
        self.postdata['seq']=103
        self.postdata['rseq'] = 103
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1 and '客户端数据错误，请稍后重试' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

    def test4_store_gacha_d1(self):
        '''购买1次'''
        d = json.dumps({"type": 1, "id": "A1"})
        self.postdata['d'] = d
        self.postdata['seq']=104
        self.postdata['rseq'] = 104
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test5_store_gacha_d5(self):
        '''购买5次,前端没有购买5次'''
        d = json.dumps({"type": 5, "id": "A1"})
        self.postdata['d'] = d
        self.postdata['seq']=105
        self.postdata['rseq'] = 105
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

    def test6_store_gacha_d11(self):
        '''购买11次'''
        d = json.dumps({"type": 11, "id": "A1"})
        self.postdata['d'] = d
        self.postdata['seq']=106
        self.postdata['rseq'] = 106
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])


if __name__ =='__main__':
    unittest.main()