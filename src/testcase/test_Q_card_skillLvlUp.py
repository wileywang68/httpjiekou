#coding=utf-8
import json
import sys
import unittest
from public.getuserToken import *
from tools.settings import *
import requests

reload(sys)
sys.setdefaultencoding('utf8')

class testCardskillLvlUp(unittest.TestCase):

    '''/card/skillLvlUp卡牌技能升级'''

    url='http://192.168.5.111:8590/card/skillLvlUp'

    def setUp(self):
        self.postdata={
            'd':{},
            'seq':100,
            'rseq':100,
            't':read_token()
        }

    def test1_card_skillLvlUp(self):
        '''正常参数'''
        d=json.dumps({"costType":"d","pcid":13,"slot":0})
        self.postdata['d']=d
        self.postdata['seq']=102
        self.postdata['rseq']=102
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test2_card_skillLvlUp(self):
        '''正常参数'''
        d=json.dumps({"costType":"d","pcid":13,"slot":1})
        self.postdata['d']=d
        self.postdata['seq']=103
        self.postdata['rseq']=103
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test3_card_skillLvlUp(self):
        '''正常参数'''
        d=json.dumps({"costType":"d","pcid":13,"slot":2})
        self.postdata['d']=d
        self.postdata['seq']=104
        self.postdata['rseq']=104
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test4_card_skillLvlUp(self):
        '''正常参数'''
        d=json.dumps({"costType":"d","pcid":13,"slot":3})
        self.postdata['d']=d
        self.postdata['seq']=105
        self.postdata['rseq']=105
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test5_card_skillLvlUp(self):
        '''正常参数'''
        d=json.dumps({"costType":"d","pcid":13,"slot":4})
        self.postdata['d']=d
        self.postdata['seq']=106
        self.postdata['rseq']=106
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test6_card_skillLvlUp(self):
        '''正常参数'''
        d=json.dumps({"costType":"d","pcid":13,"slot":5})
        self.postdata['d']=d
        self.postdata['seq']=107
        self.postdata['rseq']=107
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test7_card_skillLvlUp(self):
        '''正常参数'''
        d=json.dumps({"costType":"d","pcid":13,"slot":6})
        self.postdata['d']=d
        self.postdata['seq']=108
        self.postdata['rseq']=108
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1 and '客户端数据错误，请稍后重试' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

    def test8_card_skillLvlUp_dnotexsit(self):
        '''不存在id'''
        d = json.dumps({"costType":"d","pcid":555,"slot":1})
        self.postdata['d'] = d
        self.postdata['seq']=109
        self.postdata['rseq'] = 109
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test9_card_skillLvlUp_dcosttypeerror(self):
        '''costtype错误'''
        d = json.dumps({"costType":"m","pcid":13,"slot":2})
        self.postdata['d'] = d
        self.postdata['seq']=110
        self.postdata['rseq'] = 110
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1 and '卡牌技能未开启' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

    def testA_card_skillLvlUp_dsloterror(self):
        '''slot错误'''
        d = json.dumps({"costType":"d","pcid":13,"slot":11})
        self.postdata['d'] = d
        self.postdata['seq']=111
        self.postdata['rseq'] = 111
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1 and '客户端数据错误，请稍后重试' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

    def testB_card_skillLvlUp_dnull(self):
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