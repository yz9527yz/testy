from selenium import  webdriver
from selenium.webdriver.common.by import By
import unittest

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get('http://localhost/redmine/login')

    def test_001_login_err(self):
        # 用例一：错误密码登录失败

        # 输入正确用户名
        self.driver.find_element(By.NAME,'username').send_keys('user')
        # 输入错误密码
        self.driver.find_element(By.NAME,'password').send_keys('error')
        # 点击登录
        self.driver.find_element(By.NAME,'login').click()
        # 登录失败后的提示信息
        ele = self.driver.find_element(By.ID,'flash_error')
        # 断言
        if ele.text == '无效的用户名或密码':
            print('pass')
        else:
            print('fail')

    def test_002_login_suc(self):
        # 用例二：正确密码登录成功

        # 输入正确用户名
        self.driver.find_element(By.NAME,'username').send_keys('user')
        # 输入正确密码
        self.driver.find_element(By.NAME,'password').send_keys('12345678')
        # 点击登录
        self.driver.find_element(By.NAME,'login').click()
        # 登录后显示的用户名
        name = self.driver.find_element(By.LINK_TEXT,'user')
        # 断言
        if name.text == 'user':
            print('pass')
        else:
            print('fail')

        def tearDown(self):
            self.driver.quit()
if __name__ == '__main__':
    unittest.main()