# -*- coding: utf-8 -*-
from pymongo import MongoClient
import json

def read_userdata():
    # 连接mongodb数据库
    client = MongoClient(host="192.168.5.116", port=60001)
    # 连接mydb数据库,账号密码认证
    db = client.mydb
    db.authenticate("capstone", "capstone$cgoal#2017")
    # 连接表
    collection = db.myset

    # 查看全部表名称
    db.collection_names()
    print db.collection_names()



read_userdata()