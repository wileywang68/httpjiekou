#coding=utf-8
import json
import sys
import unittest
from public.getuserToken import *
from tools.settings import *
import requests

reload(sys)
sys.setdefaultencoding('utf8')

class testTransferBid(unittest.TestCase):

    '''/transfer/bid转会市场'''

    url='http://192.168.5.111:8590/transfer/bid'

    def setUp(self):
        d = json.dumps({"cid":"Saguero"})
        self.postdata={
            'd':d,
            'seq':100,
            'rseq':100,
            't':read_token()
        }
        url="http://192.168.5.111:8590/transfer/specificProduct"
        req = requests.post(url, data=self.postdata)
        self.itemPeriodId=req.json()['d']['list'][0]['itemPeriodId']
        self.priceType=req.json()['d']['list'][0]['priceType']
        self.bidPrice=req.json()['d']['list'][0]['bidPrice']

    def test1_transfer_bid(self):
        '''正常参数'''
        d=json.dumps({"itemPeriodId":self.itemPeriodId,"bidPrice":self.bidPrice,"priceType":self.priceType})
        self.postdata['d']=d
        self.postdata['seq']=101
        self.postdata['rseq']=101
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test2_transfer_bid_null(self):
        '''d参数为空'''
        self.postdata['d'] = {}
        self.postdata['seq']=102
        self.postdata['rseq'] = 102
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1 and '客户端数据错误，请稍后重试' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

    def test3_transfer_bid_d_error(self):
        '''d参数错误'''
        self.postdata['d'] = 2
        self.postdata['seq']=103
        self.postdata['rseq'] = 103
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1 and '客户端数据错误，请稍后重试' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

    def test4_transfer_bid_pricetypeerror(self):
        '''dpricetype错误'''
        d=json.dumps({"itemPeriodId":self.itemPeriodId,"bidPrice":self.bidPrice,"priceType":"s"})
        self.postdata['d']=d
        self.postdata['seq']=104
        self.postdata['rseq']=104
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 0):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test5_transfer_bid_itemPeriodIderror(self):
        '''ditemPeriodId错误'''
        d=json.dumps({"itemPeriodId":"sddsfs","bidPrice":self.bidPrice,"priceType":"d"})
        self.postdata['d']=d
        self.postdata['seq']=105
        self.postdata['rseq']=105
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 0):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test6_transfer_bid_bidPriceerror(self):
        '''dbidPrice错误'''
        d=json.dumps({"itemPeriodId":self.itemPeriodId,"bidPrice":1000,"priceType":"d"})
        self.postdata['d']=d
        self.postdata['seq']=106
        self.postdata['rseq']=106
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 0):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

if __name__ =='__main__':
    unittest.main()