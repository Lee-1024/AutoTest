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

    def wall_step(self,page,counts):
        """
        :param page:验证第几页的logo墙
        :param counts:当前页有几个logo
        :return:logo墙测试方法，无返回值
        """
        for i in range(1,counts+1):
            self.comme.roll('//div[@class="company-prefecture-two-content"]/div[5]',self.driver)
            self.driver.find_element_by_xpath('//div[@class="company-prefecture-three-div-number"]/div[%d]/div'%page).click()
            time.sleep(0.3)
            window_1 = self.driver.current_window_handle
            self.driver.find_element_by_xpath('//div[@class="company-prefecture-three-div-div"]/div[%d]'%i).click()
            self.comme.WinMove(window_1,self.driver)
            self.add_img()
            self.driver.close()
            self.driver.switch_to.window(window_1)

    def test_company_1_ex(self):

        self.setup_get()
        time.sleep(1)
        window_1 = self.driver.current_window_handle

        self.comme.roll('//div[@class="company-prefecture-title"]',self.driver)
        self.driver.find_element_by_xpath('//div[@class="company-prefecture-content-title-div"]/div[2]/button').click()
        self.comme.WinMove(window_1,self.driver)
        self.add_img()
        self.driver.close()
        self.driver.switch_to.window(window_1)

    def test_company_1_com(self):

        self.setup_get()
        window_1 = self.driver.current_window_handle

        for i in range(1,4):
            self.comme.roll('//div[@class="company-prefecture-title"]',self.driver)
            self.driver.find_element_by_xpath('//div[@class="company-prefecture-content-title-div-middle"]/div[%d]'%i).click()
            self.comme.WinMove(window_1,self.driver)
            self.add_img()
            self.driver.close()
            self.driver.switch_to.window(window_1)

    def test_company_2(self):

        self.setup_get()
        window_1 = self.driver.current_window_handle

        for i in range(1,9):
            self.driver.find_element_by_xpath('//div[@class="company-prefecture-two-content"]/div[%d]'%i).click()
            self.comme.WinMove(window_1,self.driver)
            self.add_img()
            self.driver.close()
            self.driver.switch_to.window(window_1)

    def test_logowall(self):
        self.setup_get()

        self.wall_step(1,15)

        self.wall_step(2,14)


if __name__ == '__main__':
    unittest.main()