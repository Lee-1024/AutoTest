# _*_ coding:utf-8 _*_
__author__ = 'Lee'
from selenium import webdriver
import unittest,time
from selenium.webdriver.common.action_chains import ActionChains

class CloudOther(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
       #self.base_url = "http://dev.hnacloudmarket.com/"
        #self.base_url ='http://stg.hnacloudmarket.com/'
        self.base_url = 'http://www.hnacloudmarket.com/'
        self.driver.implicitly_wait(30)
        self.imgs = []

    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def homePage(self):
        self.driver.find_element_by_class_name('home-logo-img').click()
        time.sleep(4)
        self.driver.find_element_by_class_name('apsClose').click()
        time.sleep(3)

    def action(self):
        #鼠标悬停方法
        self.driver.find_element_by_xpath('//*[@id="menu-item-1398"]/span/span').click()
        ele = self.driver.find_element_by_xpath('//*[@id="menu-item-1398"]/span/span')
        ActionChains(self.driver).move_to_element(ele).perform()
        time.sleep(4)



    def test_procurement(self):
        u"""一站式采购验证"""
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        time.sleep(4)
        self.driver.find_element_by_class_name('apsClose').click()
        self.driver.find_element_by_xpath('//*[@id="menu-item-1397"]/a/span').click()
        time.sleep(3)
        self.add_img()
        text = self.driver.find_element_by_xpath('//*[@id="big-footer"]/div/div/div[3]/a').text
        self.assertIn(u'云集市',text)
        self.driver.back()

    def test_partner(self):
        u"""成为合作伙伴"""
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.find_element_by_class_name('apsClose').click()
        self.action()
        #代理商
        self.driver.find_element_by_xpath('//*[@id="menu-item-1399"]/a/span').click()
        time.sleep(3)
        self.add_img()
        text = self.driver.find_element_by_xpath('//*[@id="become-a-partner"]/div/div/div[2]/a[1]').text
        self.assertIn(u'申请',text)
        window_1 = self.driver.current_window_handle#获取当前窗口handle
        #点击申请
        self.driver.find_element_by_xpath('//*[@id="become-a-partner"]/div/div/div[2]/a[1]').click()
        time.sleep(5)
        windows = self.driver.window_handles#获取所有窗口handle
        for current_window in windows:   #循环遍历当handle不等于当前的handle时移动到该窗口
            if current_window != window_1:
                self.driver.switch_to.window(current_window)

        text = self.driver.find_element_by_xpath('//*[@class="applyTit"]/h2').text
        self.assertIn(u'代理',text)
        self.driver.find_element_by_id('affiliateSubmit').click()
        text = self.driver.find_element_by_id('username-error').text
        self.assertIn(u'必填',text)
        self.add_img()
        self.driver.close()
        self.driver.switch_to.window(window_1)
        self.action()
        #厂商加盟
        self.driver.find_element_by_xpath('//*[@id="menu-item-1400"]/a/span').click()
        time.sleep(3)
        self.add_img()
        text = self.driver.find_element_by_xpath('//*[@id="become-a-partner"]/div/div/div[2]/a').text
        self.assertIn(u'联系我们',text)
        #点击联系我们
        window_1 = self.driver.current_window_handle
        self.driver.find_element_by_xpath('//*[@id="become-a-partner"]/div/div/div[2]/a').click()
        time.sleep(5)
        windows = self.driver.window_handles#获取所有窗口handle
        for current_window in windows:   #循环遍历当handle不等于当前的handle时移动到该窗口
            if current_window != window_1:
                self.driver.switch_to.window(current_window)

        text = self.driver.find_element_by_xpath('//*[@class="blue-heading"]/strong').text
        self.assertIn(u'联系',text)
        #self.driver.find_element_by_xpath('/html/body/div[5]/section/div/div/div/div[2]/div[2]/input').click()
        self.driver.find_element_by_xpath('//*[@id="wpcf7-f349-p366-o1"]/form/div[2]/div[7]/div/input').click()
        text = self.driver.find_element_by_xpath('//*[@id="wpcf7-f349-p366-o1"]/form/div[2]/div[1]/div[2]/span/span').text
        self.assertIn(u'必填',text)
        self.add_img()
        self.driver.close()
        self.driver.switch_to.window(window_1)
        self.homePage()

    def test_support(self):
        u"""支持"""
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        time.sleep(4)
        self.driver.find_element_by_class_name('apsClose').click()
        self.driver.find_element_by_xpath('//*[@id="menu-item-133"]/a/span').click()
        time.sleep(3)
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
        self.homePage()

    def test_login(self):
        u"""登录"""
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        time.sleep(4)
        self.driver.find_element_by_class_name('apsClose').click()
        self.driver.find_element_by_xpath('//*[@id="left-bar-top"]/div[3]/a[1]').click()
        time.sleep(5)
        window_1 = self.driver.current_window_handle#获取当前窗口handle
        windows = self.driver.window_handles#获取所有窗口handle
        for current_window in windows:   #循环遍历当handle不等于当前的handle时移动到该窗口
            if current_window != window_1:
                self.driver.switch_to.window(current_window)
        time.sleep(3)
        self.add_img()
        self.driver.find_element_by_id('inp_user').send_keys('1111')
        self.driver.find_element_by_id('inp_password').send_keys('22222')
        self.driver.find_element_by_xpath('//*[@id="sel_lang"]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="sel_lang"]/option[2]').click()
        self.driver.find_element_by_xpath('//*[@id="ccp-login"]/div/div/div/div[1]').click()
        self.driver.find_element_by_id('login').click()
        time.sleep(2)
        self.add_img()
        text = self.driver.find_element_by_xpath('//*[@id="ccp-login"]/div/div/div/div[1]/span[2]').text
        self.assertIn(u'请重试',text)
        self.driver.close()
        self.driver.switch_to.window(window_1)




if __name__ == '__main__':
    unittest.main()