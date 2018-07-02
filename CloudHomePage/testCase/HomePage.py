# _*_ coding:utf-8 _*_
__author__ = 'Lee'
from selenium import webdriver
import unittest
from selenium.webdriver.common.action_chains import ActionChains
import time,datetime

class HomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = 'https://community.stg.hnacloudmarket.com/'
        self.imgs = []

    def add_img(self):
        #截图添加到测试报告中的方法
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def hover(self):
        #悬停
        elem = self.driver.find_element_by_xpath('//div[@class="titleMain"]/ul/li[1]/span')
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

    def step(self,elem1,checks,check1=None):
        """操作步骤"""
        for i in range(1,len(checks)+1):
            #print len(checks)
            window_1 = self.driver.current_window_handle#获取当前窗口handle
            #print i
            self.driver.find_element_by_xpath\
                ('//div[@class="titleMain"]/ul/li[1]/div/ul/li[%d]/ul/li[%d]/a'%(elem1,i)).click()
            time.sleep(6)
            windows = self.driver.window_handles#获取所有窗口handle
            for current_window in windows:   #循环遍历当handle不等于当前的handle时移动到该窗口
                if current_window != window_1:
                    self.driver.switch_to.window(current_window)
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
                windows = self.driver.window_handles#获取所有窗口handle
                for current_window in windows:   #循环遍历当handle不等于当前的handle时移动到该窗口
                    if current_window != window_2:
                        self.driver.switch_to.window(current_window)
                text1 = self.driver.find_element_by_xpath('//*[@id="listcat_102"]/table[1]/tbody/tr/td[1]/span').text
                self.assertIn(check1,text1)
                self.add_img()
                self.driver.close()
                self.driver.switch_to.window(window_2)

            self.driver.close()#关闭新打开的页面
            self.driver.switch_to.window(window_1)#移动到原来页面
            self.hover()

    def office_ex(self,elem,che):
        #office特例使用方法
        window_1 = self.driver.current_window_handle
        self.driver.find_element_by_xpath(elem).click()
        time.sleep(3)
        windows = self.driver.window_handles#获取所有窗口handle
        for current_window in windows:   #循环遍历当handle不等于当前的handle时移动到该窗口
            if current_window != window_1:
                self.driver.switch_to.window(current_window)

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
        windows = self.driver.window_handles#获取所有窗口handle
        for current_window in windows:   #循环遍历当handle不等于当前的handle时移动到该窗口
            if current_window != window_1:
                self.driver.switch_to.window(current_window)
        self.add_img()
        text = self.driver.find_element_by_xpath(elem2).text
        self.assertIn(che,text)
        time_stamp = datetime.datetime.now()

        if self.isElementExist():
            window_2 = self.driver.current_window_handle
            self.driver.find_element_by_xpath('//div[@class="container"]/div/div[5]/div[2]/p[2]/a').click()
            windows = self.driver.window_handles#获取所有窗口handle
            for current_window in windows:   #循环遍历当handle不等于当前的handle时移动到该窗口
                if current_window != window_2:
                    self.driver.switch_to.window(current_window)
            text1 = self.driver.find_element_by_xpath('//*[@id="listcat_103"]/table[1]/tbody/tr/td[1]/span').text
            self.assertIn(check1,text1)
            self.add_img()
            self.driver.close()
            self.driver.switch_to.window(window_2)
        print "time_stamp       " + time_stamp.strftime('%Y.%m.%d-%H:%M:%S')
        self.supportLinkButton()
        print "time_stamp       " + time_stamp.strftime('%Y.%m.%d-%H:%M:%S')
        self.driver.close()
        self.driver.switch_to.window(window_1)

    def cloudService(self):
        u"""云服务"""
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        self.hover()

        #云计算
        checks = ('ECS',u'华为',u'金山',u'华云',u'创业',u'CVM')
        self.step(1,checks,check1=u'金山')
        #超算与超融合
        checks = (u'并行',u'OITS',u'应用',u'一体机')
        self.step(2,checks)
        #大数据基础设施
        checks = (u'KMR',)
        self.step(3,checks)
        #云网络
        checks = (u'SLB',u'IP',u'CDN')
        self.step(4,checks,check1=u'金山')
        #云存储
        checks = ('OSS','KS3','COS')
        self.step(5,checks)
        # #财务人事
        # checks = (u'英盛',u'通')
        # self.step(6,checks)
        #互联网中间件
        checks = (u'金融云',u'风险')
        self.step(7,checks)
        #通信产品
        checks = (u'科天',u'环信',u'与真')
        self.step(8,checks)
        #安全服务
        checks = (u'安全评估',u'公安备案',u'自助扫描',u'安全监测',u'安全防护',u'堡垒',u'防火墙',u'意识评估',u'身份核验',u'防攻击',
        u'Symantec',u'GlobalSign',u'CFCA',u'GeoTrust',u'TrustAsia',u'景安云信')
        self.step(9,checks)
        #关系型数据库
        checks = (u'RDS',u'KRDS',u'CDB')
        self.step(10,checks)
        #大数据与AI
        checks = (u'拓尔思',u'博雅',u'军犬',u'互动云',u'智能')
        self.step(11,checks)
        #迁移与云管理
        checks = (u'华云数据',u'CAN',u'VM',u'云首')
        self.step(12,checks)

        #监控服务
        checks = (u'Smonitor',u'监控宝')
        self.step(14,checks)


    def test_office(self):
        u"""通用办公类别中的选项验证"""
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        time.sleep(4)
        self.hover()
        #点击Office365
        self.office_ex('//div[@class="titleMain"]/ul/li[1]/div/ul/li[13]/ul/li[1]/a','OFFICE')
        self.hover()
        #点击WPS+云办公
        self.office_ex('//div[@class="titleMain"]/ul/li[1]/div/ul/li[13]/ul/li[2]/a','WPS')
        self.hover()
        #点击编++
        self.office_com('//div[@class="titleMain"]/ul/li[1]/div/ul/li[13]/ul/li[3]/a','//*[@class="productTitle"]/strong',u'编')
        self.hover()
        #点击由你飞
        self.office_com('//div[@class="titleMain"]/ul/li[1]/div/ul/li[13]/ul/li[4]/a','//*[@class="productTitle"]/strong',u'Unify')
        self.hover()
        #点击云势软件客户关系管理系统
        self.office_com('//div[@class="titleMain"]/ul/li[1]/div/ul/li[13]/ul/li[5]/a','//*[@class="productTitle"]/strong',u'客户关系')
        self.hover()
        #点击云势软件架构指标管理系统
        self.office_com('//div[@class="titleMain"]/ul/li[1]/div/ul/li[13]/ul/li[6]/a','//*[@class="productTitle"]/strong',u'架构指标')
        self.hover()
        #点击云势软件奖金返利管理系统
        self.office_com('//div[@class="titleMain"]/ul/li[1]/div/ul/li[13]/ul/li[7]/a','//*[@class="productTitle"]/strong',u'奖金返利')
        self.hover()
        #ProcessOn
        self.office_com('//div[@class="titleMain"]/ul/li[1]/div/ul/li[13]/ul/li[8]/a','//*[@class="productTitle"]/strong',u'essOn')
        self.hover()
        #点击今目标
        self.office_com('//div[@class="titleMain"]/ul/li[1]/div/ul/li[13]/ul/li[9]/a','//*[@class="productTitle"]/strong',u'目标',check1=u'今目标')
        self.hover()
        #点击PGS航旅电子客票平台
        self.office_com('//div[@class="titleMain"]/ul/li[1]/div/ul/li[13]/ul/li[10]/a','//*[@class="productTitle"]/strong',u'PGS')
        self.hover()
        #点击服网云桌面解决方案
        self.office_com('//div[@class="titleMain"]/ul/li[1]/div/ul/li[13]/ul/li[11]/a','//*[@class="productTitle"]/strong',u'服网云')
        self.hover()
        #点击法大大
        self.office_com('//div[@class="titleMain"]/ul/li[1]/div/ul/li[13]/ul/li[12]/a','//*[@class="productTitle"]/strong',u'电子合同')



    def tearDown(self):
        self.driver.quit()