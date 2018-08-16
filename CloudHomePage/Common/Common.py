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

        self.url = 'https://stg.hnacloudmarket.com/'

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
        for current_window in windows:   #循环遍历当handle不等于第一个窗口的handle时移动到该窗口
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

    def roll(self,elem,driver):
        """
        :param elem: 需要滚动到的位置的XPATH
        :param driver: 驱动实例
        :return: 将屏幕滚动到某个元素位置的方法，无返回值
        """
        target = driver.find_element_by_xpath(elem)
        driver.execute_script("arguments[0].scrollIntoView();", target)


    def contact_us(self,index,companyna,userna,tel,content,driver,email=""):
        """
        :param index: 选择第几个问题类型
        :param companyna: 公司名称
        :param userna: 用户名称
        :param tel: 电话
        :param content:留言信息
        :param driver: 传入驱动
        :param email: 邮件，默认为空
        :return:联系我们的发送邮件测试方法
        """
        #点击问题类型并选择
        driver.find_element_by_xpath('//*[@id="titleType"]/div/span').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li[%d]'%index).click()
        #输入公司名称
        driver.find_element_by_id('companyName').send_keys(companyna)
        #输入联系人姓名
        driver.find_element_by_id('userName').send_keys(userna)
        #输入联系人电话
        driver.find_element_by_id('userTel').send_keys(tel)
        #输入邮箱
        driver.find_element_by_id('eMail').send_keys(email)
        #输入留言
        driver.find_element_by_id('content').send_keys(content)
        #点击提交
        time.sleep(0.5)
        driver.find_element_by_xpath('//div[@class="contact-form-main-contact"]/div[7]/div/div/div/div/span/button').click()
