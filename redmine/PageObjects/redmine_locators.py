from selenium.webdriver.common.by import By


class HomePageLocators():
    """
    "主页"页面 导航栏
    """
    HomeLink = (By.LINK_TEXT,"主页")  # 主页链接
    ProjectLink = (By.LINK_TEXT,"项目")  # 项目链接
    HelpLink = (By.LINK_TEXT,"帮助")   # 帮助链接
    LoginLink = (By.LINK_TEXT,"登录")  # 登录链接
    RegisterLink = (By.LINK_TEXT,"注册")  # 注册链接
    Search = (By.ID,"q") # 搜索输入框
    ProjectSelect = (By.ID,"project-jump")  # 选择一个项目
    ProjectSearch = (By.ID,"projects-quick-search")  # 项目搜索框


class RegisterPageLocators():
    """
    "注册"页面
    """
    RegisterUserName = (By.NAME,"user[login]")  # 登录名
    RegisterPassWord = (By.NAME,"user[password]")   # 密码
    ConfirmPassWord = (By.NAME,"user[password_confirmation]")   # 确认密码
    FirstName = (By.NAME,"user[firstname]")   # 名字
    LasttName = (By.NAME, "user[lastname]")  # 姓氏
    UserMail = (By.ID, "user_mail")  # 邮件地址
    HideMail = (By.ID, "pref_hide_mail")  # 隐藏我的邮件地址
    Language = (By.ID, "user_language")  # 语言   选择语言 Select(language).select_by_value("sq")
    Submit = (By.NAME, "commit")     # 提交
    RegisterFailInfo = (By.XPATH,"//*[@id='errorExplanation']/ul/li")    # 注册失败提示信息列表
    RegisterCucceedInfo = (By.XPATH,'//*[@id="flash_error"]')          # 注册成功提示信息


class LoginPageLocators():
    """
    "用户登录"界面
    """
    UserName = (By.ID,"username")  # 登录名
    PassWord = (By.ID, "password")  # 登录密码
    LoginSubmit = (By.ID, "login-submit")  # “登录”按钮
    LoginFailedInfo = (By.ID, "flash_error")  # 登录失败后的信息
    LonginName = (By.XPATH, "//*[@id='loggedas']")  # 登录成功后的信息


class ProjectListPageLocators():
    """
    "项目列表"页面
    """
    NewProject = (By.XPATH, '//*[@id="content"]/div[1]/a[1]')    # 新建项目列表


class NewProjectPageLocators():
    """
    “新建项目"页面
    """

    ProjectName = (By.ID, 'project_name')
    Commit = (By.NAME,'commit')
    Continue = (By.NAME,'continue')
    CommitSucceedInfo = (By.ID,'flash_notice')


class WorkBenchPageLocators():
    """
    "我的在工作挺"页面
    """
    pass


class AdministerPageLocators():
    """
    "管理"页面
    """
    pass


class HelpPageLocators():
    """
    "帮助"页面
    """
    pass








