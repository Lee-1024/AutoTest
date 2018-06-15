# _*_ coding:utf-8 _*_
__author__ = 'Lee'
import unittest
from debug_doc import HTMLTestRunner5
import time

#from testCase import PublisBlog
from debug_doc import test_HTMLTestRunnercn,yhtest


#获取当前时间
now=time.strftime("%Y%m%d%H%S%S",time.localtime())
#定义测试容器
testunit = unittest.TestSuite()
#将测试用例添加到容器中
#testunit.addTest(unittest.makeSuite(PublisBlog.PublishBlog))
#testunit.addTest(unittest.makeSuite(test_HTMLTestRunnercn.test_HTMLTestRunnercn))
testunit.addTest(unittest.makeSuite(yhtest.PublishBlog))

#定义一个报告存放路径
filepath = "D:\\WORK\\AutoTest\\Report\\result"+now+".html"
fp = file(filepath,"wb")
#定义测试报告
runner = HTMLTestRunner5.HTMLTestRunner(title="带截图的测试报告", description="小试牛刀", stream=fp, verbosity=2, retry=1, save_last_try=True)


#执行用例
runner.run(testunit)



