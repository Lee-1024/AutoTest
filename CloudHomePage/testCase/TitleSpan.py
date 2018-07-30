# _*_ coding:utf-8 _*_
__author__ = 'Lee'
from selenium import webdriver
import unittest
import time
from Common import CommonMethod

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

    def supportLinkButton(self):
        #点击联系我
        self.driver.find_element_by_id('supportLinkButton').click()
        self.driver.find_element_by_xpath('//*[@id="wpcf7-f349-o1"]/form/div[2]/div[7]/div/input').click()
        time.sleep(2)
        text = self.driver.find_element_by_xpath('//*[@id="wpcf7-f349-o1"]/form/div[2]/div[1]/div[2]/span/span').text
        self.assertIn(u'必填',text)
        self.add_img()
        self.driver.find_element_by_xpath('//*[@id="contactForm"]/div/span').click()

    def step(self,elem1,checks,check1=None):
        """
        :param elem1: 大类别的位置
        :param checks: 点击后检查点列表，传入列表或元组
        :param check1: 点击购买后的检查点，如果没有购买按钮则无需传入
        :return: 操作步骤方法 无返回值
        """
        for i in range(1,len(checks)+1):
            #print len(checks)
            window_1 = self.driver.current_window_handle#获取当前窗口handle
            #print i
            self.driver.find_element_by_xpath\
                ('//div[@class="titleMain"]/ul/li[1]/div/ul/li[%d]/ul/li[%d]/a'%(elem1,i)).click()
            time.sleep(6)
            comme = CommonMethod()
            comme.WinMove(window_1,self.driver)

            #验证跳转的页面
            self.add_img()
            time.sleep(2)
            text = self.driver.find_element_by_xpath('//*[@class="productTitle"]/strong').text
            self.assertIn(checks[i-1],text)

            time.sleep(1)
            self.supportLinkButton()

            #判断是否有购买按钮，如果有则点击
            if  comme.isElementExist('//div[@class="container"]/div/div[5]/div[2]/p[2]/a',self.driver):
                window_2 = self.driver.current_window_handle
                self.driver.find_element_by_xpath('//div[@class="container"]/div/div[5]/div[2]/p[2]/a').click()
                comme.WinMove(window_2,self.driver)
                text1 = self.driver.find_element_by_class_name('BlockName').text
                self.assertIn(check1,text1)
                self.add_img()
                self.driver.close()
                self.driver.switch_to.window(window_2)

            #判断是否有购买按钮，如果有则点击
            if  comme.isElementExist('//div[@class="container"]/div/div[5]/div[1]/p[2]/a',self.driver):
                window_2 = self.driver.current_window_handle
                self.driver.find_element_by_xpath('//div[@class="container"]/div/div[5]/div[1]/p[2]/a').click()
                comme.WinMove(window_2,self.driver)
                text1 = self.driver.find_element_by_class_name('BlockName').text
                self.assertIn(check1,text1)
                self.add_img()
                self.driver.close()
                self.driver.switch_to.window(window_2)



            self.driver.close()#关闭新打开的页面
            self.driver.switch_to.window(window_1)#移动到原来页面
            comme.hover('//div[@class="titleMain"]/ul/li[1]/span',self.driver)

    def office_ex(self,elem,che):
        """
        :param elem:下拉列表中元素位置XPATH
        :param che:点击后检查点
        :return:通用办公特殊项方法 无返回值
        """
        window_1 = self.driver.current_window_handle
        self.driver.find_element_by_xpath(elem).click()
        time.sleep(3)
        comme = CommonMethod()
        comme.WinMove(window_1,self.driver)
        self.add_img()
        text = self.driver.find_element_by_xpath('//*[@id="container-product"]/div[1]/div[1]/table[1]/tbody/tr/td[1]/span').text
        self.assertIn(che,text)
        self.driver.close()
        self.driver.switch_to.window(window_1)

    def office_com(self,elem1,elem2,che,check1=None):
        """
        :param elem1: 下拉列表中元素位置XPATH
        :param elem2: 点击后检查点位置XPATH
        :param che: 点击后检查点
        :param check1: 点击购买后检查点
        :return: 通用办公通用方法 无返回值
        """
        window_1 = self.driver.current_window_handle
        self.driver.find_element_by_xpath(elem1).click()
        time.sleep(1)
        comme = CommonMethod()
        comme.WinMove(window_1,self.driver)
        self.add_img()
        text = self.driver.find_element_by_xpath(elem2).text
        self.assertIn(che,text)
        #time_stamp = datetime.datetime.now()

        self.supportLinkButton()

        if  comme.isElementExist('//div[@class="container"]/div/div[5]/div[2]/p[2]/a',self.driver):
            window_2 = self.driver.current_window_handle
            self.driver.find_element_by_xpath('//div[@class="container"]/div/div[5]/div[2]/p[2]/a').click()
            comme.WinMove(window_2,self.driver)
            text1 = self.driver.find_element_by_class_name('BlockName').text
            self.assertIn(check1,text1)
            self.add_img()
            self.driver.close()
            self.driver.switch_to.window(window_2)

        self.driver.close()
        self.driver.switch_to.window(window_1)


    def test_acloudComputing(self):
        u"""云计算类别中的选项验证"""
        self.setup_get()
        self.comme.hover('//div[@class="titleMain"]/ul/li[1]/span',self.driver)
        checks = ('ECS',u'华为',u'金山',u'华云',u'创业',u'CVM')
        self.step(1,checks,check1=u'金山')
    def test_bsuperComputing(self):
        u"""超算与超融合类别中的选项验证"""
        self.setup_get()
        self.comme.hover('//div[@class="titleMain"]/ul/li[1]/span',self.driver)
        checks = (u'并行',u'OITS',u'应用',u'一体机')
        self.step(2,checks)
    def test_cbaseInstallation(self):
        u"""大数据基础设置类别中的选项验证"""
        self.setup_get()
        self.comme.hover('//div[@class="titleMain"]/ul/li[1]/span',self.driver)
        checks = (u'KMR',)
        self.step(3,checks)
    def test_dcloudNetwork(self):
        u"""云网络类别中选项验证"""
        self.setup_get()
        self.comme.hover('//div[@class="titleMain"]/ul/li[1]/span',self.driver)
        checks = (u'SLB',u'IP',u'CDN')
        self.step(4,checks,check1=u'金山')
    def test_ecloudStorage(self):
        u"""云存储类别中的选项验证"""
        self.setup_get()
        self.comme.hover('//div[@class="titleMain"]/ul/li[1]/span',self.driver)
        checks = ('OSS','KS3','COS')
        self.step(5,checks)
    def test_ffinancial(self):
        u"""财务人事类别中的选项验证"""
        self.setup_get()
        self.comme.hover('//div[@class="titleMain"]/ul/li[1]/span',self.driver)
        checks = (u'英盛',u'通',u'简税')
        self.step(6,checks)
    def test_ginternetMiddleware(self):
        u"""互联网中间件类别中的选项验证"""
        self.setup_get()
        self.comme.hover('//div[@class="titleMain"]/ul/li[1]/span',self.driver)
        checks = (u'金融云',u'风险')
        self.step(7,checks)
    def test_hcommunicationProducts(self):
        u"""通信产品类别中选项验证"""
        self.setup_get()
        self.comme.hover('//div[@class="titleMain"]/ul/li[1]/span',self.driver)
        checks = (u'科天',u'环信',u'与真',u'云点播',u'A2A',u'会畅通','400',u'融云')
        self.step(8,checks)
    def test_isecurityService(self):
        u"""安全服务类别中的选项验证"""
        self.setup_get()
        self.comme.hover('//div[@class="titleMain"]/ul/li[1]/span',self.driver)
        checks = (u'安全评估',u'公安备案',u'自助扫描',u'安全监测',u'安全防护',u'堡垒',u'防火墙',u'意识评估',u'身份核验',u'防攻击',
        u'Symantec',u'GlobalSign',u'CFCA',u'GeoTrust',u'TrustAsia',u'景安云信',u'CChelper')
        self.step(9,checks,check1=u'绿盟')
    def test_jdataBase(self):
        u"""关系型数据库类别中选项验证"""
        self.setup_get()
        self.comme.hover('//div[@class="titleMain"]/ul/li[1]/span',self.driver)
        checks = (u'RDS',u'KRDS',u'CDB')
        self.step(10,checks)
    def test_khadoop(self):
        u"""大数据与AI类别中的选项验证"""
        self.setup_get()
        self.comme.hover('//div[@class="titleMain"]/ul/li[1]/span',self.driver)
        checks = (u'拓尔思',u'博雅',u'军犬',u'互动云',u'智能',u'彩虹')
        self.step(11,checks)
    def test_lcloudManagement(self):
        u"""迁移与云管理类别中的选项验证"""
        self.setup_get()
        self.comme.hover('//div[@class="titleMain"]/ul/li[1]/span',self.driver)
        checks = (u'华云数据',u'CAN',u'VM',u'云首')
        self.step(12,checks)
    def test_mpaas(self):
        u"""Paas"""
        self.setup_get()
        self.comme.hover('//div[@class="titleMain"]/ul/li[1]/span',self.driver)
        checks = (u'AWS',)
        self.step(13,checks)
    def test_management(self):
        u"""企业管理"""
        self.setup_get()
        self.comme.hover('//div[@class="titleMain"]/ul/li[1]/span',self.driver)
        checks = (u'纷享',)
        self.step(14,checks)
    def test_mmonitoringService(self):
        u"""监控服务类别中的选项验证"""
        self.setup_get()
        self.comme.hover('//div[@class="titleMain"]/ul/li[1]/span',self.driver)
        checks = (u'Smonitor',u'监控宝',u'Insight','Browser','Mobile','OneAlert')
        self.step(16,checks)


    def test_office(self):
        u"""通用办公类别中的选项验证"""
        self.driver.get(self.comme.url)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        time.sleep(4)
        self.driver.find_element_by_class_name('apsClose').click()
        self.comme.hover('//div[@class="titleMain"]/ul/li[1]/span',self.driver)
        #点击Office365
        self.office_ex('//div[@class="titleMain"]/ul/li[1]/div/ul/li[15]/ul/li[1]/a','OFFICE')
        self.comme.hover('//div[@class="titleMain"]/ul/li[1]/span',self.driver)
        #点击WPS+云办公
        self.office_ex('//div[@class="titleMain"]/ul/li[1]/div/ul/li[15]/ul/li[2]/a','WPS')
        self.comme.hover('//div[@class="titleMain"]/ul/li[1]/span',self.driver)
        #点击编++
        self.office_com('//div[@class="titleMain"]/ul/li[1]/div/ul/li[15]/ul/li[3]/a','//*[@class="productTitle"]/strong',u'编')
        self.comme.hover('//div[@class="titleMain"]/ul/li[1]/span',self.driver)
        #点击由你飞
        self.office_com('//div[@class="titleMain"]/ul/li[1]/div/ul/li[15]/ul/li[4]/a','//*[@class="productTitle"]/strong',u'Unify')
        self.comme.hover('//div[@class="titleMain"]/ul/li[1]/span',self.driver)
        #点击云势软件客户关系管理系统
        self.office_com('//div[@class="titleMain"]/ul/li[1]/div/ul/li[15]/ul/li[5]/a','//*[@class="productTitle"]/strong',u'客户关系')
        self.comme.hover('//div[@class="titleMain"]/ul/li[1]/span',self.driver)
        #点击云势软件架构指标管理系统
        self.office_com('//div[@class="titleMain"]/ul/li[1]/div/ul/li[15]/ul/li[6]/a','//*[@class="productTitle"]/strong',u'架构指标')
        self.comme.hover('//div[@class="titleMain"]/ul/li[1]/span',self.driver)
        #点击云势软件奖金返利管理系统
        self.office_com('//div[@class="titleMain"]/ul/li[1]/div/ul/li[15]/ul/li[7]/a','//*[@class="productTitle"]/strong',u'奖金返利')
        self.comme.hover('//div[@class="titleMain"]/ul/li[1]/span',self.driver)
        #ProcessOn
        self.office_com('//div[@class="titleMain"]/ul/li[1]/div/ul/li[15]/ul/li[8]/a','//*[@class="productTitle"]/strong',u'essOn')
        self.comme.hover('//div[@class="titleMain"]/ul/li[1]/span',self.driver)
        #点击今目标
        self.office_com('//div[@class="titleMain"]/ul/li[1]/div/ul/li[15]/ul/li[9]/a','//*[@class="productTitle"]/strong',u'目标',check1=u'今目标')
        self.comme.hover('//div[@class="titleMain"]/ul/li[1]/span',self.driver)
        #点击PGS航旅电子客票平台
        self.office_com('//div[@class="titleMain"]/ul/li[1]/div/ul/li[15]/ul/li[10]/a','//*[@class="productTitle"]/strong',u'PGS')
        self.comme.hover('//div[@class="titleMain"]/ul/li[1]/span',self.driver)
        #点击服网云桌面解决方案
        self.office_com('//div[@class="titleMain"]/ul/li[1]/div/ul/li[15]/ul/li[11]/a','//*[@class="productTitle"]/strong',u'服网云')
        self.comme.hover('//div[@class="titleMain"]/ul/li[1]/span',self.driver)
        #点击法大大
        self.office_com('//div[@class="titleMain"]/ul/li[1]/div/ul/li[15]/ul/li[12]/a','//*[@class="productTitle"]/strong',u'电子合同')

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
        self.driver.find_element_by_xpath('//div[@class="titleSpan"]/div[2]/ul/li[1]/ul/li/a').click()#点击成为代理商
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
        self.driver.find_element_by_xpath('//div[@class="titleSpan"]/div[2]/ul/li[2]/ul/li/a').click()
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