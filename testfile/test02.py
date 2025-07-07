from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import  webDriverwait

URL1 = 'https://www.baidu.com/'
URL2 = 'https://www.ptpress.com.cn/'

driver = webdriver.Chrome()
print("启动浏览器驱动")
driver.get(URL1)
print("打开百度")
sleep(2)
driver.get(URL2)
print("打开人邮局出版社")
sleep(2)
driver.back()
print("退后一层")
sleep(2)
driver.forward()
print("前进一层")
sleep(2)
driver.quit()
print("关闭浏览器驱动")
driver.page_source