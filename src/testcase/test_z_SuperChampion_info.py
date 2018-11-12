#coding=utf-8
import json
import sys
import unittest
from public.getuserToken import *
from tools.settings import *
import requests

reload(sys)
sys.setdefaultencoding('utf8')

class testSuperChampionInfo(unittest.TestCase):

    '''/superChampion/info环球挑战赛信息'''

    url='http://192.168.5.111:8590/superChampion/info'

    postdata={
            'd':{},
            'seq':100,
            'rseq':100,
            't':read_token()
    }

    def test1_superChampion_info(self):
        '''正常参数'''
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

if __name__ =='__main__':
    unittest.main()