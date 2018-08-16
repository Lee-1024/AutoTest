# _*_ coding:utf-8 _*_
__author__ = 'Lee'
import sys
import os
currentUrl = os.path.dirname(__file__)
parentUrl = os.path.abspath(os.path.join(currentUrl, os.pardir))
sys.path.append(parentUrl)
from selenium import webdriver
import unittest
import time
from Common.Common import CommonMethod

class TitleSpan(unittest.TestCase):

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


    def step_test(self,firstsort,secondsort,product):
        """
        :param firstsort:第一级位置
        :param secondsort:第二级位置
        :param product:检查产品列表，传入列表或者元组
        :return: 测试步骤，无返回值
        """
        for h in range(1,len(product)+1):
            self.comme.hover('//div[@class="titleMain"]/ul/li[1]/span',self.driver)
            time.sleep(1)
            self.comme.hover('//div[@class="titleMain"]/div[3]/ul/li[1]/ul/li[%d]'%firstsort,self.driver)
            time.sleep(1)
            self.comme.hover('//div[@class="titleMain"]/div[3]/ul/li[2]/ul/li[%d]'%secondsort,self.driver)
            time.sleep(1)
            self.driver.find_element_by_xpath('//div[@class="titleMain"]/div[3]/ul/li[3]/div/span[%d]'%h).click()
            time.sleep(3)
            text = self.driver.find_element_by_xpath('//div[@class="product-item-title"]/span').text
            self.assertIn(product[h-1],text)
            #self.comme.roll('//div[@class="DraftEditor-root"]/div/div/div/div[3]/div/h1/span/span',self.driver)
            self.add_img()
            self.driver.back()

    def test_cloudservice(self):
        u'''云服务'''
        self.setup_get()
        time.sleep(1)
        check_list = [u'OSS',u'SLB',u'COS']
        self.step_test(1,1,check_list)

    def test_zprocurement(self):
        u"""一站式采购验证"""
        self.driver.get(self.comme.url)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.find_element_by_class_name('apsClose').click()
        window_1 = self.driver.current_window_handle
        self.driver.find_element_by_xpath('//div[@class="titleMain"]/ul/li[2]/span').click()
        comme = CommonMethod()
        comme.WinMove(window_1,self.driver)
        self.add_img()
        text = self.driver.find_element_by_xpath('//*[@id="big-footer"]/div/div/div[3]/a').text
        self.assertIn(u'云集市',text)
        self.driver.close()
        self.driver.switch_to.window(window_1)

    def test_zsupport(self):
        u"""支持"""
        self.driver.get(self.comme.url)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.find_element_by_class_name('apsClose').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//div[@class="titleMain"]/ul/li[5]/span').click()
        self.add_img()
        text = self.driver.find_element_by_xpath('//*[@class="supportList"]/h5/a').text
        self.assertIn(u'营销',text)

        texts = [u'营销',u'推荐',u'付款',u'佣金',u'配置',u'查看',u'链接',u'报告']
        #循环点击内容
        for i in range(0, 8):
            self.driver.find_elements_by_class_name('supportList')[i].click()
            time.sleep(2)
            text =self.driver.find_element_by_xpath('//*[@class="supportTit"]').text
            self.assertIn(texts[i],text)
            self.add_img()
            self.driver.back()

    def test_zpartner(self):
        u"""成为合作伙伴"""
        self.driver.get(self.comme.url)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.find_element_by_class_name('apsClose').click()
        self.comme.hover('//div[@class="titleMain"]/ul/li[4]/span',self.driver)
        time.sleep(1)
        #-----代理商------#
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/ul/li[1]/ul/li/a').click()#点击成为代理商
        text = self.driver.find_element_by_class_name('contact-form-div-title').text
        self.assertIn(u'代理',text)

        self.driver.find_element_by_id('userName').send_keys('TESTER@test.com') #用户名
        self.driver.find_element_by_id("companyName").send_keys('CompanyName')#公司名称
        #公司规模
        self.driver.find_element_by_xpath('//div[@class="contact-form-content"]/form/div[1]/div[3]/div/div/div[2]/div/span/div/div/span').click()
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/ul/li[1]').click()
        #行业
        self.driver.find_element_by_xpath('//div[@class="contact-form-content"]/form/div[1]/div[4]/div/div/div[2]/div/span/div/div/span').click()
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li[1]').click()

        self.driver.find_element_by_id('companyTel').send_keys('13737374646')#公司电话
        self.driver.find_element_by_id('contactName').send_keys('Tester')#联系人姓名
        #联系人职务
        self.driver.find_element_by_xpath('//div[@class="contact-form-content"]/form/div[1]/div[7]/div/div/div[2]/div/span/div/div/span').click()
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul/li[1]').click()

        self.driver.find_element_by_id('contactTel').send_keys("13223234545")#联系人电话
        self.driver.find_element_by_id('partnerNumber').send_keys('123321')#微软合作伙伴编号

        #点击提交
        self.driver.find_element_by_xpath('//div[@class="contact-form-content"]/form/div[2]/div/div/div/div/span/button').click()
        time.sleep(2)
        self.add_img()
        time.sleep(6)
        #-----厂商-----#
        self.comme.hover('//div[@class="titleMain"]/ul/li[4]/span',self.driver)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[2]/ul/li[2]/ul/li/a').click()
        self.driver.find_element_by_id('companyName').send_keys('Company') #公司名称
        self.driver.find_element_by_id('userName').send_keys('Tester') #联系人姓名
        self.driver.find_element_by_id('userPhone').send_keys('13434344545') #联系人电话
        self.driver.find_element_by_id('userEmail').send_keys('Tester@123.com') #电子邮箱

        #厂商相关问题
        self.driver.find_element_by_id('yearTurnover').send_keys('100')#年营业额
        self.driver.find_element_by_xpath('//*[@id="api"]/label[1]/span[1]/input').click()#是否文档化
        self.driver.find_element_by_id('incomeRatio').send_keys('0.33')#年收入比例
        self.driver.find_element_by_id('decemberBudget').send_keys('100')#营销预算
        self.driver.find_element_by_id('twelveBudget').send_keys('100')#销售预算
        self.driver.find_element_by_id('channelDiscounts').send_keys('0.22')#渠道折扣
        self.driver.find_element_by_id('overlayArea').send_keys('10')#几个区域
        self.driver.find_element_by_id('solutionIntegration').send_keys('100')#方案集成
        self.driver.find_element_by_id('marketShare').send_keys(u'测试测试测试')#市场份额
        self.driver.find_element_by_id('targetMarket').send_keys('99')#目标市场
        self.driver.find_element_by_xpath('//*[@id="varChannelStrategy"]/label[1]/span[1]/input').click()#VAR
        self.driver.find_element_by_xpath('//*[@id="mspChannelStrategy"]/label[1]/span[1]/input').click()#MSP
        self.driver.find_element_by_xpath('//*[@id="providerChannelStrategy"]/label[1]/span[1]/input').click()#通讯
        self.driver.find_element_by_xpath('//*[@id="policySupport"]/label[1]/span[1]/input').click()#政策支撑
        self.driver.find_element_by_xpath('//*[@id="soleDuty"]/label[1]/span[1]/input').click()#销售团队
        self.driver.find_element_by_xpath('//*[@id="edxclusivedistribution"]/label[1]/span[1]/input').click()#转售协议
        self.driver.find_element_by_xpath('//*[@id="cooperativePartner"]/label[1]/span[1]/input').click()#合作伙伴
        self.driver.find_element_by_xpath('//*[@id="authorizationCertification"]/label[1]/span[1]/input').click()#销售产品
        self.driver.find_element_by_xpath('//*[@id="monthSubscribe"]/label[1]/span[1]/input').click()#订阅选项

        self.driver.find_element_by_xpath('//div[@class="contact-form-content"]/form/div[6]/div/div/div/div/span/button').click()
        time.sleep(2)
        self.add_img()


if __name__ == '__main__':
    unittest.main()