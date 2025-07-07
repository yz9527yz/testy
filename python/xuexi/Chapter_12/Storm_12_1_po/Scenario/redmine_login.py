from selenium import webdriver
from python.xuexi.Chapter_12.Storm_12_1_po.PageObject import redmine_operations


class LoginScenario(object):
    '''
    这里是定义‘登录’页面的场景
    '''
    def redmine_login(self):
        # 场景一：登录成功
        url = 'http://localhost/redmine/login'
        username1 = 'user'
        passward1 = '12345678'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(url)
        redmine_operations.LoginPage(driver).enter_username(username1)
        redmine_operations.LoginPage(driver).enter_password(passward1)
        redmine_operations.LoginPage(driver).click_login_button()
        return driver

if __name__ == '__main__':
    LoginScenario().redmine_login()