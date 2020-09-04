import pytest

def setup_module():
    print("setup_module：执行一次的用例")

def teardown_module():
    print("teardown_module:只执行一次的用例")

def setup_function():
    print("setup_function：开始执行用例")


def teardown_function():
    print("teardown_function：最后执行的用例")

def test_1():
    print("test_1：开始执行test_1用例")
    x = "this"
    assert "h" in x,"断言错误，test_1函数"

def test_2():
    print("test_2:开始执行test_2用例")
    x = "this"
    assert "a" in x ,"断言错误,test_2函数"

if __name__ == "__main__":
    pytest.main(["-s","test_8.py"])
