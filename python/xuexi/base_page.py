from time import sleep
from selenium import webdriver

class Base_page(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法
    """

    def __init__(self,driver):
        self.driver = driver


        # get and url link
        # get方法连接url

    def oper(self,url):
        self.driver.get(url)

        # quit browser and testing
        # 退出浏览器

    def quit_browser(self):
        self.driver.quit()

        # 浏览器前进操作 forward

    def forward(self):
        self.driver.forward()

        # 浏览器后退操作 back

    def back(self):
        self.driver.back()

