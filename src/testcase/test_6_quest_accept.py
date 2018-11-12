#coding=utf-8
import json
import sys
import unittest
from public.getuserToken import *
from tools.settings import *
import requests

reload(sys)
sys.setdefaultencoding('utf8')

class testQuestAccept(unittest.TestCase):

    '''/quest/accept俄罗斯开始游戏'''

    url='http://192.168.5.111:8590/quest/accept'

    def setUp(self):
        self.postdata={
            'd':{},
            'seq':100,
            'rseq':100,
            't':read_token()
        }

    def test1_quest_accept(self):
        '''正常参数'''
        d=json.dumps({"qid":"Q101"})
        self.postdata['d']=d
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test2_quest_accept_d_null(self):
        '''d参数为空'''
        self.postdata['d'] = {}
        self.postdata['seq']=101
        self.postdata['rseq'] = 101
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1 and '客户端数据错误，请稍后重试' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

    def test3_quest_accept_qidweijiesuo(self):
        '''d参数关卡未解锁'''
        d = json.dumps({"qid": "Q801"})
        self.postdata['d'] = d
        self.postdata['seq']=102
        self.postdata['rseq'] = 102
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1 and '前置关卡未通关，不能进行比赛' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

    def test4_quest_accept_qidnotexsit(self):
        '''d参数关卡未解锁'''
        d = json.dumps({"qid": "sdfsfds"})
        self.postdata['d'] = d
        self.postdata['seq']=103
        self.postdata['rseq'] = 103
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1 and '客户端数据错误，请稍后重试' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

if __name__ =='__main__':
    unittest.main()