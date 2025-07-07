import time

from selenium import webdriver

import unittest





class forTestTest(unittest.TestCase):

    def setUp(self) :
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        self.driver.maximize_window()
        self.driver.fullscreen_window()

    def tearDown(self):
        time.sleep(1)
        self.driver.quit()

    def test_1(self):

        self.driver.find_element_by_id('kw').send_keys('马超')
        time.sleep(1)
        self.driver.find_element_by_id('su').click()

    # def test_2(self):
    #
    #     self.driver.find_element_by_id('kw').send_keys('赵云')
    #     time.sleep(1)
    #     self.driver.find_element_by_id('su').click()
    #
    # def test_3(self):
    #
    #     self.driver.find_element_by_id('kw').send_keys('张飞')
    #     time.sleep(1)
    #     self.driver.find_element_by_id('su').click()
    #
    # def test_4(self):
    #
    #     self.driver.find_element_by_id('kw').send_keys('关羽')
    #     time.sleep(1)
    #     self.driver.find_element_by_id('su').click()
    #
    # def test_5(self):
    #
    #     self.driver.find_element_by_id('kw').send_keys('黄忠')
    #     time.sleep(1)
    #     self.driver.find_element_by_id('su').click()

if __name__ == '__main__':
    unittest.main()
