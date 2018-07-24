#_*_ coding:utf-8 _*_
__author__ = 'Lee'
from selenium.webdriver.common.action_chains import ActionChains
class CommonMethod():

    def isElementExist(self,xp,driver):
        """
        :param xp: 元素位置XPATH
        :param driver: 输入驱动实例
        :return:判断元素是否存在方法，存在返回True,不存在返回False
        """
        try:
            driver.find_element_by_xpath(xp)
            return True
        except:
            return False

    def WinMove(self,win,driver):
        """
        :param win: 传入第一个窗口的handle
        :param driver: 传入驱动实例
        :return: 窗口移动的方法，无返回值
        """
        windows = driver.window_handles#获取所有窗口handle
        for current_window in windows:   #循环遍历当handle不等于当前的handle时移动到该窗口
            if current_window != win:
                driver.switch_to.window(current_window)

    def hover(self,elem,driver):
        """
        :param elem: 要悬停的元素的xpath
        :param driver: 传入驱动实例
        :return:元素悬停方法，无返回值
        """
        elem = driver.find_element_by_xpath(elem)
        ActionChains(driver).move_to_element(elem).perform()