from selenium import webdriver
from redmine.PageObjects import redmine_operations
import time

class Login_Scenario(object):
    """
    这里定义“登录”页面的场景
    """
    def redmine_login(self):
        # 登录
        url = "http://localhost/redmine/login"
        username = 'user'
        password = '12345678'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.get(url)
        redmine_operations.LoginPage(driver).enter_username(username)
        redmine_operations.LoginPage(driver).enter_password(password)
        redmine_operations.LoginPage(driver).click_login_submit()
        return driver

if __name__ == '__main__':
    Login_Scenario().redmine_login()