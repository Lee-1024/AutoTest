# _*_ coding:utf-8 _*_
__author__ = 'Lee'
from selenium import webdriver
import unittest
from Tools import GetShoot
from pyvirtualdisplay import Display

class BrowseBlog(unittest.TestCase):

    def setUp(self):
        display = Display(visible=0,size=(800,600))
        display.start()
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.url="http://"
        self.imgs = []

    def add_imgs(self):
        #截图添加到测试报告中的方法
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def test_Login(self):
        """
        登录
        """
        pass

    def test_browseCommunity(self):
        """
        社区浏览
        """
        pass

    def test_browseBlog(self):
        """
        博客浏览与发表评论
        """
        pass

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()



