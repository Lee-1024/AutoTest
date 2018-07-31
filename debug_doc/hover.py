# _*_ coding:utf-8 _*_
__author__ = 'Lee'
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()

driver.get('https://stg.hnacloudmarket.com/')
driver.maximize_window()
time.sleep(3)
driver.find_element_by_class_name('apsClose').click()
elem1 = driver.find_element_by_xpath('//div[@class="titleMain"]/ul/li[1]/span')
ActionChains(driver).move_to_element(elem1).perform()
time.sleep(1)
elem2 = driver.find_element_by_xpath('//div[@class="titleSpan"]/div[2]/ul/li[1]/ul/li[4]')
ActionChains(driver).move_to_element(elem2).perform()
time.sleep(1)
elem3 = driver.find_element_by_xpath('//div[@class="titleSpan"]/div[2]/ul/li[2]/ul/li[1]')
ActionChains(driver).move_to_element(elem3).perform()
elem4 = driver.find_element_by_xpath('//div[@class="titleSpan"]/div[2]/ul/li[3]/div/span[1]')
ActionChains(driver).move_to_element(elem4).perform()
driver.find_element_by_xpath('//div[@class="titleSpan"]/div[2]/ul/li[3]/div/span[1]').click()
time.sleep(8)




driver.quit()