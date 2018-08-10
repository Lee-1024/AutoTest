#_*_ coding:utf-8 _*_
__author__ = 'Lee'
from selenium import webdriver
import unittest,time,random
from Common import CommonMethod

class OtherTest(unittest.TestCase):

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

    def test_partner_homepage(self):
        self.setup_get()
        self.comme.roll('//div[@class="main-div-container-hompage"]/div[8]/div/div/div[1]',self.driver)
        #厂商
        self.driver.find_element_by_xpath('//div[@class="main-div-container-hompage"]/div[8]/div/div/div[2]/div[4]/button').click()
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
        time.sleep(6)

        #分销商
        self.comme.roll('//div[@class="main-div-container-hompage"]/div[8]/div/div/div[1]',self.driver)
        #--点击分销商
        self.driver.find_element_by_xpath('//div[@class="main-div-container-hompage"]/div[8]/div/div/div[2]/div[1]/div[3]').click()
        #--点击申请
        self.driver.find_element_by_xpath('//div[@class="main-div-container-hompage"]/div[8]/div/div/div[2]/div[4]/button').click()
        #--填写信息
        self.driver.find_element_by_id('userName').send_keys('TESTER@test.com') #用户名
        self.driver.find_element_by_id("companyName").send_keys('CompanyName')#公司名称
        #公司规模
        self.driver.find_element_by_xpath('//div[@class="contact-form-content"]/form/div[1]/div[3]/div/div/div[2]/div/span/div/div/span').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/ul/li[1]').click()
        #行业
        self.driver.find_element_by_xpath('//div[@class="contact-form-content"]/form/div[1]/div[4]/div/div/div[2]/div/span/div/div/span').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li[1]').click()

        self.driver.find_element_by_id('companyTel').send_keys('13737374646')#公司电话
        self.driver.find_element_by_id('contactName').send_keys('Tester')#联系人姓名
        #联系人职务
        self.driver.find_element_by_xpath('//div[@class="contact-form-content"]/form/div[1]/div[7]/div/div/div[2]/div/span/div/div/span').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/ul/li[1]').click()

        self.driver.find_element_by_id('contactTel').send_keys("13223234545")#联系人电话
        self.driver.find_element_by_id('partnerNumber').send_keys('123321')#微软合作伙伴编号

        #点击提交
        self.driver.find_element_by_xpath('//div[@class="contact-form-content"]/form/div[2]/div/div/div/div/span/button').click()
        time.sleep(2)
        self.add_img()

    def test_product_and_server(self):
        u"""产品与服务"""
        self.setup_get()
        self.comme.roll('//div[@class="bottom-info-items-div"]/div[2]/div/div[1]',self.driver)
        time.sleep(1)
        checklist = [u'365',u'WPS',u'目标',u'金山']
        for i in range(1,len(checklist)+1):
            window_2 = self.driver.current_window_handle
            self.driver.find_element_by_xpath('//div[@class="bottom-info-items-div"]/div[2]/div/div[%d]/a'%(i+1)).click()
            time.sleep(2)
            self.comme.WinMove(window_2,self.driver)
            text1 = self.driver.find_element_by_class_name('BlockName').text
            self.assertIn(checklist[i-1],text1)
            self.add_img()
            self.driver.close()
            self.driver.switch_to.window(window_2)

    def test_about(self):
        u"""关于我们"""
        self.setup_get()
        self.comme.roll('//div[@class="bottom-info-items-div"]/div[3]/div/div[1]',self.driver)
        time.sleep(1)
        checklist = [u'海航',u'协议',u'营销']
        for i in range(1,len(checklist)+1):
            self.driver.find_element_by_xpath('//div[@class="bottom-info-items-div"]/div[3]/div/div[%d]/a'%(i+1)).click()
            time.sleep(2)
            if self.comme.isElementExist('//div[@class="usInfo"]/p',self.driver):
                text = self.driver.find_element_by_xpath('//div[@class="usInfo"]/p').text
                self.assertIn(checklist[i-1],text)
                self.comme.mylog(u'进入公司介绍判断')
            elif self.comme.isElementExist('//*[@id="userAgreement"]/div[1]/h2',self.driver):
                text = self.driver.find_element_by_xpath('//*[@id="userAgreement"]/div[1]/h2').text
                self.assertIn(checklist[i-1],text)
                self.comme.mylog(u'进入协议判断')
            elif self.comme.isElementExist('//div[@class="main-div-container"]/div[2]/div/div/div[1]/h5/a',self.driver):
                text = self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div[2]/div/div/div[1]/h5/a').text
                self.assertIn(checklist[i-1],text)
                self.comme.mylog(u"进入支持该判断")
            self.add_img()
            self.driver.back()

    def test_down_blog(self):
        u"""页脚博客与进入博客中的各个刷选标签"""
        self.setup_get()
        self.comme.roll('//div[@class="bottom-info-items-div"]/div[4]/div/div[1]',self.driver)
        time.sleep(1)
        #点击进入博客
        self.driver.find_element_by_xpath('//div[@class="bottom-info-items-div"]/div[4]/div/div[2]/a').click()
        #点击展开标识
        self.driver.find_element_by_xpath('//div[@class="ant-anchor"]/div[2]/a').click()
        #点击标签
        self.driver.find_element_by_xpath('//div[@class="ant-anchor"]/div[2]/div[2]/div[%d]'%(random.randint(1,11))).click()
        time.sleep(2)
        #点击关键词
        self.driver.find_element_by_xpath('//div[@class="main-div-panel-right "]/div[2]/div[2]/div/div[%d]'%(random.randint(1,30))).click()
        time.sleep(2)
        #点击行业
        self.driver.find_element_by_xpath('//div[@class="main-div-panel-right "]/div[3]/div[2]/div/div[%d]'%(random.randint(1,25))).click()
        time.sleep(3)
        self.add_img()
        #点击top博主
        self.driver.find_element_by_xpath('//div[@class="main-div-panel-right "]/div[4]/div[2]/div[%d]/div[1]/div/div[2]/a'%(random.randint(2,4))).click()
        self.comme.roll('//div[@class="main-div-panel-left "]/div[1]/div/div',self.driver)
        time.sleep(2)
        self.add_img()

if __name__ == '__main__':
    unittest.main()