# _*_ coding:utf-8 _*_
__author__ = 'Lee'
from selenium import webdriver
import unittest,time
from Tools import GetShoot
now=time.strftime("%Y%m%d%H%S%S",time.localtime())

class BaiduSearch(unittest.TestCase):
    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.options.binary_location = "C:\Users\Bill\AppData\Local\Google\Chrome\Application\chrome.exe"
        self.chrome_driver_binary = "C:\Python27\chromedriver.exe"
        self.driver = webdriver.Chrome(self.chrome_driver_binary,chrome_options=self.options)
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"

    def test_search(self):
        '''百度搜索'''
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.implicitly_wait(30)
        driver.find_element_by_id("su").click()
        driver.implicitly_wait(30)
        text = driver.find_element_by_xpath('//*[@id="1"]/h3/a/em').text
        #//*[@id="1"]/h3/a/em '//*[@id="4001"]/div[1]/h3/a[1]/font'
        # if text == "Selenium":
        #     print u"通过"
        # else:
        #     print u'不通过'
        #     driver.get_screenshot_as_file("D:\\WORK\\AutoTest\\report\\shoot\\msg"+now+".jpg")
        getshot=GetShoot.GetShoot(driver)
        getshot.get_windows_img()
        self.assertEqual(text,'selenium')




    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()