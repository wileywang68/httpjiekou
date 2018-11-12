# -*- coding:utf-8 -*-
import threading,time,requests,json

url='http://192.168.5.116:8590/user/login'


postdata={
            'd':{},
            'seq':1,
            'rseq':1
        }

def post():
    d = json.dumps({"pwd":"a","capid":"d05f4c5d4a064ce68b040e59fe809cb8","name":"aaa@aaa.com","udid":"d05f4c5d4a064ce68b040e59fe809cb8"})
    postdata['d'] = d
    start = time.time()
    res = requests.post(url,data=postdata)
    if res.status_code!=200:
        print(threading.current_thread().getName() + ' error : ' + str(res.status_code))
    else:
        end = time.time()
        print(threading.current_thread().getName() + ' : ' + str(end - start))

if __name__=='__main__':
    run_time = 60 #执行次数
    thread_count = 100 #并发数
    for x in range(run_time):
        i = 0
        while i < thread_count:
            i += 1
            t = threading.Thread(target=post)
            t.start()