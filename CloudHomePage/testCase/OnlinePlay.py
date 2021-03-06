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

class OlinePlay(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.binary_location = "C:\\Users\\amallayev\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"
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

    def step(self,check):
        """
        :param check: 检查点列表，传入列表或元组
        :return: 产品直播间中测试步骤方法，无返回值
        """
        self.comme.roll('//div[@class="on-line-play-content"]/div/div[4]/div[2]/div/span',self.driver)
        for i in range(1,len(check)+1):
            window_2 = self.driver.current_window_handle
            self.driver.find_element_by_xpath('//div[@class="on-line-play-content"]/div/div[%d]/div[2]/div/span'%i).click()
            WinMov = CommonMethod()
            WinMov.WinMove(window_2,self.driver)
            self.add_img()
            title=self.driver.title

            self.assertIn(check[i-1],title)
            self.driver.close()
            self.driver.switch_to.window(window_2)
            self.comme.roll('//div[@class="on-line-play-content"]/div/div[4]/div[2]/div/span',self.driver)

    def step_last(self,check):
        """
        :param check: 检查点列表，传入title列表或元组
        :return:直播间点击左移后的直播测试步骤方法，无返回值
        """
        self.comme.roll('//div[@class="on-line-play-content"]/div/div[4]/div[2]/div/span',self.driver)
        time.sleep(1)
        for i in range(1,len(check)+1):
            window_2 = self.driver.current_window_handle

            self.driver.find_element_by_class_name('on-line-play-content-right').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('//div[@class="on-line-play-content"]/div/div[5]/div[2]/div/span').click()
            self.comme.WinMove(window_2,self.driver)

            title=self.driver.title

            self.assertIn(check[i-1],title)
            self.add_img()
            self.driver.close()
            time.sleep(1)
            self.driver.switch_to.window(window_2)

    def test_onlineplay(self):
        u'''产品直播间'''
        self.driver.get(self.comme.url)
        self.driver.maximize_window()
        self.driver.find_element_by_class_name('apsClose').click()
        checklist = [u'集市2',u'集市',u'畅捷通',u'法大大']
        self.step(checklist)

        checklist_last = [u'云势',u'并行',u'绿盟',u'华为',u'腾讯',u'今目标',u'金山']
        self.step_last(checklist_last)

if __name__ == '__main__':
    unittest.main()