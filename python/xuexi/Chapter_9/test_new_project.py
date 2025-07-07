from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 通过时间戳构造唯一的项目名称
project_name = 'project_{}'.format(time.time())
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

# 访问’登录‘页面
driver.get('http://localhost/redmine/login')
# 输入正确用户名
driver.find_element(By.NAME,'username').send_keys('user')
# 输入正确密码
driver.find_element(By.NAME,'password').send_keys('12345678')
# 点击登录
driver.find_element(By.NAME,'login').click()
# 点击“项目”，进入’项目列表‘页面
driver.find_element(By.LINK_TEXT,'项目').click()
# 点击“新建项目”
driver.find_element(By.LINK_TEXT,'新建项目').click()
# 输入 项目名称
driver.find_element(By.ID,'project_name').send_keys(project_name)
# 点击’提交‘按钮
driver.find_element(By.NAME,'commit').click()
# 新建项目成功后的提示信息
ele2 = driver.find_element(By.ID,'flash_notice')
if ele2.text == '创建成功':
    print('pass')
else:
    print('fail')