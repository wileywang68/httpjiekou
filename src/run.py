#coding=utf-8
import sys
import unittest
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import src.testcase.tools.HTMLTestRunner
reload(sys)
sys.setdefaultencoding('utf8')

# 用例路径
case_path = os.path.join(os.getcwd())+"/testcase"
case_path1=r'F:\Robot_framework\GAutomator\httpJiekou\src\testcase'

def all_case():
    discover = unittest.defaultTestLoader.discover(case_path1,pattern="test*.py",top_level_dir=None)
    print(discover)
    return discover

if __name__ == '__main__':
    PATH = lambda p: os.path.abspath(p)
    path = PATH(os.getcwd() + "/report").decode('gbk')
    path1 = r'F:\Robot_framework\GAutomator\httpJiekou\src\report'
    fp = open(path1+"/httpreport.html", "wb")
    runner = src.testcase.tools.HTMLTestRunner.HTMLTestRunner(fp, title='接口功能测试报告')
    runner.run(all_case())
