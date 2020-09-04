from selenium import webdriver
import unittest
from time import sleep
data_list = [[1,2],[2,4]]
import parameterized
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    @classmethod
    def tearDownClass(cls):
        pass

    @parameterized.parameterized.expand(data_list)
    def test1(self,a,b):
        '''a和b比较大小'''
        assert a > 1,"判断错误，a小于b"

    def test2(self):
        '''a和c比较大小'''
        a = 6
        c = 7
        assert a > 1,"判断错误，a小于b"

    def test3(self):
        '''a和d比较大小'''
        a = 6
        d = 7
        assert a > 1,"判断错误，a小于b"

    def test4(self):
        '''a和e比较大小'''
        a = 6
        e = 7
        assert a > e,"判断错误，a小于b"

if __name__ == "__main__":
    unittest.main(verbosity=2)
