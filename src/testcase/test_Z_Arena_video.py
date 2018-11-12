#coding=utf-8
import json
import sys
import unittest
from public.getuserToken import *
from tools.settings import *
import requests

reload(sys)
sys.setdefaultencoding('utf8')

class testArenaVideo(unittest.TestCase):

    '''/arena/video天梯比赛回放'''

    url='http://192.168.5.111:8590/arena/video'

    postdata={
            'd':{},
            'seq':100,
            'rseq':100,
            't':read_token()
    }

    @classmethod
    def setUpClass(cls):
        url = 'http://192.168.5.111:8590/arena/record'
        req=requests.post(url,data=cls.postdata)
        cls.vid=req.json()['d']['record'][0]['vid']

    def test1_arena_video(self):
        '''正常参数'''
        d=json.dumps({"videoID":self.vid})
        self.postdata['d']=d
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test2_arena_video_vidnull(self):
        '''videoID为空'''
        d = json.dumps({"videoID": ""})
        self.postdata['d'] = d
        req=requests.post(self.url,data=self.postdata)
        print str(req.text)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)


    def test3_arena_video_viderror(self):
        '''videoid错误'''
        d=json.dumps({"videoID":"sadklfjkdasfs"})
        self.postdata['d']=d
        req=requests.post(self.url,data=self.postdata)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)

    def test4_arena_video_vidint(self):
        '''videoid错误'''
        d=json.dumps({"videoID":11})
        self.postdata['d']=d
        req=requests.post(self.url,data=self.postdata)
        print str(req.text)
        if (req.json()['r'] == 1):
            raise AssertionError(req.json()['d'])
        else:
            print '测试通过', str(req.text)


if __name__ =='__main__':
    unittest.main()