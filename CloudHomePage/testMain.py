# _*_ coding:utf-8 _*_
__author__ = 'Lee'
import unittest
from debug_doc import HTMLTestRunner5
import time



#获取当前时间
now=time.strftime("%Y%m%d%H%S%S",time.localtime())
#定义测试容器
testunit = unittest.TestSuite()
#将测试用例添加到容器中


#定义一个报告存放路径
filepath = "D:\\AutoTest\\CloudHomePage\\Report\\result"+now+".html"
fp = file(filepath,"wb")
#定义测试报告
runner = HTMLTestRunner5.HTMLTestRunner(title="测试报告", description="主流程测试报告", stream=fp, verbosity=2, retry=1, save_last_try=True)

#执行用例
runner.run(testunit)






