import unittest
class TestFirstPage(unittest.TestCase):
    """
    第一个测试集合
    """
    a = 3
    def setUp(self):
        pass

    def tearDown(self):
        pass
    #@unittest.skipIf('skip info')
    @unittest.skipIf(a ==5,'info')
    def test_one(self):
        print('第1条测试用例')
        self.assertEqual(1,1)

    def test_tow(self):
        print('第2条测试用例')
        self.assertEqual(2,2)

if __name__ == '__main__':
    unittest.main()