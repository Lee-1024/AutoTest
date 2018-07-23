#_*_ coding:utf-8 _*_
__author__ = 'Lee'
from selenium.webdriver.common.action_chains import ActionChains
class CommonMethod():

    def isElementExist(self,xp,driver):
        #判断购买按钮是否存在
        try:
            driver.find_element_by_xpath(xp)
            return True
        except:
            return False

    def WinMove(self,win,driver):
        #窗口移动
        windows = driver.window_handles#获取所有窗口handle
        for current_window in windows:   #循环遍历当handle不等于当前的handle时移动到该窗口
            if current_window != win:
                driver.switch_to.window(current_window)

    def hover(self,elem,driver):
        #悬停
        elem = driver.find_element_by_xpath(elem)
        ActionChains(driver).move_to_element(elem).perform()