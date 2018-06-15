# _*_ coding:utf-8 _*_
__author__ = 'Lee'
from selenium import webdriver
import unittest,time
from HTMLTestRunner5 import HTMLTestRunner
now = time.strftime("%Y%m%d%H%S%S",time.localtime())


class test_HTMLTestRunnercn(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "https://wwww.baidu.com"
        self.imgs=[]

    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def test_BaiduSearch(self):
        #u"""百度搜索"""
        driver = self.driver
        driver.get(self.url)
        driver.find_element_by_id("kw").send_keys("selenium")
        self.add_img()
        driver.implicitly_wait(30)
        driver.find_element_by_id("su").click()
        driver.implicitly_wait(30)
        text = driver.find_element_by_xpath('//*[@id="1"]/h3/a/em').text
        self.add_img()
        self.assertEqual(text,'selenium')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()