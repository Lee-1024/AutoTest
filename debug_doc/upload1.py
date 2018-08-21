#_*_ coding:utf-8 _*_
__author__ = 'Lee'
from selenium import webdriver
import time,os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.implicitly_wait(8)

driver.get('https://admin.stg.hnacloudmarket.com/knowledge/product/')

time.sleep(5)

driver.find_element_by_xpath('//div[@class="prod-container"]/div[2]/button/span[1]').click()
time.sleep(2)

driver.find_element_by_xpath('//div[@class="dialog-main"]/div/div[3]/div[2]/span/div[1]/span/input').send_keys('C:\\Users\\Bill\\Desktop\\google.jpg')

time.sleep(3)

ele=driver.find_element_by_xpath('//div[@class="DraftEditor-editorContainer"]/div/div/div[3]/div/h1/span/span')
#time.sleep(20)

ActionChains(driver).click(ele).send_keys(Keys.RIGHT,Keys.RIGHT).perform()

#driver.find_element_by_xpath('//div[@class="DraftEditor-editorContainer"]/div/div/div[3]/div/h1/span/span').send_keys(Keys.RIGHT)
print(driver.title)
print driver.current_url