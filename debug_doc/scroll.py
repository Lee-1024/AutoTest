#_*_ coding:utf-8 _*_
__author__ = 'Lee'
from selenium import webdriver
import time
'''
以简书首页为
'''
driver=webdriver.Chrome()
driver.get("http://www.jianshu.com")
#等待页面加载3S time.sleep(3)
'''
0：为顶部；1000000：为底部
#将滚动条移动到页面的顶部
js="var q=document.documentElement.scrollTop=0"
driver.execute_script(js)
#页面内嵌窗口浏览条滚动
js="var q=document.getElementById('id').scrollTop=1000"
driver.execute_script(js)
time.sleep(3)
'''
#将页面滚动条拖到底部
# js="var q=document.documentElement.scrollTop=100000"
# driver.execute_script(js)
# time.sleep(3)

target = driver.find_element_by_id('index-aside-download-qrbox')
driver.execute_script("arguments[0].scrollIntoView();", target)

time.sleep(5)
