#_*_ coding:utf-8 _*_
__author__ = 'Lee'
import sys
import os
import time
currentUrl = os.path.dirname(__file__)
parentUrl = os.path.abspath(os.path.join(currentUrl, os.pardir))
sys.path.append(parentUrl)
from selenium.webdriver.common.action_chains import ActionChains
class CommonMethod():

    def __init__(self):

        self.url = 'https://admin.stg.hnacloudmarket.com/'


    def WinMove(self,win,driver):
        """
        :param win: 传入第一个窗口的handle
        :param driver: 传入驱动实例
        :return: 窗口移动的方法，无返回值
        """
        windows = driver.window_handles#获取所有窗口handle
        for current_window in windows:   #循环遍历当handle不等于第一个窗口的handle时移动到该窗口
            if current_window != win:
                driver.switch_to.window(current_window)