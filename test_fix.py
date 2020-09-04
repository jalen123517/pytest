import pytest

# @pytest.fixture()
# def login():
#     print("输入账号密码，正在登陆中")
#
# @pytest.fixture()
# def logout():
#     print("正在登出")

def test_func1(login):
    print("正在执行用例:test_func1")

def test_func2(logout):
    print("正在执行用例：test_func2")


if __name__ == "__main__":
    pytest.main(["-s","test_fix.py"])