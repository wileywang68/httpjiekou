#coding=utf-8
import json
import sys
import unittest
from public.getuserToken import *
from tools.settings import *
import requests

reload(sys)
sys.setdefaultencoding('utf8')

class testCardSell(unittest.TestCase):

    '''/card/sell球员出售'''

    url='http://192.168.5.111:8590/card/sell'

    def setUp(self):
        self.postdata={
            'd':{},
            'seq':100,
            'rseq':100,
            't':read_token()
        }

    def test1_card_sell(self):
        '''正常参数'''
        d=json.dumps({"sellPiece":0,"pcids":[53]})
        self.postdata['d']=d
        self.postdata['seq']=102
        self.postdata['rseq']=102
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test2_card_sell(self):
        '''正常参数'''
        d=json.dumps({"pcids":[48]})
        self.postdata['d']=d
        self.postdata['seq']=105
        self.postdata['rseq']=105
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test3_card_sell(self):
        '''正常参数'''
        d=json.dumps({"sellPiece":0,"pcids":[53,48,40]})
        self.postdata['d']=d
        self.postdata['seq']=106
        self.postdata['rseq']=106
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test4_card_sell_dpciderror(self):
        '''pcid错误'''
        d = json.dumps({"sellPiece":0,"pcids":['s']})
        self.postdata['d'] = d
        self.postdata['seq']=110
        self.postdata['rseq'] = 110
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test5_card_sell_dnull(self):
        '''参数为空'''
        self.postdata['seq']=112
        self.postdata['rseq'] = 112
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

if __name__ =='__main__':
    unittest.main()