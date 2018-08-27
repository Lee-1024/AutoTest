#_*_ coding:utf-8 _*_
__author__ = 'Lee'
import sys
import os
currentUrl = os.path.dirname(__file__)
parentUrl = os.path.abspath(os.path.join(currentUrl, os.pardir))
sys.path.append(parentUrl)
from selenium import webdriver
import unittest,time
from Common.Common import CommonMethod
from Common.Logger import Log
class Company(unittest.TestCase):

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
        self.driver.find_element_by_class_name('apsClose').click()

    def wall_step(self,page,counts):
        """
        :param page:验证第几页的logo墙
        :param counts:当前页有几个logo
        :return:logo墙测试方法，无返回值
        """
        self.comme.roll('//div[@class="company-prefecture-two-content"]/div[5]',self.driver)

        time.sleep(0.8)
        for i in range(1,counts+1):
            self.comme.hover('//div[@class="company-prefecture-three-div"]/div/div[1]',self.driver)
            time.sleep(0.1)

            self.driver.find_element_by_xpath('//div[@class="company-prefecture-three-div-number"]/div[%d]/div'%page).click()
            time.sleep(2)
            self.comme.hover('//div[@class="company-prefecture-three-div"]/div/div[%d]'%i,self.driver)
            try:
                self.driver.find_element_by_xpath('//div[@class="company-prefecture-three-div"]/div/div[%d]'%i).click()
            except Exception as e:
                self.log.error(e)
                self.driver.find_element_by_xpath('//div[@class="company-prefecture-three-div-number"]/div[%d]/div'%page).click()
                time.sleep(1.8)
                self.driver.find_element_by_xpath('//div[@class="company-prefecture-three-div"]/div/div[%d]'%i).click()
            time.sleep(1)
            self.add_img()
            self.driver.back()

    def test_company_1_ex(self):
        u"""金山云"""
        self.setup_get()
        time.sleep(1)
        self.comme.roll('//div[@class="company-prefecture-title"]',self.driver)
        self.driver.find_element_by_xpath('//div[@class="company-prefecture-content-title-div"]/div[2]/button').click()
        self.add_img()
        text1 = self.driver.find_element_by_xpath('//div[@class="main-div"]/div[1]/div/div/div[1]/div[1]/div[1]/div/div').text
        self.assertIn(u'金山',text1)
        self.driver.back()

    def test_company_1_com(self):
        u"""金山云服务器，弹性IP，WPS+云办公"""
        self.setup_get()
        checklist=(u'服务器',u'弹性',u'云办公')
        for i in range(1,4):
            self.comme.roll('//div[@class="company-prefecture-title"]',self.driver)
            self.driver.find_element_by_xpath('//div[@class="company-prefecture-content-title-div-middle"]/div[%d]'%i).click()
            time.sleep(0.5)
            self.add_img()
            text2 = self.driver.find_element_by_xpath('//div[@class="product-item-title"]/span').text
            self.assertIn(checklist[i-1],text2)

            self.driver.back()

    def test_company_2(self):
        u"""微软，今目标，阿里云，腾讯云，华为云，绿盟，并行，云势"""
        self.setup_get()
        checklist=(u'微软',u'今目标',u'阿里云',u'腾讯云',u'华为云',u'绿盟',u'并行',u'云势')
        self.comme.roll('//div[@class="company-prefecture-title"]',self.driver)
        for i in range(1,9):
            self.driver.find_element_by_xpath('//div[@class="company-prefecture-two-content"]/div[%d]'%i).click()
            time.sleep(0.5)
            self.add_img()
            text1 = self.driver.find_element_by_xpath('//div[@class="main-div"]/div[1]/div/div/div[1]/div[1]/div[1]/div/div').text
            self.assertIn(checklist[i-1],text1)
            self.driver.back()


    def test_logowall(self):
        u'''logo墙'''
        self.setup_get()

        self.wall_step(1,15)

        self.wall_step(2,15)

        self.wall_step(3,7)


    def test_company_contact_us(self):
        u'''公司联系我们'''
        self.setup_get()
        time.sleep(1)
        self.comme.roll('//div[@class="company-prefecture-title"]',self.driver)
        self.driver.find_element_by_xpath('//div[@class="company-prefecture-content-title-div"]/div[2]/button').click()
        #点击联系我们
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[@class="company-read-info-content"]/div[1]/div[3]/button').click()
        #填入信息并提交
        self.comme.contact_us(u'厂商联系测试',u'厂商',u'15656567878',u'测试测试',self.driver,u'test@123.com')
        time.sleep(1)
if __name__ == '__main__':
    unittest.main()