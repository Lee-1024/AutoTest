#_*_ coding:utf-8 _*_
__author__ = 'Lee'
from selenium import webdriver
import unittest,time
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
        self.comme = CommonMethod()

    def add_img(self):
        #截图添加到测试报告中的方法
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def step(self,ele1,ele2,ele3):

        self.driver.find_element_by_xpath('//div[@class="product-introduction"]/div[%d]/div/div[%d]'%(ele1+1,ele2)).click()
        time.sleep(2)
        for i in range(1,ele3+1):
            window_1 = self.driver.current_window_handle
            self.driver.find_element_by_xpath('//div[@class="product-introduction"]/div[%d]/div[3]/div/div/div[%d]'%(ele1+1,i)).click()
            self.comme.WinMove(window_1,self.driver)

            self.add_img()
            self.driver.close()
            self.driver.switch_to.window(window_1)

    def test_Product_1(self):

        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.driver.find_element_by_class_name('apsClose').click()
        #IaaS
        self.step(1,1,5)

        #PaaS
        self.step(1,2,3)

        #数字营销
        self.step(1,3,3)

        #通用办公
        self.step(1,4,5)

        #企业管理
        self.step(1,5,5)

        #安全运维
        self.step(1,6,5)

    def test_Product_2(self):

        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.driver.find_element_by_class_name('apsClose').click()

        #新技术
        self.step(2,1,1)

        #服务
        self.step(2,2,5)


if __name__ == '__main__':
    unittest.main()

