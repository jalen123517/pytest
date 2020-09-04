import pytest

@pytest.fixture(scope="module")
def baidu():
    print("打开百度首页")


def test_func1(baidu):
    print("执行测试用例test_func1")

def test_func2(baidu):
    print("执行测试用例test_func2")

if __name__ == "__main__":
    pytest.main(["-s","test_f1.py"])