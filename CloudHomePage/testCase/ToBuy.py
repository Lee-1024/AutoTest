#_*_ coding:utf-8 _*_
__author__ = 'Lee'
import sys
import os
currentUrl = os.path.dirname(__file__)
parentUrl = os.path.abspath(os.path.join(currentUrl, os.pardir))
sys.path.append(parentUrl)
from selenium import webdriver
import unittest
import time
from Common.Common import CommonMethod

class ToBuy(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.binary_location = "C:\\Users\\amallayev\\AppData\\Local\\Google\Chrome\\Application\\chrome.exe"
        chrome_driver_binary = "C:\\Python27\\chromedriver.exe"
        cls.driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.imgs = []
        self.comme = CommonMethod()

    def add_img(self):
        #截图添加到测试报告中的方法
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def setup_get(self):
        self.driver.get(self.comme.url)
        self.driver.maximize_window()
        self.driver.find_element_by_class_name('apsClose').click()

    def test_kingsoftwps(self):
        u'''金山WPS与金山服务器'''
        self.setup_get()
        self.comme.roll('//div[@class="company-prefecture-title"]',self.driver)
        time.sleep(1)
        #
        self.driver.find_element_by_xpath('//div[@class="company-prefecture-content-title-div"]/div[2]/button').click()
        #点击查看详情
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[@class="product-list-div"]/div[1]/div[3]/button').click()
        #点击立即购买
        window_1 = self.driver.current_window_handle
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[@class="library-product"]/div/div[3]/button').click()
        self.comme.WinMove(window_1,self.driver)
        text1 = self.driver.find_element_by_class_name('BlockName').text
        self.assertIn(u'WPS',text1)
        self.driver.close()
        self.driver.switch_to.window(window_1)
        time.sleep(1)
        self.driver.back()
        #点击查看详情
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[@class="product-list-div"]/div[2]/div[3]/button').click()
        #点击立即购买
        window_1 = self.driver.current_window_handle
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[@class="library-product"]/div/div[3]/button').click()
        self.comme.WinMove(window_1,self.driver)
        text1 = self.driver.find_element_by_class_name('BlockName').text
        self.assertIn(u'金山',text1)
        self.driver.close()
        self.driver.switch_to.window(window_1)


    def test_office365(self):
        u'''OFFICE365'''
        self.setup_get()
        self.comme.roll('//div[@class="company-prefecture-title"]',self.driver)
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[@class="company-prefecture-two-content"]/div[1]').click()
        #点击查看详情
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[@class="product-list-div"]/div[1]/div[3]/button').click()
        #点击立即购买
        window_1 = self.driver.current_window_handle
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[@class="library-product"]/div/div[3]/button').click()
        self.comme.WinMove(window_1,self.driver)
        text1 = self.driver.find_element_by_class_name('BlockName').text
        self.assertIn(u'365',text1)
        self.driver.close()
        self.driver.switch_to.window(window_1)

    def test_jgoal(self):
        u'''今目标'''
        self.setup_get()
        self.comme.roll('//div[@class="company-prefecture-title"]',self.driver)
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[@class="company-prefecture-two-content"]/div[2]').click()
        #点击查看详情
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[@class="product-list-div"]/div[1]/div[3]/button').click()
        #点击立即购买
        window_1 = self.driver.current_window_handle
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[@class="library-product"]/div/div[3]/button').click()
        self.comme.WinMove(window_1,self.driver)
        text1 = self.driver.find_element_by_class_name('BlockName').text
        self.assertIn(u'今目标',text1)
        self.driver.close()
        self.driver.switch_to.window(window_1)


    def test_NSFOCUS_Cloud(self):
        u'''今目标'''
        self.setup_get()
        self.comme.roll('//div[@class="company-prefecture-title"]',self.driver)
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[@class="company-prefecture-two-content"]/div[6]').click()
        #点击查看详情
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[@class="product-list-div"]/div[1]/div[3]/button').click()
        #点击立即购买
        window_1 = self.driver.current_window_handle
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[@class="library-product"]/div/div[3]/button').click()
        self.comme.WinMove(window_1,self.driver)
        text1 = self.driver.find_element_by_class_name('BlockName').text
        self.assertIn(u'绿盟',text1)
        self.driver.close()
        self.driver.switch_to.window(window_1)


if __name__ == '__main__':
    unittest.main()