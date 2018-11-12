#coding=utf-8
import json
import sys
import unittest
from public.getuserToken import *
from tools.settings import *
import requests

reload(sys)
sys.setdefaultencoding('utf8')

class testPayPaytest(unittest.TestCase):

    '''/pay/payTest商城购买钻石'''

    url='http://192.168.5.111:8590/pay/payTest'

    def setUp(self):
        self.postdata={
            'd':{},
            'seq':100,
            'rseq':100,
            't':read_token()
        }

    def test1_pay_payTest(self):
        '''正常参数'''
        d=json.dumps({"productId":"cn.capstones.igoal2.d648"})
        self.postdata['d']=d
        self.postdata['seq']=101
        self.postdata['rseq']=101
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test2_pay_payTest(self):
        '''错误参数'''
        d=json.dumps({"productId":"cn.capstones.igoal2.d99999"})
        self.postdata['d']=d
        self.postdata['seq']=102
        self.postdata['rseq']=102
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1 or req.status_code!=200):
            print req.status_code
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test3_pay_payTest_d_error(self):
        '''d参数错误'''
        self.postdata['d'] = 1
        self.postdata['seq']=103
        self.postdata['rseq'] = 103
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1 and '网络不稳定' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

    def test4_pay_payTest_null(self):
        '''d参数为空'''
        self.postdata['seq']=104
        self.postdata['rseq'] = 104
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test5_pay_payTest(self):
        '''d参数68'''
        d=json.dumps({"productId":"cn.capstones.igoal2.f68","sid":1,"pid":"5adc929ce13823789518e603"})
        self.postdata['d']=d
        self.postdata['seq']=105
        self.postdata['rseq'] = 105
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1 and '网络不稳定' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])


if __name__ =='__main__':
    unittest.main()