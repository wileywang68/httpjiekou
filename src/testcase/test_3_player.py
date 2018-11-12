#coding=utf-8
import json
import sys
import unittest
from public.getuserToken import *
from tools.settings import *
import requests

reload(sys)
sys.setdefaultencoding('utf8')

class testPlayer(unittest.TestCase):

    '''/player玩家详细信息'''

    url='http://192.168.5.111:8590/player'

    def setUp(self):
        self.postdata={
            'd':{},
            'seq':100,
            'rseq':100,
            't':read_token()
        }

    def test1_player_pass(self):
        '''正常参数'''
        d = json.dumps({"plat":"WindowsEditor","flags":["lang_zh-Hans","font_FZLTH"],"capid":"d05f4c5d4a064ce68b040e59fe809cb8","jsonUpdate":{},"ver":{"editor":2147483647}})
        self.postdata['d']=d
        req=requests.post(self.url,data=self.postdata)
        print str(req.text)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过',str(req.text)

    def test2_player_d_null(self):
        '''d参数为空'''
        self.postdata['d'] = {}
        self.postdata['seq'] = 101
        self.postdata['rseq'] = 101
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1 and '设备号错误' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

if __name__ =='__main__':
    unittest.main()