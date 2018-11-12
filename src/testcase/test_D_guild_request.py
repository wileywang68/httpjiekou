#coding=utf-8
import json
import sys
import unittest
from public.getuserToken import *
from tools.settings import *
import requests

reload(sys)
sys.setdefaultencoding('utf8')

class testGuildRequest(unittest.TestCase):

    '''/guild/request联盟申请'''

    url='http://192.168.5.111:8590/guild/request'

    def setUp(self):
        self.postdata={
            'd':{},
            'seq':100,
            'rseq':100,
            't':read_token()
        }

    def test1_guild_request(self):
        '''正常参数'''
        d=json.dumps({"gid":"5ad86cc7e1382321a1138f85"})
        self.postdata['d']=d
        self.postdata['seq']=101
        self.postdata['rseq']=101
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test2_guild_request_derror(self):
        '''错误参数'''
        d=json.dumps({"gid":"sdsd"})
        self.postdata['d']=d
        self.postdata['seq']=102
        self.postdata['rseq']=102
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test3_guild_request_d(self):
        '''d参数错误'''
        self.postdata['d'] = 1
        self.postdata['seq']=103
        self.postdata['rseq'] = 103
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test4_guild_request_null(self):
        '''d参数为空'''
        self.postdata['seq']=104
        self.postdata['rseq'] = 104
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)



if __name__ =='__main__':
    unittest.main()