#coding=utf-8
import json
import sys
import requests

reload(sys)
sys.setdefaultencoding('utf8')

class world():


    '''环球挑战开始_正常参数'''
    def wcg_match(self,s):
        url = 'http://192.168.5.111:8590/wcg/match'
        d = json.dumps({"id":s})
        postdata = {
            'd': d,
            'seq': 101,
            'rseq': 101,
            't': '0b5b1b11eaea62b0aa7e000be756c0f4'
        }
        req=requests.post(url,data=postdata)
        print req.text
        print 'pass'

    '''环球挑战结束_正常参数'''
    def match_match(self):
        url='http://192.168.5.111:8590/match/match'
        d = json.dumps({"statistics":{"player":{"totalScore":0,"shootTimes":1,"possession":99,"score":1,"offsideTimes":0,"penaltyScore":0,"passing":95,"cornerTimes":0,"stealTimes":0,"foulTimes":0,"shootOnGoalTimes":1,"interceptTimes":0,"passTimes":7},"opponent":{"totalScore":0,"shootTimes":0,"possession":1,"score":0,"offsideTimes":0,"penaltyScore":0,"passing":95,"cornerTimes":0,"stealTimes":0,"foulTimes":0,"shootOnGoalTimes":0,"interceptTimes":0,"passTimes":0}},
                        "isGiveUp":False,"isSkipped":True,"ops":{"76":{"manual":{"manualPassTargetPosition":{"y":7.20670700073242,"x":-23.0613403320313},"passType":"Ground","id":9,"type":4,"targetOnfieldId":11}},"176":{"manual":{"manualPassTargetPosition":{"y":-40.2878265380859,"x":-1.04522705078125},"passType":"Ground","id":3,"type":4,"targetOnfieldId":3}},"189":{"shoot":{"targetH":1.6879825592041,"target":{"y":-54.9500007629395,"x":-3.02439951896667},"duration":0.375767827033997,"id":2,"control":{"y":-48.340747833252,"x":-0.719809591770172},
                                                                                                                                                                                                                                                                                                                                                                                    "isHigh":False}},"105":{"manual":{"manualPassTargetPosition":{"y":-3.66838264465332,"x":-9.23193359375},"passType":"Ground","id":10,"type":4,"targetOnfieldId":6}},"132":{"manual":{"manualPassTargetPosition":{"y":-21.2978553771973,"x":10.5756225585938},"passType":"High","id":5,"type":4,"targetOnfieldId":2}},"157":{"manual":{"manualPassTargetPosition":{"y":-25.5908012390137,"x":5.91009521484375},"passType":"Ground","id":1,"type":4,"targetOnfieldId":4}}},"version":17})
        postdata = {
            'd': d,
            'seq': 102,
            'rseq': 102,
            't': '0b5b1b11eaea62b0aa7e000be756c0f4'
        }
        req=requests.post(url,data=postdata)
        print req.text
        print 'pass'

    '''环球挑战信息_正常参数'''
    def wcg_info(self):
        url='http://192.168.5.111:8590/wcg/info'
        postdata = {
            'd': {},
            'seq': 103,
            'rseq': 103,
            't': '0b5b1b11eaea62b0aa7e000be756c0f4'
        }
        req=requests.post(url,data=postdata)
        print req.text
        print 'pass'


    '''环球挑战领取奖励_正常参数'''
    def wcg_autoReward(self):
        url='http://192.168.5.111:8590/wcg/autoReward'
        postdata = {
            'd': {},
            'seq': 104,
            'rseq': 104,
            't': '0b5b1b11eaea62b0aa7e000be756c0f4'
        }
        req=requests.post(url,data=postdata)
        print req.text
        print 'pass'




if __name__ =='__main__':
    for i in range(1,101):
        s="W10"+str(i)
        w=world()
        w.wcg_match(s)
        w.match_match()
        w.wcg_info()
        w.wcg_autoReward()