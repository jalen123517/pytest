import pytest

def func(a,b):
    return a+b

def test_func():
    u'''test fun测试'''
    assert func(2,3) == 5,"断言错误"

def test2_func():
    assert func(3,3) == 6,"断言错误"


#创建的.py 文件， 一定要是以 test_开头的.py文件， 这样的话，在终端同级目录下，输入pytest命令即可执行

class TestClass():
    def test_one(self):
        assert 1
    def test_two(self):
        assert 2

