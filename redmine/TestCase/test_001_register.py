import unittest
from redmine.PageObjects.redmine_operations import *
from redmine.Scenario.redmine_login import *
from parameterized import parameterized,param
from redmine.Data.var import *
import json
import time
from redmine.Common.log import logger
import logging

class TestRegister(unittest.TestCase):
    """
    注册
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get(register_url)
        logging.info('打开浏览器进入redmine注册界面')

    @parameterized.expand([('test03', '12345678', '12345678', '王', '小二', '22345678901@163.com', '1'),
                           ('', '12345678', '12345678', '王', '小二', '123456@163.com', '0'),
                           ('test02', '', '12345678', '王', '小二', '12345678901@163.com', '0'),
                           ('test02', '12345678', '', '王', '小二', '12345678901@163.com', '0'),
                           ('test02', '12345678', '12345678', '', '小二', '12345678901@163.com', '0'),
                           ('test02', '12345678', '12345678', '王', '', '12345678901@163.com', '0'),
                           ('test02', '12345678', '12345678', '王', '小二', '', '0'),
                           ('test02', '12345678', '12345678', '王', '小二', '12345678901', '0'),
                           ('test04', '12345678', '12345678', '王', '小二', '22345678901@163.com', '0'),
                           ('test03', '12345678', '12345678', '王', '小二', '22345578901@163.com', '0'),
                           ])
    def test_register(self, register_username, register_password,
                      confirm_password, first_name, last_name, user_mail, atatus):
        # 注册
        register_fail = ['邮件地址 是无效的','邮件地址 不能为空字符','邮件地址 已经被使用',
                         '密码 过短（最短为 8 个字符）','密码 与确认值不匹配',
                         '登录名 不能为空字符','登录名 已经被使用',
                         '名字 不能为空字符',
                         '姓氏 不能为空字符']
        RegisterPage(self.driver).enter_register_username(register_username)
        RegisterPage(self.driver).enter_register_password(register_password)
        RegisterPage(self.driver).enter_confirm_password(confirm_password)
        RegisterPage(self.driver).enter_first_name(first_name)
        RegisterPage(self.driver).enter_last_name(last_name)
        RegisterPage(self.driver).enter_user_mail(user_mail)
        RegisterPage(self.driver).click_submit()
        if atatus == '0':
            # 注册失败的提示信息
            try:
                ele = RegisterPage(self.driver).register_fail_info()
                self.assertIn(ele,register_fail)
                logging.info(ele)
            except Exception as e:
                logging.error(e)
        elif atatus == '1':
            # 注册成功的提示信息
            try:
                ele = RegisterPage(self.driver).register_succeed_info()
                self.assertEqual(ele,'您的帐号已被成功创建，正在等待管理员的审核。')
                logging.info(ele)
            except Exception as e:
                logging.error(e)
        else:
            logging.info('参数化的状态只能传0或1')

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()