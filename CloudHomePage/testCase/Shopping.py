# _*_ coding:utf-8 _*_
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
        self.imgs = []
        self.comme = CommonMethod()

    def add_img(self):
        #截图添加到测试报告中的方法
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def step(self,check):
        """
        :param check: 检查点列表，传入列表或元组
        :return: 一站式购买中产品方法，无返回值
        """
        for i in range(1,len(check)+1):
            window_2 = self.driver.current_window_handle
            self.driver.find_element_by_xpath('//div[@class="shopping-content"]/div/div[%d]/div/img'%i).click()
            WinMov = CommonMethod()
            WinMov.WinMove(window_2,self.driver)
            text1 = self.driver.find_element_by_class_name('BlockName').text
            self.assertIn(check[i-1],text1)
            self.add_img()
            self.driver.close()
            self.driver.switch_to.window(window_2)

    def step_last(self,check):

        self.comme.roll('//div[@class="shopping-content"]/div/div[4]/div/img',self.driver)
        time.sleep(1)
        for i in range(1,len(check)+1):
            window_2 = self.driver.current_window_handle
            self.driver.find_element_by_xpath('//div[@class="shopping-content"]/img').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('//div[@class="shopping-content"]/div/div[%d]/div/img'%(i+4)).click()
            self.comme.WinMove(window_2,self.driver)
            text1 = self.driver.find_element_by_class_name('BlockName').text
            self.assertIn(check[i-1],text1)
            self.add_img()
            self.driver.close()
            self.driver.switch_to.window(window_2)

    def test_shopping(self):

        self.driver.get(self.comme.url)
        self.driver.maximize_window()
        self.driver.find_element_by_class_name('apsClose').click()
        checklist = [u'365',u'WPS',u'金山',u'今目标']
        self.step(checklist)

        checklist_last = [u'绿盟']
        self.step_last(checklist_last)

if __name__ == '__main__':
    unittest.main()