# _*_ coding:utf-8 _*_
__author__ = 'Lee'
import unittest
#from debug_doc import HTMLTestRunner5
import HTMLTestRunner5
import time

from testCase import TitleSpan,Product,Shopping,Company,OnlinePlay,OtherTest,ToBuy

#获取当前时间
now=time.strftime("%Y%m%d%H%S%S",time.localtime())
#定义测试容器
testunit = unittest.TestSuite()
#将测试用例添加到容器中
#testunit.addTest(unittest.makeSuite(TitleSpan.TitleSpan))
#testunit.addTest(unittest.makeSuite(Shopping.Shopping))
#testunit.addTest(unittest.makeSuite(OnlinePlay.OlinePlay))
#testunit.addTest(unittest.makeSuite(Product.Product))
#testunit.addTest(unittest.makeSuite(Company.Company))
testunit.addTest(unittest.makeSuite(ToBuy.ToBuy))
#testunit.addTest(unittest.makeSuite(OtherTest.OtherTest))
#定义一个报告存放路径
filepath = "C:\\AutoTestNew\\AutoTest\\CloudHomePage\\Report\\result"+now+".html"
fp = file(filepath,"wb")
#定义测试报告
runner = HTMLTestRunner5.HTMLTestRunner(title="主页测试报告", description="主页链接跳转测试", stream=fp, verbosity=2, retry=1, save_last_try=True)

#执行用例
runner.run(testunit)






