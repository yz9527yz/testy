import unittest,json,yaml
from redmine.PageObjects.redmine_operations import *
from redmine.Scenario.redmine_login import *
from parameterized import parameterized,param
from redmine.Common.parse_csv import *
from redmine.Data.var import *
import logging

def readJson():
    return json.load(open(r'E:\pythonfile\redmine\Data\test_login_data.json'))['data']

def readYaml():
    with open(r'E:\pythonfile\redmine\Data\test_login_data.yaml') as f:
        return list(yaml.unsafe_load_all(f))


class TestLogin(unittest.TestCase):
    """
    登录
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get(login_url)
        logging.info('打开浏览器进入redmine登录界面')
    # 方式一：用例中参数化
    #@parameterized.expand([('user','123','0'),('user','12345678','1')])

    # 方式二：数据分离 导入json data
    # @parameterized.expand([
    #     param(readJson()[0]['username'],readJson()[0]['password'],readJson()[0]['atatus']),
    #     param(readJson()[1]['username'], readJson()[1]['password'], readJson()[1]['atatus'])
    # ])

    # 方式三：数据分离 导入yaml data
    @parameterized.expand([
         param(readYaml()[0]['username'],readYaml()[0]['password'],readYaml()[0]['atatus']),
         param(readYaml()[1]['username'], readYaml()[1]['password'], readYaml()[1]['atatus']),
        ])

    def test_login(self,username,password,atatus):
        # 用例一：登录
        LoginPage(self.driver).enter_username(username)
        LoginPage(self.driver).enter_password(password)
        LoginPage(self.driver).click_login_submit()
        if atatus =='0':
            #   登录失败后的提示信息
            text = LoginPage(self.driver).find_login_failed_info()
            self.assertEqual(text,'无效的用户名或密码')
        elif atatus == '1':
            # 登录成功后显示的用户名
            name = LoginPage(self.driver).find_login_name().text
            self.assertIn(username,name)
        else:
            logging.info('参数化的状态只能传0或1')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()