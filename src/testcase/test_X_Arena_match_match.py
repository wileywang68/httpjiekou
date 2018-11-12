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

class testArenaMatchMatch(unittest.TestCase):

    '''/match/match比赛结束'''

    url='http://192.168.5.111:8590/match/match'

    def setUp(self):
        self.postdata={
            'd':{},
            'seq':100,
            'rseq':100,
            't':read_token()
        }
        url='http://192.168.5.111:8590/arena/info'
        req=requests.post(url,data=self.postdata)
        l=[]
        dicts=req.json()['d']['rivals']
        for k,v in dicts.items():
            l.append(k)

        url1 = 'http://192.168.5.111:8590/arena/match'
        d=json.dumps({"pid":random.choice(l)})
        self.postdata['d']=d
        req=requests.post(url1,data=self.postdata)
        print str(req.text)

    def test1_arena_matchmatch(self):
        '''正常参数'''
        d=json.dumps({"statistics":{"player":{"totalScore":0,"shootOnGoalTimes":0,"foulTimes":0,"score":0,"offsideTimes":0,"cornerTimes":0,"penaltyScore":0,"passing":95,"stealTimes":0,"event":[{"type":2,"time":0.05}],"shootTimes":0,"possession":67,"interceptTimes":0,"passTimes":0},"opponent":{"totalScore":0,"shootOnGoalTimes":0,"foulTimes":0,"score":0,"offsideTimes":0,"cornerTimes":0,"penaltyScore":0,"passing":95,"stealTimes":0,"event":{},"shootTimes":0,"possession":33,"interceptTimes":0,"passTimes":0}},"version":35,"hasFinishedDefenseTraining":1,"isGiveUp":False,"isSkipped":True,"ops":{},"isAuto":1,"isAccelerate":2,"hasFinishedDribbleTraining":1})
        self.postdata['d']=d
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)


if __name__ =='__main__':
    unittest.main()