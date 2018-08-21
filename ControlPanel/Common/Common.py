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