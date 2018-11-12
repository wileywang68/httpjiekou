#coding=utf-8
import json
import sys
import unittest
from public.getuserToken import *
from tools.settings import *
import requests

reload(sys)
sys.setdefaultencoding('utf8')

class testCardUpgradeEquips(unittest.TestCase):

    '''/card/upgradeEquips卡牌装备升级'''

    url='http://192.168.5.111:8590/card/upgradeEquips'

    def setUp(self):
        self.postdata={
            'd':{},
            'seq':100,
            'rseq':100,
            't':read_token()
        }

    def test2_card_upgradeEquips(self):
        '''正常参数升级'''
        d=json.dumps({"pcid":14,"slots":[0,1,2]})
        self.postdata['d']=d
        self.postdata['seq']=102
        self.postdata['rseq']=102
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test3_card_upgradeEquips(self):
        '''正常参数升级'''
        d=json.dumps({"pcid":13,"slots":[0,1,2]})
        self.postdata['d']=d
        self.postdata['seq']=103
        self.postdata['rseq']=103
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test5_card_upgradeEquips_dnotexsit(self):
        '''不存在id'''
        d = json.dumps({"pcid":10111,"slots":[0,1,2]})
        self.postdata['d'] = d
        self.postdata['seq']=105
        self.postdata['rseq'] = 105
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1 and '卡牌不存在' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

    def test6_card_upgradeEquips_dnull(self):
        '''参数为空'''
        self.postdata['seq']=106
        self.postdata['rseq'] = 106
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

if __name__ =='__main__':
    unittest.main()