#coding=utf-8
import json
import sys
import unittest
from public.getuserToken import *
from tools.settings import *
import requests

reload(sys)
sys.setdefaultencoding('utf8')

class testMatch(unittest.TestCase):

    '''/match/match俄罗斯比赛结束'''

    url='http://192.168.5.111:8590/match/match'

    def setUp(self):
        self.postdata={
            'd':{},
            'seq':100,
            'rseq':100,
            't':read_token()
        }
        d = json.dumps({"qid": "Q101"})
        self.postdata['d'] = d
        url='http://192.168.5.111:8590/quest/accept'
        req = requests.post(url, data=self.postdata)

    def test1_match_match(self):
        '''正常参数'''
        d=json.dumps({"statistics":{"player":{"totalScore":0,"shootTimes":1,"possession":98,"score":3,"offsideTimes":0,"penaltyScore":0,"passing":95,"cornerTimes":0,"stealTimes":0,"foulTimes":0,"shootOnGoalTimes":1,"interceptTimes":0,"passTimes":4},"opponent":{"totalScore":0,"shootTimes":0,"possession":2,"score":0,"offsideTimes":0,"penaltyScore":0,"passing":95,"cornerTimes":0,"stealTimes":0,"foulTimes":0,"shootOnGoalTimes":0,"interceptTimes":0,"passTimes":0}},"isGiveUp":False,"isSkipped":True,"ops":{"96":{"shoot":{"targetH":1.67423319816589,"target":{"y":-54.9500007629395,"x":2.63899326324463},"duration":0.585655450820923,"id":2,"control":{"y":-45.210090637207,"x":4.20061683654785},"isHigh":False}}},"version":22})
        self.postdata['d']=d
        self.postdata['seq']=101
        self.postdata['rseq']=101
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test2_match_match_d_null(self):
        '''d参数为空'''
        self.postdata['d'] = {}
        self.postdata['seq']=102
        self.postdata['rseq'] = 102
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

    def test3_match_match_d_error(self):
        '''d参数错误'''
        d = json.dumps({"statistics": {"player": {"totalSc": 22}}})
        self.postdata['d'] = d
        self.postdata['seq']=103
        self.postdata['rseq'] = 103
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])


if __name__ =='__main__':
    unittest.main()