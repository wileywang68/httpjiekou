#coding=utf-8
import json
import sys
import unittest
from public.getuserToken import *
from tools.settings import *
import requests

reload(sys)
sys.setdefaultencoding('utf8')

class testArenaStorebuy(unittest.TestCase):

    '''/arena/storeBuy天梯商店兑换'''

    url='http://192.168.5.111:8590/arena/storeBuy'

    def setUp(self):
        self.postdata={
            'd':{},
            'seq':100,
            'rseq':100,
            't':read_token()
        }

    def test1_arena_storebuy(self):
        '''正常参数'''
        d=json.dumps({"id":"5"})
        self.postdata['d']=d
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test2_arena_storebuy_isone(self):
        '''正常参数一天限购1次'''
        d=json.dumps({"id":"2"})
        self.postdata['d']=d
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1 and '您的购买次数已用完' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

    def test3_arena_storebuy_isnotexsit(self):
        '''兑换Id不存在23'''
        d=json.dumps({"id":"23"})
        self.postdata['d']=d
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1 and '客户端数据错误，请稍后重试' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

    def test4_arena_storebuy_isnotexsit(self):
        '''兑换Id不存在0'''
        d=json.dumps({"id":"0"})
        self.postdata['d']=d
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1 and '客户端数据错误，请稍后重试' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

    def test6_arena_storebuy_iderror1(self):
        '''兑换Id错误'''
        d=json.dumps({"id":"asdfsads"})
        self.postdata['d']=d
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1 and '客户端数据错误，请稍后重试' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

    def test7_arena_storebuy_idnull(self):
        '''兑换Id为空'''
        d=json.dumps({"id":""})
        self.postdata['d']=d
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1 and '客户端数据错误，请稍后重试' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

    def test8_arena_storebuy_null(self):
        '''参数为空'''
        self.postdata['d']={}
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1 and '客户端数据错误，请稍后重试' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

    def test9_arena_storebuy(self):
        '''参数正确'''
        d=json.dumps({"id":"1"})
        self.postdata['d']=d
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

if __name__ =='__main__':
    unittest.main()