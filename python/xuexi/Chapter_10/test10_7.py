import unittest
from python.xuexi.Chapter_10 import test10_5

if __name__ == '__main__':
    # 新建测试集合
    suite = unittest.TestSuite()
    suite.addTest(test10_5.TestFirstPage('test_one'))
    suite.addTest(test10_5.TestSecondPage('test_four'))
    # 执行测试集合
    unittest.TextTestRunner().run(suite)