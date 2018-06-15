# _*_ coding:utf-8 _*_
__author__ = 'Lee'
from selenium import webdriver
import unittest,time
from selenium.webdriver.common.action_chains import ActionChains


class CloudServices(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        #self.base_url = "http://dev.hnacloudmarket.com/"
        #self.base_url = 'http://stg.hnacloudmarket.com/'
        self.base_url = 'http://www.hnacloudmarket.com/'
        self.driver.implicitly_wait(30)
        self.imgs = []

    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def homePage(self):
        self.driver.find_element_by_class_name('home-logo-img').click()
        time.sleep(3)
        self.driver.find_element_by_class_name('apsClose').click()
        time.sleep(4)

    def action(self):
        #鼠标悬停方法
        self.driver.find_element_by_xpath('//*[@id="menu-item-1329"]/span/span').click()
        ele = self.driver.find_element_by_xpath('//*[@id="menu-item-1329"]/span/span')
        ActionChains(self.driver).move_to_element(ele).perform()
        time.sleep(2)

    def step(self,ele1,ele2,ele3):
        #执行步骤方法
        self.driver.find_element_by_xpath(ele1).click()
        time.sleep(4)
        self.add_img()
        text = self.driver.find_element_by_xpath(ele2).text
        self.assertIn(ele3,text)

    def supportLinkButton(self):
        #点击联系我
        self.driver.find_element_by_id('supportLinkButton').click()
        self.driver.find_element_by_xpath('//*[@id="wpcf7-f349-o1"]/form/div[2]/div[7]/div/input').click()
        time.sleep(1)
        text = self.driver.find_element_by_xpath('//*[@id="wpcf7-f349-o1"]/form/div[2]/div[1]/div[2]/span/span').text
        self.assertIn(u'必填',text)
        self.add_img()
        self.driver.find_element_by_xpath('//*[@id="contactForm"]/div/span').click()

    def buy(self,ele1,ele2,ele3):
        #点击购买
        window_1 = self.driver.current_window_handle#获取当前窗口handle
        self.driver.find_element_by_xpath(ele1).click()
        time.sleep(3)
        windows = self.driver.window_handles#获取所有窗口handle
        for current_window in windows:   #循环遍历当handle不等于当前的handle时移动到该窗口
            if current_window != window_1:
                self.driver.switch_to.window(current_window)

        #text = self.driver.find_element_by_xpath('//*[@id="container-product"]/div[1]/div[1]/table[1]/tbody/tr/td[1]/span').text
        text = self.driver.find_element_by_xpath(ele2).text
        self.assertIn(ele3,text)
        self.driver.close()
        self.driver.switch_to.window(window_1)


    def test_cloudComputing(self):
        u"""云计算类别中的选项验证"""
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        time.sleep(4)
        self.driver.find_element_by_class_name('apsClose').click()
        self.action()
        #点击云服务器ECS
        self.driver.find_element_by_xpath('//*[@id="menu-item-1331"]/a/span').click()
        time.sleep(3)
        self.add_img()
        text = self.driver.find_element_by_xpath('//*[@class="productTitle"]/strong').text
        self.assertIn(u'云服务器 ECS',text)
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击华为云
        self.driver.find_element_by_xpath('//*[@id="menu-item-1332"]/a/span').click()
        time.sleep(3)
        self.add_img()
        text = self.driver.find_element_by_xpath('//*[@class="productTitle"]/strong').text
        self.assertIn(u'华为云',text)
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击金山云
        self.driver.find_element_by_xpath('//*[@id="menu-item-1333"]/a/span').click()
        time.sleep(3)
        self.add_img()
        text = self.driver.find_element_by_xpath('//*[@class="productTitle"]/strong').text
        self.assertIn(u'金山云服务器',text)
        self.supportLinkButton()
        self.buy('//*[@class="container"]/div/div[5]/div[2]/p[2]/a','//*[@id="container-product"]/div[1]/div[1]/table[1]/tbody/tr/td[1]/span',u'金山')
        self.homePage()
        self.action()
        #点击华为品质公有云
        self.driver.find_element_by_xpath('//*[@id="menu-item-1334"]/a/span').click()
        time.sleep(3)
        self.add_img()
        text = self.driver.find_element_by_xpath('//*[@class="productTitle"]/strong').text
        self.assertIn(u'华云', text)
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击易建VPS
        # self.driver.find_element_by_xpath('//*[@id="menu-item-1335"]/a/span').click()
        # time.sleep(3)
        # self.add_img()
        # text = self.driver.find_element_by_xpath('/html/body/div[5]/section/div/div[1]/div[2]/p').text
        # self.assertIn(u'易建',text)
        # self.supportLinkButton()
        # self.buy('/html/body/div[5]/section/div/div[3]/div[2]/p[2]/a','//*[@id="container-product"]/div[1]/div[1]/table[1]/tbody/tr/td[1]/span','VPS')
        # self.driver.find_element_by_class_name('home-logo-img').click()
        # time.sleep(3)
        # self.action()
        #点击创业云
        self.driver.find_element_by_xpath('//*[@id="menu-item-1336"]/a/span').click()
        time.sleep(3)
        self.add_img()
        text = self.driver.find_element_by_xpath('//*[@class="productTitle"]/strong').text
        self.assertIn(u'创业',text)
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击云服务器CVM
        self.driver.find_element_by_xpath('//*[@id="menu-item-1431"]/a/span').click()
        time.sleep(3)
        self.add_img()
        text = self.driver.find_element_by_xpath('//*[@class="productTitle"]/strong').text
        self.assertIn('CVM',text)
        self.supportLinkButton()

    def test_cloudNetwork(self):
        u"""云网络类别中选项验证"""
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        time.sleep(4)
        self.driver.find_element_by_class_name('apsClose').click()
        self.action()
        #点击负载均衡SLB
        self.driver.find_element_by_xpath('//*[@id="menu-item-1345"]/a/span').click()
        time.sleep(3)
        self.add_img()
        text = self.driver.find_element_by_xpath('//*[@class="productTitle"]/strong').text
        self.assertIn('SLB',text)
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击弹性IP
        self.driver.find_element_by_xpath('//*[@id="menu-item-1346"]/a/span').click()
        time.sleep(3)
        self.add_img()
        text = self.driver.find_element_by_xpath('//*[@class="productTitle"]/strong').text
        self.assertIn('IP',text)
        self.supportLinkButton()
        #self.buy('//div[@class="container"]/div/div[5]/div[2]/p[2]/a','//*[@id="listcat_129"]/table[1]/tbody/tr/td[1]/span',u'金山')
        self.homePage()
        self.action()
        #点击CDN
        self.driver.find_element_by_xpath('//*[@id="menu-item-1347"]/a/span').click()
        time.sleep(3)
        self.add_img()
        text = self.driver.find_element_by_xpath('//*[@class="productTitle"]/strong').text
        self.assertIn('CDN',text)
        self.supportLinkButton()


    def test_communicationProducts(self):
        u"""通信产品类别中选项验证"""
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        time.sleep(4)
        self.driver.find_element_by_class_name('apsClose').click()
        # self.action()
        # #点击科天云网络视频会议
        # self.driver.find_element_by_xpath('//*[@id="menu-item-1357"]/a/span').click()
        # time.sleep(3)
        # self.add_img()
        # text = self.driver.find_element_by_xpath('//*[@class="productTitle"]/strong').text
        # self.assertIn(u'科天',text)
        # self.homePage()
        # self.action()
        # #点击环信即时通讯云
        # self.driver.find_element_by_xpath('//*[@id="menu-item-1358"]/a/span').click()
        # time.sleep(3)
        # self.add_img()
        # text = self.driver.find_element_by_xpath('//*[@class="productTitle"]/strong').text
        # self.assertIn(u'环信',text)
        # self.homePage()
        # self.action()
        # #点击与真云视
        # self.driver.find_element_by_xpath('//*[@id="menu-item-1359"]/a/span').click()
        # time.sleep(3)
        # self.add_img()
        # text = self.driver.find_element_by_xpath('//*[@class="productTitle"]/strong').text
        # self.assertIn(u'真云',text)

        for i in range(3):
            lists = [u'科天',u'环信',u'真云']
            self.action()
            self.driver.find_element_by_xpath('//*[@id="menu-item-%d"]/a/span'%(1357+i)).click()
            time.sleep(3)
            self.add_img()
            text = self.driver.find_element_by_xpath('//*[@class="productTitle"]/strong').text
            self.assertIn(lists[i],text)
            self.supportLinkButton()
            self.homePage()

    def test_dataBase(self):
        u"""关系型数据库类别中选项验证"""
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        time.sleep(4)
        self.driver.find_element_by_class_name('apsClose').click()
        self.action()
        #点击云数据库RDS
        self.driver.find_element_by_xpath('//*[@id="menu-item-1375"]/a/span').click()
        time.sleep(3)
        self.add_img()
        text = self.driver.find_element_by_xpath('//*[@class="productTitle"]/strong').text
        self.assertIn(u'RDS',text)
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击关系数据库KRDS
        self.driver.find_element_by_xpath('//*[@id="menu-item-1376"]/a/span').click()
        time.sleep(3)
        self.add_img()
        text = self.driver.find_element_by_xpath('//*[@class="productTitle"]/strong').text
        self.assertIn(u'KRDS',text)
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击云数据库(CDB)
        self.driver.find_element_by_xpath('//*[@id="menu-item-1432"]/a/span').click()
        time.sleep(3)
        self.add_img()
        text = self.driver.find_element_by_xpath('//*[@class="productTitle"]/strong').text
        self.assertIn(u'CDB',text)
        self.supportLinkButton()
        self.homePage()

    def test_office(self):
        u"""通用办公类别中的选项验证"""
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        time.sleep(4)
        self.driver.find_element_by_class_name('apsClose').click()
        self.action()
        #点击Office365
        self.driver.find_element_by_xpath('//*[@id="menu-item-1385"]/a/span').click()
        time.sleep(3)
        self.add_img()
        text = self.driver.find_element_by_xpath('//*[@id="container-product"]/div[1]/div[1]/table[1]/tbody/tr/td[1]/span').text
        self.assertIn(u'365',text)
        self.driver.back()
        time.sleep(3)
        self.driver.find_element_by_class_name('apsClose').click()
        self.action()
        #点击WPS+云办公
        self.driver.find_element_by_xpath('//*[@id="menu-item-1386"]/a/span').click()
        time.sleep(3)
        self.add_img()
        text = self.driver.find_element_by_xpath('//*[@id="container-product"]/div[1]/div[1]/table[1]/tbody/tr/td[1]/span').text
        self.assertIn('WPS',text)
        self.driver.back()
        time.sleep(3)
        self.driver.find_element_by_class_name('apsClose').click()
        self.action()
        #点击编++
        self.driver.find_element_by_xpath('//*[@id="menu-item-1387"]/a/span').click()
        time.sleep(3)
        self.add_img()
        text = self.driver.find_element_by_xpath('//*[@class="productTitle"]/strong').text
        self.assertIn(u'编',text)
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击由你飞（Unify）
        self.driver.find_element_by_xpath('//*[@id="menu-item-1388"]/a/span').click()
        time.sleep(3)
        self.add_img()
        text = self.driver.find_element_by_xpath('//*[@class="productTitle"]/strong').text
        self.assertIn(u'由你',text)
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击云势软件客户关系管理系统
        self.driver.find_element_by_xpath('//*[@id="menu-item-1389"]/a/span').click()
        time.sleep(3)
        self.add_img()
        text = self.driver.find_element_by_xpath('//*[@class="productTitle"]/strong').text
        self.assertIn(u'客户关系',text)
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击云势软件架构指标管理系统
        self.driver.find_element_by_xpath('//*[@id="menu-item-1390"]/a/span').click()
        time.sleep(3)
        self.add_img()
        text = self.driver.find_element_by_xpath('//*[@class="productTitle"]/strong').text
        self.assertIn(u'架构指标',text)
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击云势软件奖金返利管理系统
        self.driver.find_element_by_xpath('//*[@id="menu-item-1391"]/a/span').click()
        time.sleep(3)
        self.add_img()
        text = self.driver.find_element_by_xpath('//*[@class="productTitle"]/strong').text
        self.assertIn(u'奖金返利',text)
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击ProcessOn
        self.driver.find_element_by_xpath('//*[@id="menu-item-1392"]/a/span').click()
        time.sleep(3)
        self.add_img()
        text = self.driver.find_element_by_xpath('//*[@class="productTitle"]/strong').text
        self.assertIn(u'ProcessOn',text)
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击今目标
        self.driver.find_element_by_xpath('//*[@id="menu-item-1393"]/a/span').click()
        time.sleep(3)
        self.add_img()
        text = self.driver.find_element_by_xpath('//*[@class="productTitle"]/strong').text
        self.assertIn(u'目标',text)
        self.supportLinkButton()
        self.buy('//*[@class="container"]/div/div[5]/div[2]/p[2]/a','//*[@id="container-product"]/div[1]/div[1]/table[1]/tbody/tr/td[1]/span',u'今目标')
        self.homePage()
        self.action()
        #点击PGS航旅电子客票平台
        self.driver.find_element_by_xpath('//*[@id="menu-item-1394"]/a/span').click()
        time.sleep(3)
        self.add_img()
        text = self.driver.find_element_by_xpath('//*[@class="productTitle"]/strong').text
        self.assertIn(u'航旅',text)
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击服网云桌面解决方案
        self.driver.find_element_by_xpath('//*[@id="menu-item-1435"]/a/span').click()
        time.sleep(3)
        self.add_img()
        text = self.driver.find_element_by_xpath('//*[@class="productTitle"]/strong').text
        self.assertIn(u'网云',text)
        self.supportLinkButton()
        self.homePage()

    def test_cloudStorage(self):
        u"""云存储类别中的选项验证"""
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        time.sleep(4)
        self.driver.find_element_by_class_name('apsClose').click()
        self.action()
        #点击对象存储OSS
        self.step('//*[@id="menu-item-1349"]/a/span','//*[@class="productTitle"]/strong','OSS')
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击对象存储KS3
        self.step('//*[@id="menu-item-1350"]/a/span','//*[@class="productTitle"]/strong',u'KS3')
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击对象存储(COS)
        self.step('//*[@id="menu-item-1433"]/a/span','//*[@class="productTitle"]/strong',u'COS')
        self.supportLinkButton()
        self.homePage()

    def test_securityService(self):
        u"""安全服务类别中的选项验证"""
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        time.sleep(4)
        self.driver.find_element_by_class_name('apsClose').click()
        self.action()
        #点击绿盟网站安全评估服务
        self.step('//*[@id="menu-item-1361"]/a/span','//*[@class="productTitle"]/strong',u'网站安全评估服务')
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击绿盟网站安全评估服务公安备案版
        self.step('//*[@id="menu-item-1362"]/a/span','//*[@class="productTitle"]/strong',u'公安备案')
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击绿盟极光自助扫描服务
        self.step('//*[@id="menu-item-1363"]/a/span','//*[@class="productTitle"]/strong',u'扫描服务')
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击绿盟网站安全监测服务
        self.step('//*[@id="menu-item-1364"]/a/span','//*[@class="productTitle"]/strong',u'安全监测')
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击绿盟网站安全防护服务
        self.step('//*[@id="menu-item-1365"]/a/span','//*[@class="productTitle"]/strong',u'防护服务')
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击绿盟堡垒机云服务
        self.step('//*[@id="menu-item-1366"]/a/span','//*[@class="productTitle"]/strong',u'堡垒机')
        self.supportLinkButton()
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击绿盟下一代防火墙云服务
        self.step('//*[@id="menu-item-1367"]/a/span','//*[@class="productTitle"]/strong',u'防火墙')
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击绿盟安全意识评估服务
        self.step('//*[@id="menu-item-1368"]/a/span','//*[@class="productTitle"]/strong',u'安全意识')
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击身份核验云
        self.step('//*[@id="menu-item-1369"]/a/span','//*[@class="productTitle"]/strong',u'身份核验')
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击防攻击中心
        self.step('//*[@id="menu-item-1370"]/a/span','//*[@class="productTitle"]/strong',u'防攻击')
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击Symantec/DigiCert SSL证书
        self.step('//*[@id="menu-item-1516"]/a/span','//*[@class="productTitle"]/strong',u'Symantec')
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击TrustAsia SSL证书
        self.step('//*[@id="menu-item-1520"]/a/span','//*[@class="productTitle"]/strong',u'TrustAsia')
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击GeoTrust SSL证书
        self.step('//*[@id="menu-item-1519"]/a/span','//*[@class="productTitle"]/strong',u'GeoTrust')
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击GlobalSign SSL证书
        self.step('//*[@id="menu-item-1517"]/a/span','//*[@class="productTitle"]/strong',u'GlobalSign')
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击CFCA SSL证书
        self.step('//*[@id="menu-item-1518"]/a/span','//*[@class="productTitle"]/strong',u'CFCA')
        self.supportLinkButton()
        self.homePage()

    def test_hadoop(self):
        u"""大数据类别中的选项验证"""
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        time.sleep(4)
        self.driver.find_element_by_class_name('apsClose').click()
        self.action()
        #点击拓尔思简查企业信息查询平台
        self.step('//*[@id="menu-item-1377"]/a/span','//*[@class="productTitle"]/strong',u'拓尔')
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击博雅智库
        self.step('//*[@id="menu-item-1378"]/a/span','//*[@class="productTitle"]/strong',u'博雅')
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击军犬舆情管家
        self.step('//*[@id="menu-item-1379"]/a/span','//*[@class="productTitle"]/strong',u'军犬')
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击环信客户互动云
        self.step('//*[@id="menu-item-1380"]/a/span','//*[@class="productTitle"]/strong',u'环信')
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击智能客服云
        self.step('//*[@id="menu-item-1381"]/a/span','//*[@class="productTitle"]/strong',u'智能')
        self.supportLinkButton()
        self.homePage()

    def test_superComputing(self):
        u"""超算与超融合类别中的选项验证"""
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        time.sleep(4)
        self.driver.find_element_by_class_name('apsClose').click()
        self.action()
        #点击并行超算公有云
        self.step('//*[@id="menu-item-1338"]/a/span','//*[@class="productTitle"]/strong',u'并行')
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击OITS在线运维
        self.step('//*[@id="menu-item-1339"]/a/span','//*[@class="productTitle"]/strong',u'在线运维')
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击应用运行特征采集器
        self.step('//*[@id="menu-item-1340"]/a/span','//*[@class="productTitle"]/strong',u'特征采集')
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击SDATA数据库一体机云平台
        self.step('//*[@id="menu-item-1341"]/a/span','//*[@class="productTitle"]/strong',u'一体机')
        self.supportLinkButton()
        self.homePage()

    def test_financial(self):
        u"""财务人事类别中的选项验证"""
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        time.sleep(4)
        self.driver.find_element_by_class_name('apsClose').click()
        self.action()
        #点击英盛网络商学院
        self.step('//*[@id="menu-item-1352"]/a/span','//*[@class="productTitle"]/strong',u'商学院')
        self.supportLinkButton()
        self.homePage()

    def test_baseInstallation(self):
        u"""大数据基础设置类别中的选项验证"""
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        time.sleep(4)
        self.driver.find_element_by_class_name('apsClose').click()
        self.action()
        #点击托管Hadoop KMR
        self.step('//*[@id="menu-item-1343"]/a/span','//*[@class="productTitle"]/strong',u'Hadoop')
        self.supportLinkButton()
        self.homePage()

    def test_internetMiddleware(self):
        u"""互联网中间件类别中的选项验证"""
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        time.sleep(4)
        self.driver.find_element_by_class_name('apsClose').click()
        self.action()
        #点击互联网金融云服务
        self.step('//*[@id="menu-item-1355"]/a/span','//*[@class="productTitle"]/strong',u'金融云')
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击金融风险管控云服务
        self.step('//*[@id="menu-item-1356"]/a/span','//*[@class="productTitle"]/strong',u'金融风险')
        self.supportLinkButton()
        self.homePage()

    def test_cloudManagement(self):
        u"""迁移与云管理类别中的选项验证"""
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        time.sleep(4)
        self.driver.find_element_by_class_name('apsClose').click()
        self.action()
        #点击华云数据企业级云计算平台
        self.step('//*[@id="menu-item-1382"]/a/span','//*[@class="productTitle"]/strong',u'华云')
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击华云数据vCAN服务
        self.step('//*[@id="menu-item-1383"]/a/span','//*[@class="productTitle"]/strong',u'CAN')
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击VMUltra异构云平台
        self.step('//*[@id="menu-item-1384"]/a/span','//*[@class="productTitle"]/strong',u'VM')
        self.supportLinkButton()
        self.homePage()

    def test_monitoringService(self):
        u"""监控服务类别中的选项验证"""
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(30)
        time.sleep(4)
        self.driver.find_element_by_class_name('apsClose').click()
        self.action()
        self.driver.maximize_window()
        #点击Smonitor数据库监控云平台
        self.step('//*[@id="menu-item-1396"]/a/span','//*[@class="productTitle"]/strong',u'监控云平')
        self.supportLinkButton()
        self.homePage()
        self.action()
        #点击监控宝
        self.step('//*[@id="menu-item-1434"]/a/span','//*[@class="productTitle"]/strong',u'监控宝')
        self.supportLinkButton()
        self.homePage()



if __name__ == '__main__':
    unittest.main()