#_*_ coding:utf-8 _*_
__author__ = 'Lee'

from selenium import webdriver
import time,os

driver = webdriver.Chrome()
driver.implicitly_wait(8)

file_path = os.path.abspath('C:\\Users\\Bill\\Desktop\\upload.html')#脚本与upload_file.html在同一个目录
driver.get(file_path)

time.sleep(5)

driver.find_element_by_name('file').send_keys('C:\\Users\\Bill\\Desktop\\google.jpg')#定位上传按钮，添加本地文件
time.sleep(3)
print(driver.title)  #把页面的title打印出来

