#coding=utf-8
import json
import sys
import unittest
import requests
from tools.settings import *

reload(sys)
sys.setdefaultencoding('utf8')

class testUserLogin(unittest.TestCase):

    '''user/login用户登录'''

    url='http://192.168.5.116:8590/user/login'

    def setUp(self):
        self.postdata={
            'd':{},
            'seq':1,
            'rseq':1
        }

    def test1_userlogin(self):
        '''正常参数'''
        d = json.dumps({"pwd":"c","capid":"d05f4c5d4a064ce68b040e59fe809cb8","name":"ccc@ccc.com","udid":"d05f4c5d4a064ce68b040e59fe809cb8"})
        self.postdata['d']=d
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test2_userlogin_nameerror(self):
        '''账号格式错误'''
        d = json.dumps({"pwd":"4","capid":"d05f4c5d4a064ce68b040e59fe809cb8","name":"asdfasfdasfds","udid":"d05f4c5d4a064ce68b040e59fe809cb8"})
        self.postdata['d']=d
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1 and ('用户名格式错误' in req.json()['d'])):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

    def test3_userlogin_name_notexsit(self):
        '''账号错误'''
        d = json.dumps({"pwd": "4", "capid": "d05f4c5d4a064ce68b040e59fe809cb8", "name": "akd@sdkf.com",
                        "udid": "d05f4c5d4a064ce68b040e59fe809cb8"})
        self.postdata['d'] = d
        req = requests.post(self.url, data=self.postdata)
        if (req.json()['r'] == 1 and '用户不存在' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

    def test4_userlogin_passworderror(self):
        '''密码错误'''
        d = json.dumps({"pwd":"4","capid":"d05f4c5d4a064ce68b040e59fe809cb8","name":"ccc@ccc.com","udid":"d05f4c5d4a064ce68b040e59fe809cb8"})
        self.postdata['d']=d
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1 and '密码错误，请重试' in req.json()['d']):
            print '测试通过', str(req.text)
        else:
            raise AssertionError(req.json()['d'])

if __name__ =='__main__':
    unittest.main()