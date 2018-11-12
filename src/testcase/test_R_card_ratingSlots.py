#coding=utf-8
import json
import sys
import unittest
from public.getuserToken import *
from tools.settings import *
import requests

reload(sys)
sys.setdefaultencoding('utf8')

class testCardRatingslots(unittest.TestCase):

    '''/card/ratingSlots球员碎片点亮'''

    url='http://192.168.5.111:8590/card/ratingSlots'

    def setUp(self):
        self.postdata={
            'd':{},
            'seq':100,
            'rseq':100,
            't':read_token()
        }

    def test1_card_ratingSlots(self):
        '''正常参数'''
        d=json.dumps({"pcid":13,"slots":[1]})
        self.postdata['d']=d
        self.postdata['seq']=102
        self.postdata['rseq']=102
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test2_card_ratingSlots(self):
        '''正常参数'''
        d=json.dumps({"pcid":13,"slots":[2]})
        self.postdata['d']=d
        self.postdata['seq']=103
        self.postdata['rseq']=103
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test3_card_ratingSlots(self):
        '''正常参数'''
        d=json.dumps({"pcid":13,"slots":[3]})
        self.postdata['d']=d
        self.postdata['seq']=104
        self.postdata['rseq']=104
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test4_card_ratingSlots(self):
        '''正常参数'''
        d=json.dumps({"pcid":13,"slots":[4]})
        self.postdata['d']=d
        self.postdata['seq']=105
        self.postdata['rseq']=105
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test5_card_ratingSlots(self):
        '''正常参数'''
        d=json.dumps({"pcid":1,"slots":[5]})
        self.postdata['d']=d
        self.postdata['seq']=106
        self.postdata['rseq']=106
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test6_card_ratingSlots(self):
        '''正常参数'''
        d=json.dumps({"pcid":1,"slots":[6]})
        self.postdata['d']=d
        self.postdata['seq']=107
        self.postdata['rseq']=107
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test7_card_ratingSlots_dnotexsit(self):
        '''不存在slots'''
        d = json.dumps({"pcid":13,"slots":[90]})
        self.postdata['d'] = d
        self.postdata['seq']=109
        self.postdata['rseq'] = 109
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def testA_card_ratingSlots_dpciderror(self):
        '''pcid错误'''
        d = json.dumps({"pcid":55523223,"slots":[1]})
        self.postdata['d'] = d
        self.postdata['seq']=110
        self.postdata['rseq'] = 110
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def testC_card_ratingSlots_dnull(self):
        '''参数为空'''
        self.postdata['seq']=112
        self.postdata['rseq'] = 112
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def testD_card_ratingSlots_yijian(self):
        '''正常参数一键点亮'''
        d=json.dumps({"pcid":13,"slots":[5,6]})
        self.postdata['d']=d
        self.postdata['seq']=113
        self.postdata['rseq']=113
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)


if __name__ =='__main__':
    unittest.main()