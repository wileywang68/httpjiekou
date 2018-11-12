#coding=utf-8
import json
import sys
import unittest
from public.getuserToken import *
from tools.settings import *
import requests

reload(sys)
sys.setdefaultencoding('utf8')

class testPlayerChangeName(unittest.TestCase):

    '''/player/changeName修改俱乐部名称'''

    url='http://192.168.5.111:8590/player/changeName'

    def setUp(self):
        self.postdata={
            'd':{},
            'seq':100,
            'rseq':100,
            't':read_token()
        }

    def test1_player_changeName_namelong(self):
        '''参数name超出长度'''
        d=json.dumps({"name":"巴黎苞米水电费看是的风口浪尖水电费看见的斯洛伐克就手动开拉法基说了的空间发"})
        self.postdata['d']=d
        self.postdata['seq']=101
        self.postdata['rseq']=101
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1 and '球队名不符合长度限制' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

    def test2_player_changeName(self):
        '''正常参数'''
        d=json.dumps({"name":"你好"})
        self.postdata['d']=d
        self.postdata['seq']=102
        self.postdata['rseq']=102
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test3_player_changeName_derror(self):
        '''d参数错误'''
        self.postdata['d'] = 1
        self.postdata['seq']=103
        self.postdata['rseq'] = 103
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1 and '名字不能为空' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

    def test4_player_changeName_null(self):
        '''d参数为空'''
        self.postdata['seq']=104
        self.postdata['rseq'] = 104
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1 and '名字不能为空' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

    def test5_player_changeName_minganci(self):
        '''名字包含敏感词'''
        d=json.dumps({"name":"习近平"})
        self.postdata['d']=d
        self.postdata['seq']=105
        self.postdata['rseq']=105
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1 and '名称中含有敏感词，请尝试其他名称' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

    def test6_player_changeName_isexsit(self):
        '''名字已存在'''
        d=json.dumps({"name":"你好"})
        self.postdata['d']=d
        self.postdata['seq']=105
        self.postdata['rseq']=105
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1 and '球队名重复' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

if __name__ =='__main__':
    unittest.main()