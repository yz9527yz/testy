from selenium import  webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(20)

driver.get('http://localhost/redmine/login')

# 用例一：错误密码登录失败

# 输入正确用户名
driver.find_element(By.NAME,'username').send_keys('user')
# 输入错误密码
driver.find_element(By.NAME,'password').send_keys('error')
# 点击登录
driver.find_element(By.NAME,'login').click()
# 登录失败后的提示信息
ele = driver.find_element(By.ID,'flash_error')
# 断言
if ele.text == '无效的用户名或密码':
    print('pass')
else:
    print('fail')

# 用例二：正确密码登录成功

# 输入正确用户名
driver.find_element(By.NAME,'username').send_keys('user')
# 输入正确密码
driver.find_element(By.NAME,'password').send_keys('12345678')
# 点击登录
driver.find_element(By.NAME,'login').click()
# 登录后显示的用户名
name = driver.find_element(By.LINK_TEXT,'user')
# 断言
if name.text == 'user':
    print('pass')
else:
    print('fail')

driver.quit()