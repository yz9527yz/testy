import unittest
import HTMLTestRunner
import time,os

if __name__ == '__main__':
    # 查找当前目录的测试用例文件
    testSuite = unittest.TestLoader().discover('.')
    # 定义一个文件名，文件名以粘液时分秒结尾，方便查找
    filename = os.getcwd() + os.sep + "unittest2_{}.html".format(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())))
    # 以 with open 的方式打开文件
    with open(filename,'wb') as f:
        #通过HTMLTestRunner来执行测试用例，并生成报告
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, verbosity=2,title='Redmine测试报告', description='unittest线性测试报告')
        runner.run(testSuite)