import pytest

@pytest.fixture()
def login():
    print("输入账号密码，正在进行登陆操作")

@pytest.fixture()
def logout():
    print("正在进行登出操作")