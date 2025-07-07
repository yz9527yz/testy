
import unittest
from python.xuexi.Chapter_10 import test10_5

if __name__ == '__main__':
    # 新建测试集合
    testSuite = unittest.TestLoader().discover('.')
    unittest.TextTestRunner(verbosity=2).run(testSuite)