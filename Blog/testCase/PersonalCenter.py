# _*_ coding:utf-8 _*_
__author__ = 'Lee'
from selenium import webdriver
import unittest
from selenium.webdriver.common.action_chains import ActionChains
import time,random,uuid
from Common import LogiAndExit



class PersonalCenter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://stg.hnacloudmarket.com"
        #self.base_url = "https://10.125.1.236/"
        self.imgs = []

    def add_img(self):
        #截图添加到测试报告中的方法
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def hover(self):
        self.driver.find_element_by_xpath('//div[@class="titleUserPic"]/img').click()
        ele = self.driver.find_element_by_xpath('//div[@class="titleUserPic"]/img')
        time.sleep(2)
        ActionChains(self.driver).move_to_element(ele).perform()
        time.sleep(2)
        self.driver.find_elements_by_class_name('titleUserMenuItem')[0].click()

    def test_center(self):
        u"""personalcenter"""
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.driver.find_element_by_class_name('apsClose').click()
        #login
        login = LogiAndExit()
        login.login(self.driver,'17600591024','123456')
        time.sleep(5)
        firsrn = self.driver.find_element_by_xpath('//div[@class="titleUserBtn clickable "]').text
        self.assertIn('HNA',firsrn)

        time.sleep(2)
        self.driver.find_element_by_class_name('titleMain').click()
        ele = self.driver.find_element_by_class_name('titleMain')
        ActionChains(self.driver).move_to_element(ele).perform()
        time.sleep(2)

        #hover
        self.hover()
        time.sleep(1)
        self.add_img()

        #modified data
        self.driver.find_element_by_class_name('ant-btn').click()
        num = random.randint(100,2000)
        nickname = 'HNA-'+str(uuid.uuid1())[0:11]
        time.sleep(3)
        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[2]/div[2]/input').clear()
        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[2]/div[2]/input').send_keys(nickname)
        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[2]/div[2]/button').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//div[@class="ant-confirm-btns"]/button[2]').click()

        time.sleep(1)

        #--intro
        intro = 'I HAVE A DREAM%d'%num
        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[4]/div[2]/textarea').clear()
        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[4]/div[2]/textarea').send_keys(intro)
        #--name
        name = 'Tony%d'%num
        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[5]/div[2]/input').clear()
        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[5]/div[2]/input').send_keys(name)
        #--email
        email = 'Tony%d@cc.com'%num
        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[6]/div[2]/input').clear()
        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[6]/div[2]/input').send_keys(email)
        #--QQ
        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[7]/div[2]/input').clear()
        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[7]/div[2]/input').send_keys(num)
        #--Weixin
        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[8]/div[2]/input').clear()
        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[8]/div[2]/input').send_keys(num)
        #--position
        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[9]/div[2]/input').clear()
        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[9]/div[2]/input').send_keys(num)
        #--company
        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[10]/div[2]/input').clear()
        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[10]/div[2]/input').send_keys(num)
        #--address
        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[11]/div[2]/textarea').clear()
        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[11]/div[2]/textarea').send_keys(num)
        #--submit
        self.driver.find_element_by_xpath('//div[@class="main-div-container"]/div/div[12]/div[2]/button').click()

        self.hover()
        time.sleep(1)
        rename = self.driver.find_element_by_xpath('//div[@class="personal-info-panel-info"]/div[2]').text
        self.assertEqual(nickname,rename)
        self.driver.find_element_by_class_name('ant-btn').click()
        time.sleep(2)
        self.add_img()

        time.sleep(2)
        #back center
        self.driver.find_element_by_class_name('titleMain').click()
        ele = self.driver.find_element_by_class_name('titleMain')
        ActionChains(self.driver).move_to_element(ele).perform()
        time.sleep(2)
        self.hover()
        #fans number
        time.sleep(1)
        text = self.driver.find_element_by_xpath('//div[@class="main-div-panel-right "]/div[2]/div/div[1]/div[1]/div[1]').text
        self.assertEqual('2',text)
        #attention number
        time.sleep(1)
        text = self.driver.find_element_by_xpath('//div[@class="main-div-panel-right "]/div[2]/div/div[1]/div[3]/div[1]').text
        self.assertEqual('2',text)


    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()



