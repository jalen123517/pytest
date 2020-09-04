import pytest
#
# @pytest.fixture()
# def open():
#     print("打开百度首页")
#
# def test_func1():
#     print("正在执行测试用例test_func1")
#
# def test_func2(open):
#     print("正在执行测试用例test_func2")




# @pytest.fixture(scope="module")
# def open():
#     print("打开百度首页")
#
#     yield
#     print("所有用例执行完毕")
#
# def test_func1(open):
#     print("正在执行测试用例test_func1")
#
# def test_func2(open):
#     print("正在执行测试test_func2")



# @pytest.fixture(scope="module")
# def open():
#     print("打开百度首页")
#
#     yield
#     print("所有用例执行完毕")
#
# def test_func1(open):
#     raise NameError
#     print("正在执行测试用例test_func1")
#
# def test_func2(open):
#     print("正在执行测试test_func2")


# @pytest.fixture(scope="module")
# def open():
#     # raise NameError
#     print("打开百度首页")
#
#     yield
#     print("所有用例执行完毕")
#
# def test_func1(open):
#     print("正在执行测试用例test_func1")
#
# def test_func2(open):
#     print("正在执行测试test_func2")



#参数化
# @pytest.mark.parametrize("a,b",[(5,6),(7,7),(8,9)])
# def test_func1(test_input,test_expect):
#     assert test_input == test_expect,"断言错误"

# import pytest
# @pytest.mark.parametrize("test_input,expected",
#                          [ ("3+5", 8),
#                            ("2+4", 6),
#                            ("6 * 9", 42),
#                          ])
# def test_eval(test_input, expected):
#     assert eval(test_input) == expected
#
# @pytest.mark.parametrize("test_input,expected", [
#                         ("3+5", 8),
#                         ("2+4", 6),
#                         pytest.param("6 * 9", 42, marks=pytest.mark.xfail),
#                         ])
# def test_eval(test_input, expected):
#     print("-------开始用例------")
#     assert eval(test_input) == expected


import pytest
@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_foo(x, y):
    print("测试数据组合：x->%s, y->%s" % (x, y))





if __name__ == "__main__":
    pytest.main(["-s","test_f2.py"])