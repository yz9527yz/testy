from python.xuexi.Chapter_12.Storm_12_1_po.PageObject.redmine_operations import *
from python.xuexi.Chapter_12.Storm_12_1_po.Scenario.redmine_login import *
import time


class NewProjectScenario(object):
    """
    这里是定义‘新建项目’页面场景
    """
    def redmine_new_project(self):
        # 通过时间戳构造唯一项目名
        project_name = 'project_{}'.format(time.time())
        # 登录
        driver = LoginScenario().redmine_login()
        # 访问‘项目列表‘页面
        driver.get('http://localhost/redmine/projects/new')
        # 点击 ’新建项目‘ 按钮
        ProjectListPage().click_new_pro_btn()
        NewProjectPage().enter_projectname(project_name)
        NewProjectPage().click_com_btn()
        return driver


if __name__ == '__main__':
    NewProjectScenario().redmine_new_project()