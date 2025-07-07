import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
import unittest
import ddt

@ddt.ddt()
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get('http://localhost/redmine/login')


    '''
    1.@ddt.data,括号中可以传递列表或元祖
    2.这里传递了两个列表，代表了两个测试用例
    3.每个测试用例包含三个参数
        1.用户名取值
        2.密码取值
        3.登录成功与否：我们约定0代表登录失败，1代表登录成功
    '''

    @ddt.data(['user','error','0'],['user','12345678','1'])
    @ddt.unpack
    def test_001_login(self,username,password,status):
        # 输入用户名
        self.driver.find_element(By.NAME, 'username').clear()
        self.driver.find_element(By.NAME, 'username').send_keys(username)
        # 输入密码
        self.driver.find_element(By.NAME, 'password').clear()
        self.driver.find_element(By.NAME, 'password').send_keys(password)
        # 点击登录
        self.driver.find_element(By.NAME, 'login').click()
        # 判断登录状态
        if status == '0':
            # 登录失败后的提示信息
            ele = self.driver.find_element(By.ID, 'flash_error')
            self.assertEqual('无效的用户名或密码',ele.text)
        elif status == '1':
            # 登录后显示的用户名
            name = self.driver.find_element(By.LINK_TEXT, 'user')
            self.assertEqual('user',name.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':

    unittest.main()