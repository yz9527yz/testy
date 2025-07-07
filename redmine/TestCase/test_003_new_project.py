import time
import unittest

from redmine.Scenario import redmine_login
from redmine.PageObjects.redmine_operations import *
from redmine.Data.var import *
from redmine.Common.log import logger
import logging
class TestNewProject(unittest.TestCase):
    # 通过时间戳构造唯一的项目名称
    def setUp(self):
        #  登录，并访问”项目列表页面“

        self.driver = redmine_login.Login_Scenario().redmine_login()
        self.driver.get(new_project_url)
        logging.info('打开浏览器进入redmine新建项目界面')

    def test_new_project(self):
        try:
            project_name1 = 'project_{}'.format(time.time())
            # 点击新建项目按钮
            ProjectListPage(self.driver).click_new_project()
            # 输入 项目名称
            NewProjectPage(self.driver).enter_project_name(project_name1)
            # 点击’提交‘按钮
            NewProjectPage(self.driver).click_commit()
            # 新建项目成功后的提示信息
            ele = NewProjectPage(self.driver).commit_succeed_info()
            self.assertEqual(ele,'创建成功')
            logging.info('返回登录成功提示信息')
        except Exception as e:
            logging.error(e)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()