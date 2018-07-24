#_*_ coding:utf-8 _*_
__author__ = 'Lee'
from selenium import webdriver
import unittest,time
from Common import CommonMethod

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

    def add_img(self):
        #截图添加到测试报告中的方法
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def setup_get(self):
        self.driver.get(self.comme.url)
        self.driver.maximize_window()
        self.driver.find_element_by_class_name('apsClose').click()

    def test_company_1_ex(self):

        self.setup_get()
        window_1 = self.driver.current_window_handle
        self.driver.find_element_by_xpath('//div[@class="company-prefecture"]/div[2]/div/div[1]/div[2]/button').click()
        self.comme.WinMove(window_1,self.driver)
        self.add_img()
        self.driver.close()
        self.driver.switch_to.window(window_1)

    def test_company_1_com(self):

        self.setup_get()
        window_1 = self.driver.current_window_handle

        for i in range(1,4):
            self.driver.find_element_by_xpath('//div[@class="company-prefecture"]/div[2]/div/div[2]/div[%d]'%i).click()
            self.comme.WinMove(window_1,self.driver)
            self.add_img()
            self.driver.close()
            self.driver.switch_to.window(window_1)


        time.sleep(5)