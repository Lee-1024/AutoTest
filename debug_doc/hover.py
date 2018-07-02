# _*_ coding:utf-8 _*_
__author__ = 'Lee'
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()

driver.get('https://community.stg.hnacloudmarket.com/')
driver.maximize_window()
time.sleep(5)
elem = driver.find_element_by_xpath('//div[@class="titleMain"]/ul/li[1]/span')
ActionChains(driver).move_to_element(elem).perform()
time.sleep(5)

checks = ['ECS',u'华为',u'金山',u'华云',u'创业',u'CVM']

for i in checks:
    print i



driver.quit()