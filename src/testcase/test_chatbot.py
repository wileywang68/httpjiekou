#coding=utf-8
import json
import sys
import unittest
import requests
from public.getuserToken import *
from tools.settings import *

reload(sys)
sys.setdefaultencoding('utf8')

class testChatbot(unittest.TestCase):

    '''/wcg/match环球挑战'''
    url='http://192.168.141.143/token'
    def setUp(self):
        self.postdata={
                "game_id": 10389,
                "ts": 1536544125,
                "openid":"2249408860"
             }
        self.header={
            "User-Agent": "IdreamChat/1.0(android:4.4.2;appkey:e19081b4527963d70c7a;game_type:1;channel:TEST0000000;app_version:1.0;package:com.kiloo.subwaysurf;sdk_version:pay-1.0.0.0;network:wifi;device_brand:Honor;device_model:HONOR H30-L01;udid:3q1q11n1_3229119054873088411r950;lang:zh_CN;local_time:20180909143129+0800);",
            "Content-Type": "application/json"
            }

    def test2_match_match(self):
        '''环球挑战结束_正常参数'''

        print self.header
        print self.postdata
        req=requests.post(self.url,data=self.postdata,headers=self.header)
        print req.headers
        print str(req.text)



if __name__ =='__main__':
    unittest.main()