#coding=utf-8
import json
import sys
import unittest
from public.getuserToken import *
from tools.settings import *
import requests

reload(sys)
sys.setdefaultencoding('utf8')

class testCardUprating(unittest.TestCase):

    '''/card/upRating球员评价提升'''

    url='http://192.168.5.111:8590/card/upRating'

    def setUp(self):
        self.postdata={
            'd':{},
            'seq':100,
            'rseq':100,
            't':read_token()
        }

    def test1_card_uprating(self):
        '''正常参数'''
        d=json.dumps({"pcid":13})
        self.postdata['d']=d
        self.postdata['seq']=102
        self.postdata['rseq']=102
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test2_card_uprating(self):
        '''正常参数已评价提升'''
        d=json.dumps({"pcid":13})
        self.postdata['d']=d
        self.postdata['seq']=103
        self.postdata['rseq']=103
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test3_card_uprating_dpciderror(self):
        '''pcid错误'''
        d = json.dumps({"pcid":555})
        self.postdata['d'] = d
        self.postdata['seq']=110
        self.postdata['rseq'] = 110
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test4_card_uprating_dnull(self):
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