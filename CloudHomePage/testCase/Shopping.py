# _*_ coding:utf-8 _*_
__author__ = 'Lee'
from selenium import webdriver
import unittest
from Common import CommonMethod

class Shopping(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.base_url = 'https://stg.hnacloudmarket.com/'
        #self.base_url = 'https://www.hnacloudmarket.com/'
        self.imgs = []

    def add_img(self):
        #截图添加到测试报告中的方法
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def step(self,check):
        for i in range(1,len(check)+1):
            window_2 = self.driver.current_window_handle
            self.driver.find_element_by_xpath('//div[@class="shopping"]/div[2]/div[%d]/div/img'%i).click()
            WinMov = CommonMethod()
            WinMov.WinMove(window_2,self.driver)
            text1 = self.driver.find_element_by_class_name('BlockName').text
            self.assertIn(check[i-1],text1)
            self.add_img()
            self.driver.close()
            self.driver.switch_to.window(window_2)


    def test_shopping(self):

        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.driver.find_element_by_class_name('apsClose').click()
        checklist = [u'365',u'WPS',u'金山',u'今目标']
        self.step(checklist)

if __name__ == '__main__':
    unittest.main()