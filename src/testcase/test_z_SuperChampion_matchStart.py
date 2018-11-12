#coding=utf-8
import json
import sys
import unittest
from public.getuserToken import *
from tools.settings import *
import requests

reload(sys)
sys.setdefaultencoding('utf8')

class testMatchStart(unittest.TestCase):

    '''/superChampion/matchStart环球挑战赛比赛'''

    url='http://192.168.5.111:8590/superChampion/matchStart'



    def setUp(self):
        self.postdata={
            'd':{},
            'seq':100,
            'rseq':100,
            't':read_token()
    }
    #
    # @classmethod
    # def setUpClass(cls):
    #     url = 'http://192.168.5.111:8590/superChampion/info'
    #     req = requests.post(url, data=cls.postdata)
    #     cls.sid=req.json()['d']['members'][1]['player']['sid']
    #     cls.id = req.json()['d']['members'][1]['player']['id']

    def test_matchStart(self):
        '''正常参数'''
        d = json.dumps({"sid":1,"id":'npc701b'})
        self.postdata['d'] = d
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)



if __name__ =='__main__':
    unittest.main()