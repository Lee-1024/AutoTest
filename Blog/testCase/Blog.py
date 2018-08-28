# _*_ coding:utf-8 _*_
__author__ = 'Lee'
from selenium import webdriver
import unittest
import time,random
from Common import LogiAndExit

class PublishBlog(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.binary_location = "C:\\Users\\amallayev\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"
        chrome_driver_binary = "C:\\Python27\\chromedriver.exe"
        self.driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
        #self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://stg.hnacloudmarket.com"
        self.imgs = []

    def add_img(self):
        #截图添加到测试报告中的方法
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def test_publish(self):
        """
        Blog
        """
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.find_element_by_class_name('apsClose').click()
        self.add_img()
        #点击博客
        self.driver.find_element_by_xpath('//div[@class="titleMain"]/ul/li[3]/span').click()
        #index click
        text = self.driver.find_element_by_xpath('//div[@class="main-div-panel-right "]/div[2]/div[2]/div/div[1]').text
        self.assertIn('nginx', text)
        text = self.driver.find_element_by_xpath('//div[@class="main-div-panel-right "]/div[3]/div[2]/div/div[8]').text
        self.assertIn('O2O',text)
        time.sleep(1)
        #login
        login = LogiAndExit()
        login.login(self.driver,'15044495530','l12345')

        time.sleep(6)
        text = self.driver.find_element_by_xpath('//div[@class="titleUserBtn clickable "]').text
        self.assertIn('T',text)

        #点击标签筛选
        #点击 nginx
        self.driver.find_element_by_xpath('//div[@class="main-div-panel-right "]/div[2]/div[2]/div/div[1]').click()
        # text = self.driver.find_element_by_xpath('//div[@class="main-div-panel-right "]/div[2]/div[2]/div/div[1]').text
        # self.assertIn('nginx',text)
        #点击 O2O
        self.driver.find_element_by_xpath('//div[@class="main-div-panel-right "]/div[3]/div[2]/div/div[8]').click()
        # text = self.driver.find_element_by_xpath('//div[@class="main-div-panel-right "]/div[3]/div[2]/div/div[8]').text
        # self.assertIn('O2O',text)
        time.sleep(1)
        self.add_img()
        self.driver.find_element_by_xpath('//div[@class="main-div-panel-right "]/div[1]/div/button[1]').click()
        self.add_img()
        time.sleep(3)
        #publish
        content = "The Zen of Python, " \
                  "by Tim Peters Beautiful is better than ugly." \
                  "Explicit is better than implicit." \
                  "Simple is better than complex." \
                  "Complex is better than complicated." \
                  "Flat is better than nested." \
                  "Sparse is better than dense." \
                  "Readability counts.📷" \
                  "Special cases aren't special enough to break the rules." \
                  "Although practicality beats purity." \
                  " should never pass silently." \
                  "Unless explicitly silenced." \
                  "In the face of ambiguity, refuse the temptation to guess." \
                  "There should be one-- and preferably only one --obvious way to do it." \
                  "Although that way may not be obvious at first unless you're Dutch." \
                  "Now is better than never.Although never is often better than *right* now." \
                  "If the implementation is hard to explain, it's a bad idea." \
                  "If the implementation is easy to explain, it may be a good idea." \
                  "Namespaces are one honking great idea -- let's do more of those!".decode('GBK')

        self.driver.find_element_by_xpath('//div[@class="ant-modal-footer"]/div/button[2]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/input').send_keys('The Zen of Python')
        self.driver.find_element_by_class_name('DraftEditor-root').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[@class="DraftEditor-editorContainer"]/div').send_keys(content)
        # self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[3]/div[2]/div/div[1]').click()
        # self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[4]/div[2]/div/div[1]').click()
        # self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[5]/div[2]/div/div[1]').click()
        #测试上传图片
        self.driver.find_element_by_xpath('//div[@class="RE-toolbar-root"]/span[7]').click()
        self.driver.find_element_by_id('url').send_keys('https://gss0.bdstatic.com/94o3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike150%2C5%2C5%2C150%2C50/sign=db37d3b8454a20a425133495f13bf347/3b87e950352ac65c8819edd9f1f2b21193138a78.jpg')
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[@class="RE-modal-root"]/form/div[2]/div/div/span/button').click()
        time.sleep(2)
        #创建一个随机数
        index = random.randint(1,11)
        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[3]/div[2]/div/div[6]').click()#展开
        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[3]/div[2]/div/div[%d]'%index).click()
        #创建一个随机数
        index = random.randint(1,30)
        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[4]/div[2]/div/div[6]').click()#展开
        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[4]/div[2]/div/div[%d]'%index).click()
        #创建一个随机数
        index = random.randint(1,25)
        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[5]/div[2]/div/div[6]').click()#展开
        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[5]/div[2]/div/div[%d]'%index).click()

        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[9]/div[2]/div/input').send_keys('0000')
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[11]/div[2]/div/button').click()
        time.sleep(1)
        text = self.driver.find_element_by_class_name('blog-reader-content-title').text
        self.assertIn(u'Python',text)
        self.add_img()
        #comment
        self.driver.find_element_by_xpath('//*[@class="blog-read-comment-main-input"]/textarea').send_keys('good')
        self.driver.find_element_by_xpath('//*[@class="blog-read-comment-main-input-btn"]/button').click()
        time.sleep(2)
        text = self.driver.find_element_by_class_name('blog-read-comment-item-content').text
        self.assertIn(u'good',text)
        self.add_img()
        #reply
        self.driver.find_element_by_class_name('blog-read-comment-item-bottom-reList').click()
        self.driver.find_element_by_xpath('//div[@class="blog-read-comment-item-recomment"]/div[3]/textarea').send_keys('good too')
        self.driver.find_element_by_xpath('//div[@class="blog-read-comment-item-recomment"]/div[3]/div/button').click()
        text = self.driver.find_element_by_xpath('//div[@class="blog-read-comment-item-recomment"]/div[2]/div[2]').text
        self.assertIn(u'too',text)

        #edit
        self.driver.find_element_by_xpath('//div[@class="blog-reader-content-actbar-author"]/div[1]').click()
        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/input').send_keys('The Zen of Python-1')
        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[9]/div[2]/div/input').send_keys('0000')
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[11]/div[2]/div/button').click()

        #返回博客首页截图
        time.sleep(2)
        self.driver.find_element_by_xpath('//div[@class="titleMain"]/ul/li[3]/span').click()
        time.sleep(1)
        target = self.driver.find_element_by_xpath('//div[@class="main-div-panel-right "]/div[1]/div/button[1]')
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        self.add_img()

        time.sleep(3)
        #重新进入发布的博客
        self.driver.find_element_by_xpath('//div[@class="content-title"]/a').click()
        time.sleep(2)

        #delete
        self.driver.find_element_by_xpath('//div[@class="blog-reader-content-actbar-author"]/div[3]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@class="ant-confirm-btns"]/button[2]').click()
        #eixt
        time.sleep(3)

        exit = LogiAndExit()
        exit.exit(self.driver)

        time.sleep(3)

    def tearDown(self):
        self.driver.quit()