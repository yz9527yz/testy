import unittest

class TestSecondPage(unittest.TestCase):
    """
    第一个测试集合
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_three(self):
        print('第3条测试用例')
        self.assertEqual(3,3)

    #@unittest.skip('skip info')
    def test_four(self):
        print('第4条测试用例')
        self.assertEqual(4,4)

if __name__ == '__main__':
    unittest.main()