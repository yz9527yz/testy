from redmine.PageObjects.redmine_operations import *
from redmine.Scenario.redmine_login import *
import time

class NewProject_Scenario(object):
    """
    这里定义“新建项目”页面的场景
    """
    def redmine_new_project(self):
        # 通过时间戳构建唯一项目名
        project_name = 'project_{}'.format(time.time())
        # 登录
        driver = Login_Scenario().redmine_login()
        # 访问“项目列表”页面
        project_list_url = 'http://localhost/redmine/projects'
        driver.get(project_list_url)
        # 点击"新建项目"按钮
        ProjectListPage(driver).click_new_project()
        # 输入项目名称
        NewProjectPage(driver).enter_project_name(project_name)
        # 点击创建
        NewProjectPage(driver).click_commit()
        return driver


if __name__ == '__main__':
    NewProject_Scenario().redmine_new_project()