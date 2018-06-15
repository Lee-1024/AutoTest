# _*_ coding:utf-8 _*_
__author__ = 'Lee'
from selenium import webdriver
from pyvirtualdisplay import Display
import unittest,time

class PublishBlog(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://www.baidu.com"
        self.display = Display(visible=0,size=(800,600))
        self.display.start()
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def test_login(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.implicitly_wait(30)
        driver.find_element_by_id("su").click()
        driver.implicitly_wait(30)
        text = driver.find_element_by_xpath('//*[@id="4001"]/div[1]/h3/a[1]/font').text
        if text == "selenium":
            print u"通过"

    def tearDown(self):
        self.driver.quit()
        self.display.stop()


if __name__ == "__main__":
    unittest.main()
