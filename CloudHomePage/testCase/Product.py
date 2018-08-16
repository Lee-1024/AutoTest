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

class Product(unittest.TestCase):

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

    def step(self,ele1,ele2,ele3,check_list):
        """
        :param ele1: 元素在第几行
        :param ele2: 元素是该行的第几个
        :param ele3: 点击该行一个元素后，下面有几个点击项
        :param check_list: 传入检查点，列表或者元组
        :return: 云产品区操作方法，无返回值
        """
        self.driver.find_element_by_xpath('//div[@class="main-div-container-hompage"]/div[4]/div/div/div[%d]/div[1]/div[%d]'%(ele1+1,ele2)).click()
        time.sleep(2)
        for i in range(1,ele3+1):
            self.driver.find_element_by_xpath('//div[@class="main-div-container-hompage"]/div[4]/div/div/div[%d]/div[3]/div/div/div[%d]'%(ele1+1,i)).click()
            time.sleep(1)
            self.add_img()
            if self.comme.isElementExist('//div[@class="main-div"]/div[1]/div/div/div[1]/div[1]/div[1]/div/div',self.driver):
                text1 = self.driver.find_element_by_xpath('//div[@class="main-div"]/div[1]/div/div/div[1]/div[1]/div[1]/div/div').text
                self.assertIn(check_list[i-1],text1)

            elif self.comme.isElementExist('//div[@class="product-item-title"]/span',self.driver):
                text2 = self.driver.find_element_by_xpath('//div[@class="product-item-title"]/span').text
                self.assertIn(check_list[i-1],text2)

            self.driver.back()
            self.driver.find_element_by_xpath('//div[@class="main-div-container-hompage"]/div[4]/div/div/div[%d]/div[1]/div[%d]'%(ele1+1,ele2)).click()
            time.sleep(2)

    def test_Product_1(self):
        u'''不断更新的云产品第一行'''
        self.driver.get(self.comme.url)
        self.driver.maximize_window()
        self.driver.find_element_by_class_name('apsClose').click()
        #IaaS
        checks=(u'阿里',u'腾讯',u'华为',u'金山',u'华云')
        self.step(1,1,5,checks)

        #PaaS
        checks=(u'AWS',u'IM',u'环信')
        self.step(1,2,3,checks)

        #数字营销
        checks=(u'军犬',u'博雅',u'编++')
        self.step(1,3,3,checks)

        #通用办公
        checks=(u'Office365',u'今目标',u'与真云视',u'科天',u'Proces')
        self.step(1,4,5,checks)

        #企业管理
        checks=(u'英盛网',u'法大大',u'用友',u'云势',u'由你飞')
        self.step(1,5,5,checks)

        #安全运维
        checks=(u'服网',u'景安',u'监控',u'绿盟',u'亚洲')
        self.step(1,6,5,checks)

    def test_Product_2(self):
        u'''不断更新的云产品第二行'''
        self.driver.get(self.comme.url)
        self.driver.maximize_window()
        self.driver.find_element_by_class_name('apsClose').click()

        #新技术
        checks=(u'拓尔思')
        self.step(2,1,1,checks)

        #服务
        #self.step(2,2,5)


    def test_product_contact_us(self):
        u'''产品联系我们'''
        self.driver.get(self.comme.url)
        self.driver.maximize_window()
        self.driver.find_element_by_class_name('apsClose').click()
        self.driver.find_element_by_xpath('//div[@class="main-div-container-hompage"]/div[4]/div/div/div[2]/div[1]/div[2]').click()
        self.driver.find_element_by_xpath('//div[@class="main-div-container-hompage"]/div[4]/div/div/div[2]/div[3]/div/div/div[1]').click()
        #点击联系我们
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[@class="library-product-main"]/div[3]/button').click()
        #填入邮件信息并发送
        self.comme.contact_us(1,u'产品详情厂商',u'产品',u'13223233434',u'测试测试',self.driver)
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()

