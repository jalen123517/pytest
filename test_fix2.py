import pytest



def test_func3():
    print("正在执行测试用例：test_func3")
    assert 1

def test_func4(logout):
    print("正在执行测试用例：test_func4")
    assert 0


if __name__ == "__main__":
    pytest.main(["-s","test_fix2.py"])