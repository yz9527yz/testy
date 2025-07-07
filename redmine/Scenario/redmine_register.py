from selenium import webdriver
from redmine.PageObjects import redmine_operations


class Register_Scenario(object):
    """
    这里定义“注册”页面的场景
    """

    def redmine_registe(self):
        # 注册 成功
        url = "http://localhost/redmine/account/register"
        register_username1 = "admin"
        register_password1 = "12345678"
        confirm_password1 = "12345678"
        first_name1 = "王"
        last_name1 = "树根"
        user_mail1 = "123456@163.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.get(url)
        redmine_operations.RegisterPage(driver).enter_register_username(register_username1)
        redmine_operations.RegisterPage(driver).enter_register_password(register_password1)
        redmine_operations.RegisterPage(driver).enter_confirm_password(confirm_password1)
        redmine_operations.RegisterPage(driver).enter_first_name(first_name1)
        redmine_operations.RegisterPage(driver).enter_last_name(last_name1)
        redmine_operations.RegisterPage(driver).enter_user_mail(user_mail1)
        redmine_operations.RegisterPage(driver).click_submit()
        return driver


if __name__ == '__main__':
    Register_Scenario().redmine_registe()