#coding=utf-8
import json
import sys
import unittest
from public.getuserToken import *
from tools.settings import *
import requests

reload(sys)
sys.setdefaultencoding('utf8')

class testCardCardLvlup(unittest.TestCase):

    '''/card/cardLvlUp卡牌升级'''

    url='http://192.168.5.111:8590/card/cardLvlUp'

    def setUp(self):
        self.postdata={
            'd':{},
            'seq':100,
            'rseq':100,
            't':read_token()
        }

    def test1_card_cardLvlUp(self):
        '''正常参数升级'''
        d=json.dumps({"pcid":13,"exp":1})
        self.postdata['d']=d
        self.postdata['seq']=102
        self.postdata['rseq']=102
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test2_card_cardLvlUp(self):
        '''正常参数升级'''
        d=json.dumps({"pcid":13,"exp":999999})
        self.postdata['d']=d
        self.postdata['seq']=103
        self.postdata['rseq']=103
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test3_card_cardLvlUp_dnotexsit(self):
        '''不存在id'''
        d = json.dumps({"pcid":5522335,"exp":190})
        self.postdata['d'] = d
        self.postdata['seq']=105
        self.postdata['rseq'] = 105
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test4_card_cardLvlUp_dexpfushu(self):
        '''经验负数'''
        d = json.dumps({"pcid":14,"exp":-1})
        self.postdata['d'] = d
        self.postdata['seq']=106
        self.postdata['rseq'] = 106
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test5_card_cardLvlUp_dnull(self):
        '''参数为空'''
        self.postdata['seq']=107
        self.postdata['rseq'] = 107
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

if __name__ =='__main__':
    unittest.main()