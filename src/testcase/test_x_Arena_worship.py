#coding=utf-8
import json
import sys
import unittest
from public.getuserToken import *
from tools.settings import *
import requests
import random

reload(sys)
sys.setdefaultencoding('utf8')

class testArenaWorship(unittest.TestCase):

    '''/arena/worship天梯排行膜拜'''

    url='http://192.168.5.111:8590/arena/worship'


    postdata={
            'd':{},
            'seq':100,
            'rseq':100,
            't':read_token()
    }

    @classmethod
    def setUpClass(cls):
        url='http://192.168.5.111:8590/arena/rankInfo'
        req=requests.post(url,data=cls.postdata)
        cls.l=[]
        dicts=req.json()['d']['rankList']
        for k,v in dicts.items():
            cls.l.append(k)


    def test1_arena_worship(self):
        '''正常参数'''
        d=json.dumps({"pid":random.choice(self.l)})
        self.postdata['d']=d
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test2_arena_worship_isworship(self):
        '''已经膜拜过'''
        d=json.dumps({"pid":random.choice(self.l)})
        self.postdata['d']=d
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test3_arena_worship_pidnull(self):
        '''参数Pid为空'''
        d=json.dumps({"pid":""})
        self.postdata['d']=d
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)


    def test4_arena_worship_piderror(self):
        '''参数Pid错误'''
        d = json.dumps({"pid": "asdfjasdlfkjds"})
        self.postdata['d'] = d
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test5_arena_worship_null(self):
        '''参数为空'''
        self.postdata['d'] = {}
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)


if __name__ =='__main__':
    unittest.main()