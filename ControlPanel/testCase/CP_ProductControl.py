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
import unittest,time,random
import urllib
from Common.Common import CommonMethod
from Common.Logger import Log

class ProductControl(unittest.TestCase):

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

    def input_text(self,index,text):
        self.driver.find_element_by_xpath('//div[@class="DraftEditor-editorContainer"]/div/div/div[%d]/div/h1/span/span'%index).click()

        ActionChains(self.driver).send_keys(Keys.RIGHT,Keys.RIGHT).perform()

        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        time.sleep(1)
        ActionChains(self.driver).send_keys(text).perform()

    def test_product(self):
        u'''产品管理'''
        self.setup_get()
        #点击云产品
        self.driver.find_element_by_xpath('//div[@class="side-list-root"]/nav/div[4]').click()
        time.sleep(0.5)
        #点击产品管理
        self.driver.find_element_by_xpath('//div[@class="side-list-root"]/nav/div[5]/div/div/div/div[2]/div/span').click()
        time.sleep(0.5)
        #点击添加
        self.driver.find_element_by_xpath('//div[@class="prod-container"]/div[2]/button/span[1]').click()
        time.sleep(0.5)
        #输入产品名称
        self.driver.find_element_by_xpath('//div[@class="dialog-main"]/div/div[1]/div[2]/input').send_keys(u'测试产品详情')
        time.sleep(0.5)
        #输入产品描述
        self.driver.find_element_by_xpath('//div[@class="dialog-main"]/div/div[2]/div[2]/textarea').send_keys(u'测试产品详情描述')
        time.sleep(0.5)
        #上传产品logo
        self.driver.find_element_by_xpath('//div[@class="dialog-main"]/div/div[3]/div[2]/span/div[1]/span/input').send_keys(
            'C:\\Users\\Bill\\Desktop\\google.jpg')
        time.sleep(0.5)
        #选择所属公司
        self.driver.find_element_by_xpath('//div[@class="dialog-main"]/div/div[4]/div[2]/div/div/span').click()
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li[1]').click()
        time.sleep(0.5)
        #产品信息
        self.input_text(1,u'测试')
        #产品功能
        self.input_text(3,u'还是测试')
        #业务场景
        self.input_text(5,u'又是个测试')
        #技术参数
        self.input_text(7,u'这是个测试')
        #产品优势
        self.input_text(9,u'这还是测试')
        #客户案例
        self.input_text(11,u'接着测试')
        #视频演示
        self.driver.find_element_by_xpath('//div[@class="DraftEditor-editorContainer"]/div/div/div[13]/div/h1/span/span').click()
        ActionChains(self.driver).send_keys(Keys.RIGHT,Keys.RIGHT).perform()
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        self.driver.find_element_by_xpath('//div[@class="RE-toolbar-root"]/span[8]').click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//div[@class="ant-row"]/div/div/label[3]/span[2]').click()
        time.sleep(0.5)
        self.driver.find_element_by_id('url').send_keys('https://vendor-video.oss-cn-beijing.aliyuncs.com/5-erp.mp4')
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//div[@class="RE-modal-root"]/form/div[2]/div/div/span/button').click()
        time.sleep(3.5)
        #常见问题
        self.input_text(16,u'不断的测试')
        window_1 = self.driver.current_window_handle
        self.driver.find_element_by_xpath('//div[@class="dialog-main"]/header/div/button[3]/span[1]').click()
        time.sleep(5)
        self.comme.WinMove(window_1,self.driver)

        text2 = self.driver.find_element_by_xpath('//div[@class="product-item-title"]/span').text

        self.assertIn(u'详情',text2)

        for i in range(2,10):

            self.driver.find_element_by_xpath('//div[@class="ant-anchor"]/div[%d]'%i).click()
            text1 = self.driver.find_element_by_xpath('//div[@class="ant-anchor"]/div[%d]/a'%i).text
            self.log.info(text1)
            self.add_img()

        self.driver.close()

        self.driver.switch_to.window(window_1)


if __name__ == '__main__':
    unittest.main()
