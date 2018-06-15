# _*_ coding:utf-8 _*_
__author__ = 'Lee'
from selenium import webdriver
import unittest
from selenium.webdriver.common.action_chains import ActionChains
import time


class Banner(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        #self.base_url = "http://dev.hnacloudmarket.com/"
        #self.base_url ='http://stg.hnacloudmarket.com/'
        self.base_url = 'http://www.hnacloudmarket.com/'
        self.driver.implicitly_wait(30)
        self.imgs = []

    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def test_banner(self):
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        time.sleep(4)
        self.driver.find_element_by_class_name('apsClose').click()
        elem = self.driver.find_elements_by_class_name('nivo-imageLink')

        for i in range(0,6):
            urls=elem[i].get_attribute('href')
            self.driver.get(urls)
            time.sleep(1)
            self.driver.get(self.base_url)
            time.sleep(4)
            self.driver.find_element_by_class_name('apsClose').click()
            time.sleep(5)
            self.add_img()
            elem = self.driver.find_elements_by_class_name('nivo-imageLink')


if __name__ == '__main__':
    unittest.main()