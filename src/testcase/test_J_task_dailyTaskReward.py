#coding=utf-8
import json
import sys
import unittest
from public.getuserToken import *
from tools.settings import *
import requests

reload(sys)
sys.setdefaultencoding('utf8')

class testTaskDailyTaskReward(unittest.TestCase):

    '''/task/dailyTaskReward每日活跃'''

    url='http://192.168.5.111:8590/task/dailyTaskReward'

    def setUp(self):
        self.postdata={
            'd':{},
            'seq':100,
            'rseq':100,
            't':read_token()
        }

    def test1_task_dailyTaskReward(self):
        '''正常参数'''
        d=json.dumps({"taskId":"602"})
        self.postdata['d']=d
        self.postdata['seq']=102
        self.postdata['rseq']=102
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test2_task_dailyTaskReward_isreward(self):
        '''已领取过奖励'''
        d = json.dumps({"taskId":"602"})
        self.postdata['d'] = d
        self.postdata['seq']=103
        self.postdata['rseq'] = 103
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1 and '任务静态表错误' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

    def test3_task_dailyTaskReward_notreward(self):
        '''奖励不可领取'''
        d = json.dumps({"taskId":"608"})
        self.postdata['d'] = d
        self.postdata['seq']=104
        self.postdata['rseq'] = 104
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1 and '任务静态表错误' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

    def test4_task_dailyTaskReward_notexist(self):
        '''奖励不存在id'''
        d = json.dumps({"taskId":"1012323"})
        self.postdata['d'] = d
        self.postdata['seq']=105
        self.postdata['rseq'] = 105
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1 and '任务静态表错误' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

    def test5_task_dailyTaskReward_null(self):
        '''d参数为空'''
        self.postdata['seq']=106
        self.postdata['rseq'] = 106
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1 and '任务静态表错误' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])


if __name__ =='__main__':
    unittest.main()