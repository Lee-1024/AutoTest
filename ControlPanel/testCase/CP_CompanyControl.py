#_*_ coding:utf-8 _*_
__author__ = 'Lee'
import sys
import os
currentUrl = os.path.dirname(__file__)
parentUrl = os.path.abspath(os.path.join(currentUrl, os.pardir))
sys.path.append(parentUrl)
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import unittest,time,uuid
import urllib
from Common.Common import CommonMethod
from Common.Logger import Log

class CompanyControl(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.imgs = []
        self.comme = CommonMethod()
        self.log = Log()

    def add_img(self):
        #截图添加到测试报告中的方法
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def setup_get(self):
        self.driver.get(self.comme.url)
        self.driver.maximize_window()


    def test_product(self):
        u'''公司管理'''
        companyname = u'测试厂商-'+str(uuid.uuid1())[0:8]
        self.setup_get()
        #点击云产品
        self.driver.find_element_by_xpath('//div[@class="side-list-root"]/nav/div[4]').click()
        time.sleep(0.5)
        #点击公司管理
        self.driver.find_element_by_xpath('//div[@class="side-list-root"]/nav/div[5]/div/div/div/div[1]/div/span').click()
        time.sleep(0.5)
        #点击添加
        self.driver.find_element_by_xpath('//div[@class="root-main-view"]/div/div[1]/div/button').click()
        time.sleep(0.5)
        #输入厂商名称
        self.driver.find_element_by_xpath('//div[@class="companyCon"]/p[1]/label/input').send_keys(companyname)
        time.sleep(0.5)
        #输入官网地址
        self.driver.find_element_by_xpath('//div[@class="companyCon"]/p[2]/label/input').send_keys(u'www.baidu.com')
        time.sleep(0.5)
        #上传图片
        self.driver.find_element_by_xpath('//div[@class="uploadCon"]/input[2]').send_keys('C:\\Users\\Bill\\Desktop\\google.jpg')
        time.sleep(0.5)
        #输入厂商描述
        self.driver.find_element_by_xpath('//div[@class="companyCon"]/p[4]/label/textarea').send_keys(u'厂商描述')
        time.sleep(0.5)
        #点击保存
        self.driver.find_element_by_xpath('//div[@class="ant-modal-content"]/div[3]/button').click()
        time.sleep(3.5)
        #获取当初厂商ID
        text = self.driver.find_element_by_xpath('//div[@class="root-main-view"]/div/table/tbody/tr[1]/td[1]').text
        #通过ID打开该厂商链接
        self.driver.get('https://stg.hnacloudmarket.com/cloudLibrary/company/%s'%text)
        time.sleep(2)
        text1 = self.driver.find_element_by_xpath('//div[@class="main-div"]/div[1]/div/div/div[1]/div[1]/div[1]/div/div').text
        self.assertIn(u'厂商',text1)

        time.sleep(3)


if __name__ == '__main__':
    unittest.main()