# _*_ coding:utf-8 _*_
__author__ = 'Lee'
from selenium import webdriver
import unittest
from selenium.webdriver.common.action_chains import ActionChains
import time,datetime

class HomePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.base_url = 'https://stg.hnacloudmarket.com/'
        #self.base_url = 'https://hnacloudmarket.com/'
        self.imgs = []

    def add_img(self):
        #截图添加到测试报告中的方法
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def hover(self,elem):
        #悬停
        elem = self.driver.find_element_by_xpath(elem)
        ActionChains(self.driver).move_to_element(elem).perform()

    def supportLinkButton(self):
        #点击联系我
        self.driver.find_element_by_id('supportLinkButton').click()
        self.driver.find_element_by_xpath('//*[@id="wpcf7-f349-o1"]/form/div[2]/div[7]/div/input').click()
        time.sleep(2)
        text = self.driver.find_element_by_xpath('//*[@id="wpcf7-f349-o1"]/form/div[2]/div[1]/div[2]/span/span').text
        self.assertIn(u'必填',text)
        self.add_img()
        self.driver.find_element_by_xpath('//*[@id="contactForm"]/div/span').click()


    def isElementExist(self):
        #判断购买按钮是否存在
        try:
            self.driver.find_element_by_xpath('//div[@class="container"]/div/div[5]/div[2]/p[2]/a')
            return True
        except:
            return False

    def WinMove(self,win):
        #窗口移动
        windows = self.driver.window_handles#获取所有窗口handle
        for current_window in windows:   #循环遍历当handle不等于当前的handle时移动到该窗口
            if current_window != win:
                self.driver.switch_to.window(current_window)

    def step(self,elem1,checks,check1=None):
        """操作步骤"""
        for i in range(1,len(checks)+1):
            #print len(checks)
            window_1 = self.driver.current_window_handle#获取当前窗口handle
            #print i
            self.driver.find_element_by_xpath\
                ('//div[@class="titleMain"]/ul/li[1]/div/ul/li[%d]/ul/li[%d]/a'%(elem1,i)).click()
            time.sleep(6)

            self.WinMove(window_1)

            #验证跳转的页面
            self.add_img()
            time.sleep(2)
            text = self.driver.find_element_by_xpath('//*[@class="productTitle"]/strong').text
            self.assertIn(checks[i-1],text)

            time.sleep(1)
            self.supportLinkButton()

            #判断是否有购买按钮，如果有则点击
            if self.isElementExist():
                window_2 = self.driver.current_window_handle
                self.driver.find_element_by_xpath('//div[@class="container"]/div/div[5]/div[2]/p[2]/a').click()
                self.WinMove(window_2)
                text1 = self.driver.find_element_by_class_name('BlockName').text
                self.assertIn(check1,text1)
                self.add_img()
                self.driver.close()
                self.driver.switch_to.window(window_2)

            self.driver.close()#关闭新打开的页面
            self.driver.switch_to.window(window_1)#移动到原来页面
            self.hover('//div[@class="titleMain"]/ul/li[1]/span')

    def office_ex(self,elem,che):
        #office特例使用方法
        window_1 = self.driver.current_window_handle
        self.driver.find_element_by_xpath(elem).click()
        time.sleep(3)
        self.WinMove(window_1)

        self.add_img()
        text = self.driver.find_element_by_xpath('//*[@id="container-product"]/div[1]/div[1]/table[1]/tbody/tr/td[1]/span').text
        self.assertIn(che,text)
        self.driver.close()
        self.driver.switch_to.window(window_1)

    def office_com(self,elem1,elem2,che,check1=None):
        #office中通用的方法
        window_1 = self.driver.current_window_handle
        self.driver.find_element_by_xpath(elem1).click()
        time.sleep(1)
        self.WinMove(window_1)
        self.add_img()
        text = self.driver.find_element_by_xpath(elem2).text
        self.assertIn(che,text)
        time_stamp = datetime.datetime.now()

        if self.isElementExist():
            window_2 = self.driver.current_window_handle
            self.driver.find_element_by_xpath('//div[@class="container"]/div/div[5]/div[2]/p[2]/a').click()
            self.WinMove(window_2)
            text1 = self.driver.find_element_by_class_name('BlockName').text
            self.assertIn(check1,text1)
            self.add_img()
            self.driver.close()
            self.driver.switch_to.window(window_2)
        #print "time_stamp       " + time_stamp.strftime('%Y.%m.%d-%H:%M:%S')
        self.supportLinkButton()
        #print "time_stamp       " + time_stamp.strftime('%Y.%m.%d-%H:%M:%S')
        self.driver.close()
        self.driver.switch_to.window(window_1)


    def test_acloudComputing(self):
        u"""云计算类别中的选项验证"""
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.driver.find_element_by_class_name('apsClose').click()
        self.hover('//div[@class="titleMain"]/ul/li[1]/span')
        checks = ('ECS',u'华为',u'金山',u'华云',u'创业',u'CVM')
        self.step(1,checks,check1=u'金山')
    def test_bsuperComputing(self):
        u"""超算与超融合类别中的选项验证"""
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.driver.find_element_by_class_name('apsClose').click()
        self.hover('//div[@class="titleMain"]/ul/li[1]/span')
        checks = (u'并行',u'OITS',u'应用',u'一体机')
        self.step(2,checks)
    def test_cbaseInstallation(self):
        u"""大数据基础设置类别中的选项验证"""
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.driver.find_element_by_class_name('apsClose').click()
        self.hover('//div[@class="titleMain"]/ul/li[1]/span')
        checks = (u'KMR',)
        self.step(3,checks)
    def test_dcloudNetwork(self):
        u"""云网络类别中选项验证"""
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.driver.find_element_by_class_name('apsClose').click()
        self.hover('//div[@class="titleMain"]/ul/li[1]/span')
        checks = (u'SLB',u'IP',u'CDN')
        self.step(4,checks,check1=u'金山')
    def test_ecloudStorage(self):
        u"""云存储类别中的选项验证"""
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.driver.find_element_by_class_name('apsClose').click()
        self.hover('//div[@class="titleMain"]/ul/li[1]/span')
        checks = ('OSS','KS3','COS')
        self.step(5,checks)
    def test_ffinancial(self):
        u"""财务人事类别中的选项验证"""
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.driver.find_element_by_class_name('apsClose').click()
        self.hover('//div[@class="titleMain"]/ul/li[1]/span')
        checks = (u'英盛',u'通',u'简税')
        self.step(6,checks)
    def test_ginternetMiddleware(self):
        u"""互联网中间件类别中的选项验证"""
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.driver.find_element_by_class_name('apsClose').click()
        self.hover('//div[@class="titleMain"]/ul/li[1]/span')
        checks = (u'金融云',u'风险')
        self.step(7,checks)
    def test_hcommunicationProducts(self):
        u"""通信产品类别中选项验证"""
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.driver.find_element_by_class_name('apsClose').click()
        self.hover('//div[@class="titleMain"]/ul/li[1]/span')
        checks = (u'科天',u'环信',u'与真',u'云点播',u'A2A',u'会畅通','400',u'融云')
        self.step(8,checks)
    def test_isecurityService(self):
        u"""安全服务类别中的选项验证"""
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.driver.find_element_by_class_name('apsClose').click()
        self.hover('//div[@class="titleMain"]/ul/li[1]/span')
        checks = (u'安全评估',u'公安备案',u'自助扫描',u'安全监测',u'安全防护',u'堡垒',u'防火墙',u'意识评估',u'身份核验',u'防攻击',
        u'Symantec',u'GlobalSign',u'CFCA',u'GeoTrust',u'TrustAsia',u'景安云信',u'CChelper')
        self.step(9,checks)
    def test_jdataBase(self):
        u"""关系型数据库类别中选项验证"""
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.driver.find_element_by_class_name('apsClose').click()
        self.hover('//div[@class="titleMain"]/ul/li[1]/span')
        checks = (u'RDS',u'KRDS',u'CDB')
        self.step(10,checks)
    def test_khadoop(self):
        u"""大数据与AI类别中的选项验证"""
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.driver.find_element_by_class_name('apsClose').click()
        self.hover('//div[@class="titleMain"]/ul/li[1]/span')
        checks = (u'拓尔思',u'博雅',u'军犬',u'互动云',u'智能',u'彩虹')
        self.step(11,checks)
    def test_lcloudManagement(self):
        u"""迁移与云管理类别中的选项验证"""
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.driver.find_element_by_class_name('apsClose').click()
        self.hover('//div[@class="titleMain"]/ul/li[1]/span')
        checks = (u'华云数据',u'CAN',u'VM',u'云首')
        self.step(12,checks)
    def test_mpaas(self):
        u"""Paas"""
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.driver.find_element_by_class_name('apsClose').click()
        self.hover('//div[@class="titleMain"]/ul/li[1]/span')
        checks = (u'AWS',)
        self.step(13,checks)
    def test_mmonitoringService(self):
        u"""监控服务类别中的选项验证"""
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.driver.find_element_by_class_name('apsClose').click()
        self.hover('//div[@class="titleMain"]/ul/li[1]/span')
        checks = (u'Smonitor',u'监控宝',u'Insight','Browser','Mobile','OneAlert')
        self.step(15,checks)


    def test_office(self):
        u"""通用办公类别中的选项验证"""
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        time.sleep(4)
        self.driver.find_element_by_class_name('apsClose').click()
        self.hover('//div[@class="titleMain"]/ul/li[1]/span')
        #点击Office365
        self.office_ex('//div[@class="titleMain"]/ul/li[1]/div/ul/li[14]/ul/li[1]/a','OFFICE')
        self.hover('//div[@class="titleMain"]/ul/li[1]/span')
        #点击WPS+云办公
        self.office_ex('//div[@class="titleMain"]/ul/li[1]/div/ul/li[14]/ul/li[2]/a','WPS')
        self.hover('//div[@class="titleMain"]/ul/li[1]/span')
        #点击编++
        self.office_com('//div[@class="titleMain"]/ul/li[1]/div/ul/li[14]/ul/li[3]/a','//*[@class="productTitle"]/strong',u'编')
        self.hover('//div[@class="titleMain"]/ul/li[1]/span')
        #点击由你飞
        self.office_com('//div[@class="titleMain"]/ul/li[1]/div/ul/li[14]/ul/li[4]/a','//*[@class="productTitle"]/strong',u'Unify')
        self.hover('//div[@class="titleMain"]/ul/li[1]/span')
        #点击云势软件客户关系管理系统
        self.office_com('//div[@class="titleMain"]/ul/li[1]/div/ul/li[14]/ul/li[5]/a','//*[@class="productTitle"]/strong',u'客户关系')
        self.hover('//div[@class="titleMain"]/ul/li[1]/span')
        #点击云势软件架构指标管理系统
        self.office_com('//div[@class="titleMain"]/ul/li[1]/div/ul/li[14]/ul/li[6]/a','//*[@class="productTitle"]/strong',u'架构指标')
        self.hover('//div[@class="titleMain"]/ul/li[1]/span')
        #点击云势软件奖金返利管理系统
        self.office_com('//div[@class="titleMain"]/ul/li[1]/div/ul/li[14]/ul/li[7]/a','//*[@class="productTitle"]/strong',u'奖金返利')
        self.hover('//div[@class="titleMain"]/ul/li[1]/span')
        #ProcessOn
        self.office_com('//div[@class="titleMain"]/ul/li[1]/div/ul/li[14]/ul/li[8]/a','//*[@class="productTitle"]/strong',u'essOn')
        self.hover('//div[@class="titleMain"]/ul/li[1]/span')
        #点击今目标
        self.office_com('//div[@class="titleMain"]/ul/li[1]/div/ul/li[14]/ul/li[9]/a','//*[@class="productTitle"]/strong',u'目标',check1=u'今目标')
        self.hover('//div[@class="titleMain"]/ul/li[1]/span')
        #点击PGS航旅电子客票平台
        self.office_com('//div[@class="titleMain"]/ul/li[1]/div/ul/li[14]/ul/li[10]/a','//*[@class="productTitle"]/strong',u'PGS')
        self.hover('//div[@class="titleMain"]/ul/li[1]/span')
        #点击服网云桌面解决方案
        self.office_com('//div[@class="titleMain"]/ul/li[1]/div/ul/li[14]/ul/li[11]/a','//*[@class="productTitle"]/strong',u'服网云')
        self.hover('//div[@class="titleMain"]/ul/li[1]/span')
        #点击法大大
        self.office_com('//div[@class="titleMain"]/ul/li[1]/div/ul/li[14]/ul/li[12]/a','//*[@class="productTitle"]/strong',u'电子合同')

    def test_zprocurement(self):
        u"""一站式采购验证"""
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.find_element_by_class_name('apsClose').click()
        window_1 = self.driver.current_window_handle
        self.driver.find_element_by_xpath('//div[@class="titleMain"]/ul/li[2]/span').click()
        self.WinMove(window_1)
        self.add_img()
        text = self.driver.find_element_by_xpath('//*[@id="big-footer"]/div/div/div[3]/a').text
        self.assertIn(u'云集市',text)
        self.driver.close()
        self.driver.switch_to.window(window_1)

    def test_zsupport(self):
        u"""支持"""
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.find_element_by_class_name('apsClose').click()
        time.sleep(3)
        window_1 = self.driver.current_window_handle
        self.driver.find_element_by_xpath('//div[@class="titleMain"]/ul/li[5]/span').click()
        self.WinMove(window_1)
        self.add_img()
        text = self.driver.find_element_by_xpath('//*[@class="supportList"]/h5/a').text
        self.assertIn(u'营销',text)

        texts = [u'营销',u'推荐',u'付款',u'佣金',u'配置',u'查看',u'链接',u'报告']
        #循环点击内容
        for i in range(1, 9):
            pa = '//*[@class="vc_column-inner "]/div/div/div/section/div/div/div[%d]/h5/a'%i
            self.driver.find_element_by_xpath(pa).click()
            time.sleep(2)
            text =self.driver.find_element_by_xpath('//*[@class="vc_column-inner "]/div/div/div/section/div/h4').text
            self.assertIn(texts[i-1],text)
            self.add_img()
            self.driver.back()

    def test_zpartner(self):
        u"""成为合作伙伴"""
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.find_element_by_class_name('apsClose').click()
        self.hover('//div[@class="titleMain"]/ul/li[4]/span')
        time.sleep(1)
        #代理商
        window_1 = self.driver.current_window_handle
        self.driver.find_element_by_xpath('//div[@class="titleMain"]/ul/li[4]/div/ul/li[1]/ul/li/a').click()
        self.WinMove(window_1)
        window_2 = self.driver.current_window_handle
        self.driver.find_element_by_xpath('//div[@class="content-box"]/div[2]/a[1]').click()#点击申请
        self.WinMove(window_2)
        self.driver.find_element_by_xpath('//div[@class="applyLogin"]/input').click()#点击立即申请
        self.add_img()
        text = self.driver.find_element_by_xpath('//form[@class="wpcf7-form invalid"]/div[2]/div[1]/div[2]/span/span').text
        self.assertIn(u'必填',text)
        self.driver.close()
        self.driver.switch_to.window(window_2)#移动到第二窗口
        self.driver.close()
        self.driver.switch_to.window(window_1)#移动到第一窗口
        #加盟
        self.hover('//div[@class="titleMain"]/ul/li[4]/span')
        time.sleep(1)
        window_1 = self.driver.current_window_handle
        self.driver.find_element_by_xpath('//div[@class="titleMain"]/ul/li[4]/div/ul/li[2]/ul/li/a').click()
        self.WinMove(window_1)
        window_2 = self.driver.current_window_handle
        self.driver.find_element_by_xpath('//div[@class="content-box"]/div[2]/a[1]').click()#点击联系我们
        self.WinMove(window_2)
        self.driver.find_element_by_xpath('//div[@class="applyLogin"]/input').click()#点击立即申请
        self.add_img()
        text = self.driver.find_element_by_xpath('//form[@class="wpcf7-form invalid"]/div[2]/div[1]/div[2]/span/span').text
        self.assertIn(u'必填',text)
        self.driver.close()
        self.driver.switch_to.window(window_2)#移动到第二窗口
        self.driver.close()
        self.driver.switch_to.window(window_1)#移动到第一窗口


if __name__ == '__main__':
    unittest.main()