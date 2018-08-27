# _*_ coding:utf-8 _*_
__author__ = 'Lee'
from selenium import webdriver
import unittest
import  time

class PublishBlog(unittest.TestCase):
    def setUp(self):
        # display = Display(visible=0,size=(800,600))
        # display.start()
        self.driver = webdriver.Chrome('C:\Python27\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.base_url = "https://community.stg.hnacloudmarket.com"
        self.imgs = []

    def add_img(self):
        #截图添加到测试报告中的方法
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def publish(self,num):
        self.driver.find_element_by_xpath('//div[@class="main-div-panel-right "]/div[1]/button[1]').click()
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
                  "Readability counts." \
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
                  "Namespaces are one honking great idea -- let's do more of those!"

        self.driver.find_element_by_xpath('//div[@class="ant-modal-footer"]/div/button[2]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/input').send_keys('The Zen of Python--%d'%num)
        #self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/div[2]').click()
        self.driver.find_element_by_class_name('DraftEditor-root').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[@class="DraftEditor-editorContainer"]/div').send_keys(content)
        time.sleep(3)
        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[3]/div[2]/div/div[1]').click()
        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[4]/div[2]/div/div[1]').click()
        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[5]/div[2]/div/div[6]').click()
        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[5]/div[2]/div/div[%d]'%num).click()
        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[9]/div[2]/div/input').send_keys('0000')
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[11]/div[2]/div/button').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div[2]').click()
    def test_publisBlog(self):
        """
        发表博客
        """
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        time.sleep(3)
        #login
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div[6]/div[1]').click()
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/span/div/div[2]/span[1]/input').send_keys('15044495530')
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/span/div/div[2]/span[2]/input').send_keys('123456')
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/span/div/div[3]/button').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div[2]').click()

        for i in range(1,26):
            self.publish(i)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()