# _*_ coding:utf-8 _*_
__author__ = 'Lee'
import time
from selenium.webdriver.common.action_chains import ActionChains

class LogiAndExit():

    def login(self,driver,moblie,code):
        driver.find_element_by_xpath('//div[@class="titleUserBtnGroup"]/div[1]').click()
        driver.find_element_by_xpath('//div[@class="login-modal-main-inputs"]/span[1]/input').send_keys(moblie)
        time.sleep(1)
        driver.find_element_by_xpath('//div[@class="login-modal-main-inputs"]/span[2]/input').send_keys(code)
        driver.find_element_by_xpath('//div[@class="login-modal-main-btns"]/button').click()

    def exit(self,driver):
        driver.find_element_by_xpath('//div[@class="titleUserPic"]/img').click()
        ele = driver.find_element_by_xpath('//div[@class="titleUserPic"]/img')
        ActionChains(driver).move_to_element(ele).perform()
        time.sleep(3)
        driver.find_elements_by_class_name('titleUserMenuItem')[1].click()
