from selenium import webdriver
from redmine.PageObjects import redmine_operations


class Home_Scenario(object):
    """
    这里定义“主页”页面的场景
    """

    def redmine_click_home_link(self):
        # 点击"主页"链接进行页面跳转
        url = "http://localhost/redmine/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait()
        driver.get(url)
        redmine_operations.HomePage(driver).click_home_link()

    def redmine_click_porject_link(self):
        # 点击"项目"链接进行页面跳转
        url = "http://localhost/redmine/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait()
        driver.get(url)
        redmine_operations.HomePage(driver).click_porject_link()

    def redmine_click_help_link(self):
        # 点击"帮助"链接进行页面跳转
        url = "http://localhost/redmine/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait()
        driver.get(url)
        redmine_operations.HomePage(driver).click_help_link()

    def redmine_click_login_link(self):
        # 点击"登录"链接进行页面跳转
        url = "http://localhost/redmine/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait()
        driver.get(url)
        redmine_operations.HomePage(driver).click_login_link()

    def redmine_click_register_link(self):
        # 点击"注册"链接进行页面跳转
        url = "http://localhost/redmine/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait()
        driver.get(url)
        redmine_operations.HomePage(driver).click_register_link()

    def redmine_searck(self,wd):
        # 点击搜索输入框
        url = "http://localhost/redmine/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait()
        driver.get(url)
        redmine_operations.HomePage(driver).searck(wd)

    def redmine_project_select(self):
        # 选择一个项目
        url = "http://localhost/redmine/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait()
        driver.get(url)
        redmine_operations.HomePage(driver).project_select()

    def redmine_project_search(self,wd):
        # 项目搜索框
        url = "http://localhost/redmine/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait()
        driver.get(url)
        redmine_operations.HomePage(driver).project_search(wd)


