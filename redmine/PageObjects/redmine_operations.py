import logging
from redmine.PageObjects.redmine_locators import *
from selenium.webdriver.support.ui import Select
from redmine.Common.log import *

operations_log = logging.getLogger('redmine.PageObjects.operations')


class BasePage():
    # 构造一个基础类
    def __init__(self,driver):
        #  在初始化的时候自动执行
        self.driver = driver


class HomePage(BasePage):
    """
        "主页"页面 导航栏操作
    """
    def click_home_link(self):
        # 点击主页链接
        ele = self.driver.find_element(*HomePageLocators.HomeLink)
        ele.click()

    def click_porject_link(self):
        # 点击项目链接
        ele = self.driver.find_element(*HomePageLocators.ProjectLink)
        ele.click()

    def click_help_link(self):
        # 点击帮助链接
        ele = self.driver.find_element(*HomePageLocators.HelpLink)
        ele.click()

    def click_login_link(self):
        # 点击登录链接
        ele = self.driver.find_element(*HomePageLocators.LoginLink)
        ele.click()

    def click_register_link(self):
        # 点击注册链接
        ele = self.driver.find_element(*HomePageLocators.RegisterLink)
        ele.click()

    def searck(self,wd):
        # 点击搜索输入框
        ele = self.driver.find_element(*HomePageLocators.Search)
        ele.clear()
        ele.send_keys(wd)

    def project_select(self):
        # 选择一个项目
        ele = self.driver.find_element(*HomePageLocators.ProjectSelect)
        ele.click()

    def project_search(self,wd):
        # 项目搜索框
        ele = self.driver.find_element(*HomePageLocators.ProjectSearch)
        ele.clear()
        ele.send_keys(wd)


class RegisterPage(BasePage):
    """
        "注册"页面操作
    """
    logger = logging.getLogger('redmine.PageObjects.operations.register')

    def enter_register_username(self,register_username):
        # 输入注册用户名
        try:
            ele = self.driver.find_element(*RegisterPageLocators.RegisterUserName)
            ele.clear()
            ele.send_keys(register_username)
            logger.info('定位注册用户名输入框，清除并开始输入注册用户名')
        except Exception as e:
            logger.error(e)

    def enter_register_password(self,register_password):
        # 输入注册密码
        try:
            ele = self.driver.find_element(*RegisterPageLocators.RegisterPassWord)
            ele.clear()
            ele.send_keys(register_password)
            logger.info('定位注册密码输入框，清除并开始输入注册密码')
        except Exception as e:
            logger.error(e)

    def enter_confirm_password(self,confirm_password):
        # 输入确认密码
        try:
            ele = self.driver.find_element(*RegisterPageLocators.ConfirmPassWord)
            ele.clear()
            ele.send_keys(confirm_password)
            logger.info('定位确认注册密码输入框，清除并开始输入确认注册密码')
        except Exception as e:
            logger.error(e)

    def enter_first_name(self,first_name):
        # 输入姓
        try:
            ele = self.driver.find_element(*RegisterPageLocators.FirstName)
            ele.clear()
            ele.send_keys(first_name)
            logger.info('定位姓输入框，清除并开始输入姓')
        except Exception as e:
            logger.error(e)

    def enter_last_name(self,last_name):
        # 输入名
        try:
            ele = self.driver.find_element(*RegisterPageLocators.LasttName)
            ele.clear()
            ele.send_keys(last_name)
            logger.info('定位名输入框，清除并开始输入名')
        except Exception as e:
            logger.error(e)

    def enter_user_mail(self,user_mail):
        # 输入邮件地址
        try:
            ele = self.driver.find_element(*RegisterPageLocators.UserMail)
            ele.clear()
            ele.send_keys(user_mail)
            logger.info('定位邮箱地址输入框，清除并开始输入邮箱地址')
        except Exception as e:
            logger.error(e)

    def click_hide_mail(self, hide_mail):
        # 隐藏邮件复选框-checkbox
        ele = self.driver.find_element(*RegisterPageLocators.HideMail)
        ele.click()

    def select_language(self):
        # 选择语言
        ele = self.driver.find_element(*RegisterPageLocators.Language)
        Select(ele).select_by_value("zh-TW")

    def register_fail_info(self):
        # 返回注册失败提示信息
        ele = self.driver.find_element(*RegisterPageLocators.RegisterFailInfo)
        return ele.text

    def register_succeed_info(self):
        ele = self.driver.find_element(*RegisterPageLocators.RegisterCucceedInfo)
        return ele.text

    def click_submit(self):
        try:
            ele = self.driver.find_element(*RegisterPageLocators.Submit)
            ele.click()
            logger.info('提交注册信息')
        except Exception as e:
            logger.error(e)


class LoginPage(BasePage):
    """
        "登录"页面操作
    """
    def enter_username(self,username):
        # 输入登录名
        try:
            ele = self.driver.find_element(*LoginPageLocators.UserName)
            ele.clear()
            ele.send_keys(username)
            logger.info('定位登录名输入框，清除并开始输入登录名')
        except Exception as e:
            logger.error(e)

    def enter_password(self, password):
        # 输入登录密码
        try:
            ele = self.driver.find_element(*LoginPageLocators.PassWord)
            ele.clear()
            ele.send_keys(password)
            logger.info('定位密码输入框，清除并开始输入密码')
        except Exception as e:
            logger.error(e)

    def click_login_submit(self):
        # 点击”登录“按钮
        try:
            ele = self.driver.find_element(*LoginPageLocators.LoginSubmit)
            ele.click()
            logger.info('登录')
        except Exception as e:
            logger.error(e)

    def find_login_name(self):
        # 查找并返回登录成功后的元素
        ele = self.driver.find_element(*LoginPageLocators.LonginName)
        return ele

    def find_login_failed_info(self):
        # 查找并返回登录失败后的提示信息元素
        ele = self.driver.find_element(*LoginPageLocators.LoginFailedInfo)
        return ele.text


class ProjectListPage(BasePage):
    """
    项目列表 页面操作
    """
    def click_new_project(self):
        # 点击新建项目按钮
        try:
            ele = self.driver.find_element(*ProjectListPageLocators.NewProject)
            ele.click()
            logger.info('点击新建项目按钮')
        except Exception as e:
            logger.error(e)


class NewProjectPage(BasePage):
    """
    新建项目 页面操作
    """
    def enter_project_name(self,project_name):
        # 输入项目名称
        try:
            ele = self.driver.find_element(*NewProjectPageLocators.ProjectName)
            ele.send_keys(project_name)
            logger.info('定位项目名称输入框，清除并开始输入项目名称')
        except Exception as e:
            logger.error(e)

    def click_commit(self):
        # 点击项目创建按钮
        try:
            ele = self.driver.find_element(*NewProjectPageLocators.Commit)
            ele.click()
            logger.info('点击项目创建按钮')
        except Exception as e:
            logger.error(e)

    def click_comtiue(self):
        # 点击项目创建并继续添加按钮
        try:
            ele = self.driver.find_element(*NewProjectPageLocators.Continue)
            ele.click()
            logger.info('点击项目创建并继续添加按钮')
        except Exception as e:
            logger.error(e)

    def commit_succeed_info(self):
        # 项目创建成功提示信息
        ele = self.driver.find_element(*NewProjectPageLocators.CommitSucceedInfo)
        return ele.text