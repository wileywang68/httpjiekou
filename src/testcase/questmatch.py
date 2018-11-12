#coding=utf-8
import json
import sys
import requests
from public.getuserToken import *
reload(sys)
sys.setdefaultencoding('utf8')

class questmatch():


    '''俄罗斯挑战开始_正常参数'''
    def quest_accept(self,qid):
        url = 'http://192.168.5.111:8590/quest/accept'
        d = json.dumps({"qid":qid})
        postdata = {
            'd': d,
            'seq': 101,
            'rseq': 101,
            't': "cbd1da997c99c99afacbb8f7bd69859f"
        }
        req=requests.post(url,data=postdata)
        print req.text
        print 'pass'

    '''俄罗斯挑战结束_正常参数'''
    def match_match(self):
        url='http://192.168.5.111:8590/match/match'
        d = json.dumps({"statistics":{"player":{"totalScore":0,"shootTimes":4,"possession":56,"score":6,"offsideTimes":0,"penaltyScore":0,"passing":95,"cornerTimes":0,"stealTimes":1,"foulTimes":0,"shootOnGoalTimes":4,"interceptTimes":2,"passTimes":15},"opponent":{"totalScore":0,"shootTimes":0,"possession":44,"score":0,"offsideTimes":0,"penaltyScore":0,"passing":77,"cornerTimes":0,"stealTimes":0,"foulTimes":1,"shootOnGoalTimes":0,"interceptTimes":0,"passTimes":14}},"isGiveUp":False,"isSkipped":False,"ops":{"719":{"shoot":{"targetH":1.36452150344849,"target":{"y":-54.9500007629395,"x":2.31561374664307},"duration":0.422879099845886,"id":2,"control":{"y":-47.4159088134766,"x":-0.0296316146850586},"isHigh":False}},"138":{"manual":{"manualPassTargetPosition":{"y":-31.3652572631836,"x":-0.13006591796875},"passType":"Ground","id":1,"type":4,"targetOnfieldId":9}},"383":{"shoot":{"targetH":1.29935526847839,"target":{"y":-54.9500007629395,"x":-2.11808967590332},"duration":0.736299335956573,"id":2,"control":{"y":-42.9348678588867,"x":0.401915550231934},"isHigh":False}},"189":{"shoot":{"targetH":1.23912453651428,"target":{"y":-54.9500007629395,"x":-1.77722358703613},"duration":0.186165302991867,"id":9,"control":{"y":-53.6566200256348,"x":-5.08354949951172},"isHigh":False}},"296":{"manualDefense":{"type":0}},"906":{"shoot":{"targetH":1.9695999622345,"target":{"y":-54.9500007629395,"x":-1.17476892471313},"duration":0.855904877185822,"id":1,"control":{"y":-40.1471328735352,"x":-1.56994128227234},"isHigh":False}},"691":{"manual":{"manualPassTargetPosition":{"y":-32.5698165893555,"x":-5.56451416015625},"passType":"Ground","id":11,"type":4,"targetOnfieldId":3}}},"hashKey":51296554,"version":22})
        postdata = {
            'd': d,
            'seq': 102,
            'rseq': 102,
            't': "cbd1da997c99c99afacbb8f7bd69859f"
        }
        req=requests.post(url,data=postdata)
        print req.text
        print 'pass'

    '''环球挑战信息_正常参数'''
    def quest_goon(self,qid):
        url='http://192.168.5.111:8590/quest/goon'
        d = json.dumps({"qid": qid})
        postdata = {
            'd': d,
            'seq': 103,
            'rseq': 103,
            't': "cbd1da997c99c99afacbb8f7bd69859f"
        }
        req=requests.post(url,data=postdata)
        print req.text
        print 'pass'


    '''环球挑战领取奖励_正常参数'''
    def quest_info(self):
        url='http://192.168.5.111:8590/quest/info'
        postdata = {
            'd': {},
            'seq': 104,
            'rseq': 104,
            't': "cbd1da997c99c99afacbb8f7bd69859f"
        }
        req=requests.post(url,data=postdata)
        print req.text
        print 'pass'


    def readquest(self):
        path="./tools/quest.txt"
        list1=[]
        with open(path, "r") as fs:  # 读取quest
            for i in fs.readlines():
                list1.append(i.strip())
        return list1

if __name__ =='__main__':
    q=questmatch()
    for qid in q.readquest():
        q.quest_accept(qid)
        q.match_match()
        q.quest_goon(qid)
        q.quest_info()
