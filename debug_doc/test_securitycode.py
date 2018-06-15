# _*_ coding:utf-8 _*_
__author__ = 'Lee'
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import yagmail

browser = webdriver.Chrome()
browser.get('file:///D:/WORK/test.html')

source = browser.find_element_by_id('dragHandler') #获取要移动的元素
#ActionChains(browser).click_and_hold(source).perform()
#ActionChains(browser).drag_and_drop(source,260).perform()
ActionChains(browser).drag_and_drop_by_offset(source,260,0).perform() #将元素向右移动260像素
time.sleep(2000)

window_1 = browser.current_window_handle #获取当前窗口handle
windows = browser.window_handles #获取所有窗口handle
for current_window in windows:   #循环遍历当handle不等于当前的handle时移动到该窗口
    if current_window != window_1:
        browser.switch_to.window(current_window)

ActionChains(browser).move_to_element(source).perform() #鼠标悬停
elm = browser.find_element_by_link_text("设置").click()
browser.quit()



#链接邮箱服务器
yag = yagmail.SMTP( user="user@126.com", password="1234", host='smtp.126.com')

# 邮箱正文
contents = ['This is the body, and here is just text http://somedomain/image.png',
            'You can find an audio file attached.', '/local/path/song.mp3']

# 发送邮件
yag.send('taaa@126.com', 'subject', contents)
# 发送带附件邮件
yag.send('aaaa@126.com', '发送附件', contents, ["d://log.txt","d://baidu_img.jpg"])