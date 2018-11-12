#coding=utf-8
import json
import sys
import unittest
from public.getuserToken import *
from tools.settings import *
import requests

reload(sys)
sys.setdefaultencoding('utf8')

class testCardUpgrade(unittest.TestCase):

    '''/card/upgrade卡牌进阶'''

    url='http://192.168.5.111:8590/card/upgrade'

    def setUp(self):
        self.postdata={
            'd':{},
            'seq':100,
            'rseq':100,
            't':read_token()
        }

    def test1_card_upgrade(self):
        '''正常参数进阶'''
        d=json.dumps({"pcid":13})
        self.postdata['d']=d
        self.postdata['seq']=102
        self.postdata['rseq']=102
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test2_card_upgrade(self):
        '''正常参数进阶'''
        d=json.dumps({"pcid":12})
        self.postdata['d']=d
        self.postdata['seq']=103
        self.postdata['rseq']=103
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test3_card_upgrade_dnotexsit(self):
        '''不存在id'''
        d = json.dumps({"pcid":555})
        self.postdata['d'] = d
        self.postdata['seq']=105
        self.postdata['rseq'] = 105
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1 and '卡牌不存在' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

    def test4_card_upgrade_dnull(self):
        '''参数为空'''
        self.postdata['seq']=106
        self.postdata['rseq'] = 106
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1 and '卡牌不存在' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

if __name__ =='__main__':
    unittest.main()