#coding=utf-8
import json
import sys
import unittest
import requests
from public.getuserToken import *
from tools.settings import *

reload(sys)
sys.setdefaultencoding('utf8')

class testworld(unittest.TestCase):

    '''/wcg/match环球挑战'''

    def setUp(self):
        self.postdata={
            'd':{},
            'seq':101,
            'rseq':101,
            't':read_token()
        }
        '''环球挑战开始_正常参数'''
        url = 'http://192.168.5.111:8590/wcg/match'
        d = json.dumps({"id":"W101"})
        self.postdata['d']=d
        req=requests.post(url,data=self.postdata)

    def test2_match_match(self):
        '''环球挑战结束_正常参数'''
        url = 'http://192.168.5.111:8590/match/match'
        d = json.dumps({"statistics":{"player":{"totalScore":0,"shootTimes":1,"possession":99,"score":1,"offsideTimes":0,"penaltyScore":0,"passing":95,"cornerTimes":0,"stealTimes":0,
                        "foulTimes":0,"shootOnGoalTimes":1,"interceptTimes":0,"passTimes":7},"opponent":{"totalScore":0,"shootTimes":0,"possession":1,"score":0,"offsideTimes":0,"penaltyScore":0,"passing":95,"cornerTimes":0,
                        "stealTimes":0,"foulTimes":0,"shootOnGoalTimes":0,"interceptTimes":0,"passTimes":0}},"isGiveUp":False,"isSkipped":True,"ops":{"76":{"manual":{"manualPassTargetPosition":
                       {"y":7.20670700073242,"x":-23.0613403320313},"passType":"Ground","id":9,"type":4,"targetOnfieldId":11}},"176":{"manual":{"manualPassTargetPosition":{"y":-40.2878265380859,"x":-1.04522705078125},"passType":"Ground","id":3,"type":4,"targetOnfieldId":3}},
                       "189":{"shoot":{"targetH":1.6879825592041,"target":{"y":-54.9500007629395,"x":-3.02439951896667},"duration":0.375767827033997,"id":2,"control":{"y":-48.340747833252,"x":-0.719809591770172},
                       "isHigh":False}},"105":{"manual":{"manualPassTargetPosition":{"y":-3.66838264465332,"x":-9.23193359375},"passType":"Ground","id":10,"type":4,"targetOnfieldId":6}},"132":{"manual":{"manualPassTargetPosition":{"y":-21.2978553771973,"x":10.5756225585938},
                       "passType":"High","id":5,"type":4,"targetOnfieldId":2}},"157":{"manual":{"manualPassTargetPosition":{"y":-25.5908012390137,"x":5.91009521484375},"passType":"Ground","id":1,"type":4,"targetOnfieldId":4}}},"version":17
                        })
        self.postdata['d']=d
        self.postdata['seq']=102
        self.postdata['rseq']=102
        req=requests.post(url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test3_wcg_info(self):
        '''环球挑战信息_正常参数'''
        url='http://192.168.5.111:8590/wcg/info'
        self.postdata['seq'] = 103
        self.postdata['rseq'] = 103
        req=requests.post(url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test4_wcg_autoReward(self):
        '''环球挑战领取奖励_正常参数'''
        url='http://192.168.5.111:8590/wcg/autoReward'
        self.postdata['seq'] = 104
        self.postdata['rseq'] = 104
        req=requests.post(url,data=self.postdata)
        if (req.json()['r'] == 1 and '奖励不存在' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

if __name__ =='__main__':
    unittest.main()