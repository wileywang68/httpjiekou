#coding=utf-8
import json
import sys
import requests
reload(sys)
sys.setdefaultencoding('utf8')


def getuser(name,passowrd):
    url="http://192.168.5.116:8590/user/login"
    d=json.dumps({"pwd":passowrd,"capid":"d05f4c5d4a064ce68b040e59fe809cb8","name":name,"udid":"d05f4c5d4a064ce68b040e59fe809cb8"})
    postdata={
        "d":d,
        "seq":1,
        "rseq":1
    }
    req=requests.post(url,data=postdata)
    token= req.json()["d"]["uinfo"]["token"]
    capstoneID= req.json()["d"]["uinfo"]["capstoneID"]
    cuid= req.json()["d"]["cuid"]
    res=(token,capstoneID,cuid)
    return res


def getuserToken(name,password):
    res=getuser(name,password)
    url="http://192.168.5.111:8590/a/login"
    d=json.dumps({"uinfo":
                  {
                      "token":res[0],
                      "capstoneID":res[1]
                  },
                    "channel":"capstone",
                    "bichannel":"capstone",
                    "cuid":res[2],
                    "capid":"d05f4c5d4a064ce68b040e59fe809cb8",
                    "pf":"capstone",
                    "udid":"d05f4c5d4a064ce68b040e59fe809cb8"})
    postdata = {
        "d": d,
        "seq": 2,
        "rseq": 2
    }
    req=requests.post(url,data=postdata)
    token= req.json()['d']['servers'][0]['player']['token']
    return token

# def json_txt(dic_json):
#     tokens=dic_json['dev']['db']['Player']['findOne'].keys()[0]
#     token=eval(tokens)
#     return token['token']
#
# def getuserToken(name,password):
#     url='http://192.168.5.111:8590/player/homepage'
#     postdata = {
#         "d": {},
#         "seq": 3,
#         "rseq": 3,
#         "t":getuserToken1(name,password)
#     }
#     req=requests.post(url,data=postdata)
#     token=json_txt(req.json())
#     return token

def save_token(name,password):
    token=getuserToken(name, password)
    f=open('token.txt','wb')
    f.write(token)
    f.close()


def read_token():
    f=open(r'F:\Robot_framework\GAutomator\httpJiekou\src\testcase\public\token.txt','r')
    token=f.readline()
    f.close()
    return token

#print read_token()


#save_token("ddd@ddd.com","d")




