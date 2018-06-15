# _*_ coding:utf-8 _*_
__author__ = 'Lee'
from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get('http://stg.hnacloudmarket.com/')


driver.implicitly_wait(30)
driver.maximize_window()
time.sleep(5)
elem = driver.find_elements_by_class_name('nivo-imageLink')

# js = 'var li=document.getElementsByClassName("nivo-control"); li[0].setAttribute("class","nivo-control active")'
# driver.execute_script(js)
# time.sleep(10)

#urls=elem[0].get_attribute('href')

#driver.get(urls)

for i in range(0,6):
    urls=elem[i].get_attribute('href')
    driver.get(urls)
    time.sleep(1)
    driver.get('http://stg.hnacloudmarket.com/')
    time.sleep(5)
    elem = driver.find_elements_by_class_name('nivo-imageLink')

driver.quit()