#_*_ coding:utf-8 _*_
__author__ = 'Lee'
import unittest
import HTMLTestRunner5
import time

from testCase import CP_ProductControl,CP_CompanyControl,CP_Banner

#获取当前时间
now=time.strftime("%Y%m%d%H%S%S",time.localtime())
#定义测试容器
testunit = unittest.TestSuite()
#将测试用例添加到容器中
testunit.addTest(unittest.makeSuite(CP_ProductControl.ProductControl))
testunit.addTest(unittest.makeSuite(CP_CompanyControl.CompanyControl))
testunit.addTest(unittest.makeSuite(CP_Banner.Banner))
#定义一个报告存放路径
filepath = "C:\\AutoTestNew\\AutoTest\\ControlPanel\\Report\\result"+now+".html"
fp = file(filepath,"wb")
#定义测试报告
runner = HTMLTestRunner5.HTMLTestRunner(title="控制面板测试报告", description="控制面板相关功能测试", stream=fp, verbosity=2, retry=1, save_last_try=True)

#执行用例
runner.run(testunit)