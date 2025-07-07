from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
URL1 = 'https://www.baidu.com/'
#URL1 = 'https://www.bilibili.com/'
URL2 = 'https://www.ptpress.com.cn/'

driver = webdriver.Chrome()
driver.get(URL1)
# ele = driver.find_element_by_id('kw')
# print(ele)
# print(type(ele))
# eles = driver.find_elements_by_id('kw')
# print(eles)
# print(type(eles))

# 使用 id 来定位
#driver.find_element_by_id('kw').send_keys('storm')
driver.find_element(By.ID,'kw').send_keys('storm')
sleep(2)
driver.find_element(By.ID,'kw').send_keys(Keys.CONTROL,'a')
driver.find_element(By.ID,'kw').send_keys(Keys.CONTROL,'c')
driver.find_element(By.ID,'kw').clear()
sleep(2)
driver.find_element(By.ID,'kw').send_keys(Keys.CONTROL,'v')
# 使用 name 来定位
#driver.find_element_by_name('wd').send_keys('storm')



sleep(2)
driver.quit()

