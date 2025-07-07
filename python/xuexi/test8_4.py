from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')

try:
    # 判断title
    ele = WebDriverWait(driver,10).until(EC.title_is("百度一下，你就知道"),message='你是个傻逼吧')
    # 输出返回值类型
    print(type(ele))
    # 输出返回值
    print(ele)
    # 如果匹配，就执行该语句
    driver.find_element(By.LINK_TEXT,'地图').click()
    sleep(2)
except Exception as e:
    # 有异常跑出
    raise e

finally:
    # 最后退出driver
    driver.quit()