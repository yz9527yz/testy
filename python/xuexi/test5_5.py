from selenium import webdriver
from time import sleep
import data
import base_page

URL1 = 'https://www.baidu.com/'
URL2 = 'https://www.ptpress.com.cn/'

driver = webdriver.Chrome()
driver.get(URL1)
winsize = driver.get_window_size()
print("获取当前窗口的大小")
print(winsize)
print("输出变量类型")
print(type(winsize))
sleep(2)
driver.set_window_size(550,802)
print("设置窗口大小")
pos =driver.get_window_position()
print("获取当前窗口位置")
print(pos)
sleep(2)
driver.set_window_position(500,300)
print("设置窗口位置")
print(driver.get_window_position())
print("再次输出窗口位置")
print(driver.title)
print("输出当前网页title")
print("获取当前网页的url")
print(driver.current_url)
sleep(2)
# 最大化
driver.maximize_window()
print("最大化")
sleep(2)
# 最小化
driver.minimize_window()
print("最小化")
sleep(2)
# 全屏显示
driver.fullscreen_window()
print("全屏")
sleep(2)
driver.quit()
print("退出")
