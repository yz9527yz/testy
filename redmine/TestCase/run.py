import unittest
import HTMLTestRunner
import time, os
import logging
from redmine.Data.var import *
from redmine.Common.sendEmail import SendSmptEmail
from redmine.Common.lastest_report import latest_report
from redmine.TestCase.test_002_login import *
from redmine.Common.log import logger
run_log = logging.getLogger('redmine')


if __name__ == '__main__':

    # 查找当前目录的测试用例文件

    logging.info('test1')
    print("print1")
    # testSuite = unittest.TestLoader().discover('.')
    testSuite = unittest.TestSuite()
    testSuite.addTest(TestLogin("test_login"))

    run_log.info('test2')
    print("print2")
    # 定义一个文件名，文件名以粘液时分秒结尾，方便查找
    #run_log.info('test3')
    print("print3")
    filename = report_url + os.sep + "Redmine_{}.html".format(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
    # 以 with open 的方式打开文件
    #run_log.info('test4')
    print("print4")
    with open(filename, 'wb') as f:
        # 通过HTMLTestRunner来执行测试用例，并生成报告
        #run_log.info('test5')
        print("print5")
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, verbosity=2,title='Redmine测试报告', description='unittest线性测试报告')
        runner.run(testSuite)
        #run_log.info('test6')
        print("print6")
        #logger.info('执行测试用例集合，生成html测试报告')
        #run_log.info('执行测试用例集合，生成html测试报告')
        f.close()
    SendSmptEmail.send_email(latest_report(report_url))
    
    #run_log.info('邮件提交测试报告')
    #logger.info('邮件提交测试报告')
    #run_log.info('test7')
    print("print7")