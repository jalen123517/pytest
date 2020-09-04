import pytest

class TestCase():

    def setup(self):
        print("setup:每个用例执行之前都会执行的")

    def teardown(self):
        print("teardown:每个用例执行完都会执行的")

    def teardown_class(self):
        print("teardown_class:所有测试用例执行完，才会执行一次")
    def setup_class(self):
        print("setup_class:所有用例执行之前执行一次")

    def test1_func(self):
        print("test1_func:开始执行测试用例test1_func")
        assert 1

    def test2_func(self):
        print("test2_func:开始执行测试用例test2_func")
        assert 2

if __name__ == "__main__":
    pytest.main(["-s","test_9.py"])