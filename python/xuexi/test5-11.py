from selenium import  webdriver
from time import sleep

URL1 = 'https://www.baidu.com/'
URL2 = 'https://www.ptpress.com.cn/'

driver = webdriver.Chrome()
driver.get('http://sahitest.com/demo/index.htm')
# 查看当前窗口句柄
first_handle = driver.current_window_handle
print(driver.current_window_handle)
print(first_handle)
# 打开新window
driver.find_element_by_link_text('Window Open Test').click()
# 查看所有窗口句柄
all_handle = driver.window_handles
print(driver.window_handles)
print(all_handle)
# 切换窗口
driver.switch_to.window(all_handle[1])
sleep(2)
# 切换到第一个frame
driver.switch_to.frame(1)
sleep(2)
driver.find_element_by_link_text('Link Test').click()
sleep(2)

driver.switch_to.new_window("tab")
driver.switch_to.new_window('window')
# driver.close()
# print(driver.window_handles)
# sleep(2)
driver.quit()
