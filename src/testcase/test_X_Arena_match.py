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

class testArenaMatch(unittest.TestCase):

    '''/arena/match天梯赛挑战'''

    url='http://192.168.5.111:8590/arena/match'

    def setUp(self):
        self.postdata={
            'd':{},
            'seq':100,
            'rseq':100,
            't':read_token()
        }
        url='http://192.168.5.111:8590/arena/rankInfo'
        req=requests.post(url,data=self.postdata)
        self.l = []
        dicts = req.json()['d']['rankList']
        for k, v in dicts.items():
            self.l.append(k)

    def test1_arena_match(self):
        '''正常参数'''
        d=json.dumps({"pid":random.choice(self.l)})
        self.postdata['d']=d
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test2_arena_match_cd(self):
        '''挑战冷却时间'''
        d=json.dumps({"pid":random.choice(self.l)})
        self.postdata['d']=d
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1 and '挑战冷却时间内' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

    def test3_arena_match_piderror(self):
        '''pid参数错误'''
        d=json.dumps({"pid":"sadfdsafasfsaf"})
        self.postdata['d']=d
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

    def test4_arena_match_pidnull(self):
        '''pid参数为空'''
        d=json.dumps({"pid":""})
        self.postdata['d']=d
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

    def test5_arena_match_null(self):
        '''参数为空'''
        self.postdata['d']={}
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])


if __name__ =='__main__':
    unittest.main()