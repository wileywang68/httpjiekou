#coding=utf-8
import json
import sys
import unittest
from public.getuserToken import *
from tools.settings import *
import requests

reload(sys)
sys.setdefaultencoding('utf8')

class testGuildMultirequest(unittest.TestCase):

    '''/guild/multiRequest'''

    url='http://192.168.5.111:8590/guild/multiRequest'

    def setUp(self):
        self.postdata={
            'd':{},
            'seq':100,
            'rseq':100,
            't':read_token()
        }

    def test1_guild_multiRequest(self):
        '''正常参数'''
        d=json.dumps({"gidArray":["5ad8378de13823291d7e7170","5ad985bbe1382352245fee37","5adf806ae1382357520d4263","5adafff8e13823522168e798","5ad80c80e138230c5c318500","5ad86cc7e1382321a1138f85","5ad8902ae13823521a37c836","5ad8a4b7e13823521d28cf59","5ad87ac6e1382323ef3c9023","5ad9eacce1382352165daf81","5ad86c54e1382321a7289423","5adcb3f6e13823789e372856","5adcb4ffe13823789b7dbcc7","5adcbd75e138237898082b48","5adcdfd7e138237892295b4c","5adce710e1382378a21d37db","5adda948e1382378a21d37de","5ada0c00e13823522942b37f"]})
        self.postdata['d']=d
        self.postdata['seq']=101
        self.postdata['rseq']=101
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test2_guild_multiRequest(self):
        '''错误参数'''
        d=json.dumps({"gidArray":["sdsd"]})
        self.postdata['d']=d
        self.postdata['seq']=102
        self.postdata['rseq']=102
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test3_guild_multiRequest_d(self):
        '''d参数错误'''
        self.postdata['d'] = 1
        self.postdata['seq']=103
        self.postdata['rseq'] = 103
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test4_guild_multiRequest_null(self):
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