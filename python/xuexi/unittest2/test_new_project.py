from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

# 通过时间戳构造唯一的项目名称
project_name = 'project_{}'.format(time.time())

class TestNewProject(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        # 访问’登录‘页面
        self.driver.get('http://localhost/redmine/login')
        # 输入正确用户名
        self.driver.find_element(By.NAME, 'username').send_keys('user')
        # 输入正确密码
        self.driver.find_element(By.NAME, 'password').send_keys('12345678')
        # 点击登录
        self.driver.find_element(By.NAME, 'login').click()

    def test_new_project(self):
        # 点击“项目”，进入’项目列表‘页面
        self.driver.find_element(By.LINK_TEXT,'项目').click()
        # 点击“新建项目”
        self.driver.find_element(By.LINK_TEXT,'新建项目').click()
        # 输入 项目名称
        self.driver.find_element(By.ID,'project_name').send_keys(project_name)
        # 点击’提交‘按钮
        self.driver.find_element(By.NAME,'commit').click()
        # 新建项目成功后的提示信息
        ele2 = self.driver.find_element(By.ID,'flash_notice')
        if ele2.text == '创建成功':
            print('pass')
        else:
            print('fail')

        def tearDown(self):
            self.driver.quit()


if __name__ == '__main__':
    unittest.main()