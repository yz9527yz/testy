from selenium.webdriver.common.by import By


class LoginPageLocators():
    '''
    ‘用户登录’ 页面
    '''
    # 用户名输入框
    UserName = (By.NAME, 'username')
    # 密码输入框
    PassWord = (By.NAME, 'password')
    # 登录按钮
    LoginButton = (By.NAME, 'login')
    # 登录失败后的提示信息
    LoginFailedInfo = (By.ID, 'flash_error')
    # 登录后显示的用户名
    LoginName = (By.ID, 'loggedas')


class ProjiectListPageLocators():
    '''
    '项目列表'页面
    '''
    # 新建项目按钮
    NewProject = (By.LINK_TEXT,'新建项目')

class NewProjectPageLocators():
    '''
    '新建项目'页面
    '''
    # 项目名称输入框
    ProjectName = (By.ID,'project_name')
    # 提交按钮
    CommitButton = (By.NAME,'commit')
    # 提交后的信息
    ProjectCommitInfo = (By.ID,'flash_notice')
