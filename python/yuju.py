# name = 'stakl'
# print('ads ')
# print('hahahh{}'.format(name))
# print('ned')

#
# def power(a,b):
#     return a*b
#
# cheng = power(3,8)
# print(cheng)
#
# def power(x,n=2):
#
#     s = 1
#     while n > 0 :
#         n = n-1
#         s = s * x
#     return s
# if __name__ == '__main__':
#     print(power(2,4))

#
# def person(name,age,**kw):
#     print('name:',name,'age:',age,'other:',kw)
#
# print(person("asd",58,asfd='afff',sdsd='lgk'))

import  time
from datetime import datetime
#
# now = datetime.now()
# print(now)
# print('{:%Y-%m-%d %X]}'.format(now))
# print('hello {0:>{1}} '.format('Kevin',50))
# print('{!s}'.format('2'))
# #2
# print('{!r}'.format('2'))
# #‘2'

# class Student(object):
#     pass
#
# atorm = Student()
# s = Student()
# print(atorm)
# print(s)
# print(Student)
# atorm.name = 'dasda'
# print(atorm.name)
#
# class Student(object):
# #     def __int__(self,name,score):
# #         self.name = name
# #         self.score = score
# #
# #
# # storm = Student( "ddds" , 100)
# # print(storm.name)
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.Common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# URL1 = 'https://www.bilibili.com/'
# URL2 = 'https://www.ptpress.com.cn/'
# URL3 = 'https://www.baidu.com/'
#
# driver = webdriver.Chrome()
# driver.get(URL1)
# # driver.find_element_by_class_name('nav-search-input').send_keys('storm')
# # driver.find_element_by_partial_link_text('番').click()
# # #driver.find_element_by_class_name('番剧').click()
# # driver.find_element_by_css_selector('#nav-searchform > div.nav-search-btn > svg').click()
# # driver.find_element(By.CLASS_NAME,'nav-search-input').send_keys('storm')
# driver.find_element(By.CLASS_NAME,'nav-search-input').send_keys('马超')
# driver.find_element(By.CLASS_NAME,'nav-search-btn').click()
#
# su = WebDriverWait(driver,10).until(EC.presence_of_element_located(((By.LINK_TEXT),"番剧")))
# result = su.text
# print(result)
#
# # sleep(2)
# import os
# print(os.getcwd())
# print(os.sep)
# # driver.quit()
# 张三体重 = '60KG'
# print(张三体重)

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time
from selenium import webdriver
from redmine.PageObjects.redmine_locators import *
from selenium.webdriver.common.by import By
from redmine.Scenario.redmine_login import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# driver = webdriver.Chrome()
# driver.get("http://localhost/redmine/login")

# driver.find_element(*RegisterPageLocators.RegisterUserName).send_keys("user112")
# driver.find_element(*RegisterPageLocators.RegisterPassWord).send_keys("12345678")
# driver.find_element(*RegisterPageLocators.ConfirmPassWord).send_keys("12345678")
# driver.find_element(*RegisterPageLocators.FirstName).send_keys("王")
# driver.find_element(*RegisterPageLocators.LasttName).send_keys("小二")
# driver.find_element(*RegisterPageLocators.UserMail).send_keys("1235411@163.com")
# driver.find_element(*RegisterPageLocators.Submit).click()
# time.sleep(3)
# eles = driver.find_elements(By.XPATH,"//*[@id='errorExplanation']/ul/li")
# print(type(eles))
# print(eles)
# for ele in eles :
#     print(ele.text)
#
# # ele2 =//*[@id="flash_error"]
# ele2 = driver.find_element(By.XPATH,'//*[@id="flash_error"]')
# print(ele2.text)


# 注册成功：您的帐号已被成功创建，正在等待管理员的审核。
# 注册失败：
#
# 邮件地址 是无效的
# 邮件地址 不能为空字符
# 邮件地址 已经被使用
#
# 密码 过短（最短为 8 个字符）
# 密码 与确认值不匹配
#
# 登录名 不能为空字符
# 登录名 已经被使用
#
# 名字 不能为空字符
# 姓氏 不能为空字符
#
#
# eles = ['snik','水泥',1]
# type(eles)
# print(eles.text)
#
# driver.find_element(By.ID,"username").send_keys('user')
# driver.find_element(By.ID, "password").send_keys('12345678')
# driver.find_element(By.ID, "login-submit").click()
# ele = driver.find_element(By.LINK_TEXT,'项目')
# print(type(ele))
# print(ele.text)

# try:
#     ele2 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.LINK_TEXT,'项目')))
#     time.sleep(2)
#     print(ele2)
#     print(type(ele2))
#     ele2.click()
# except Exception as e:
#     raise e
# finally:
#     time.sleep(5)
import os
t = os.gtecwd()