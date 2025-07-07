from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
try:
    # 检测元素是否找到
    ele = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,'地图')))
    # 返回列表中包含的元素数量
    #print(len(ele))
    # 返回值的类别
    print(type(ele))
    # 返回值
    print(ele.text)

except Exception as e:
    # 有异常抛出
    raise e
finally:
    driver.quit()