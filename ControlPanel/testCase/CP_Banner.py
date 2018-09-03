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

class Banner(unittest.TestCase):

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


    def test_homepage_banner(self):
        u"""首页banner"""
        self.setup_get()

        self.driver.find_element_by_xpath('//div[@class="side-list-root"]/nav/div[3]').click()

        self.driver.find_element_by_xpath('//div[@class="side-list-root"]/nav/div[4]/div/div/div/div[1]/div/span').click()

        self.driver.find_element_by_xpath('//div[@class="root-main-view"]/div/div[2]/div/button/span[1]').click()

        self.driver.find_element_by_xpath('//div[@class="dialog-main-container"]/div[1]/div[1]/div/div/input').send_keys(u'测试')

        self.driver.find_element_by_xpath('//div[@class="dialog-main-container"]/div[2]/div[1]/div/div/input').send_keys('www.baidu.com')

        self.driver.find_element_by_xpath('//div[@class="dialog-main-container"]/div[2]/div[2]/div/div/input').send_keys(3)

        self.driver.find_element_by_xpath('//div[@class="dialog-main-container"]/div[4]/input').send_keys(u'C:\\AutoTest_tools\\dota2.jpg')

        time.sleep(1)
        self.driver.find_element_by_xpath('//div[@class="dialog-main"]/header/div/button[2]/span[1]').click()

        self.driver.get('https://stg.hnacloudmarket.com/')
        time.sleep(3)
        self.driver.find_element_by_class_name('apsClose').click()
        self.driver.find_element_by_xpath('//div[@class="ant-carousel"]/div/ul/li[1]/button').click()

        self.add_img()

        time.sleep(5)

    def test_blog_banner(self):
        self.setup_get()

        self.driver.find_element_by_xpath('//div[@class="side-list-root"]/nav/div[3]').click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//div[@class="side-list-root"]/nav/div[4]/div/div/div/div[2]/div/span').click()

        self.driver.find_element_by_xpath('//div[@class="root-main-view"]/div/div[2]/div/button/span[1]').click()

        self.driver.find_element_by_xpath('//div[@class="dialog-main-container"]/div[1]/div[1]/div/div/input').send_keys(u'测试')

        self.driver.find_element_by_xpath('//div[@class="dialog-main-container"]/div[2]/div[1]/div/div/input').send_keys('www.baidu.com')

        self.driver.find_element_by_xpath('//div[@class="dialog-main-container"]/div[2]/div[2]/div/div/input').send_keys(1)

        self.driver.find_element_by_xpath('//div[@class="dialog-main-container"]/div[4]/input').send_keys(u'C:\\AutoTest_tools\\dota2.jpg')

        time.sleep(1)
        self.driver.find_element_by_xpath('//div[@class="dialog-main"]/header/div/button[2]/span[1]').click()

        time.sleep(10)


if __name__ == "__main__":
    unittest.main()