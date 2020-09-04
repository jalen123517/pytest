import pytest

#1.函数

# def test_func1():
#     print("开始执行测试用例test_func1")
#
# def test_func2():
#     print("开始执行测试用例test_func2")


#增加setup和teardown


# def test_func1():
#     w
#     raise NameError
#     print("开始执行测试用例test_func1")
# def test_func2():
#     print("开始执行测试用例test_func2")
#
# def teardown_function():
#     print("开始执行测试用例teardown_function")
# def setup_function():
#     print("开始执行测试用例setup_function")
#
# def setup_module():
#     print("开始执行测试用例setup_module")
# def teardown_module():
#     print("开始执行测试用例teardown_module")
# ##出现一个测试用例错误，不会影响后面的用例执行


#增加类的
# import pytest
# # 类和方法
# class Test1():    #一定是Test开头的
#
#     def setup(self):
#         print("setup: 每个用例开始前执行")
#
#     def teardown(self):
#         print("teardown: 每个用例结束后执行")
#
#     def setup_class(self):
#         print("setup_class：所有用例执行之前")
#
#     def teardown_class(self):
#         print("teardown_class：所有用例结束后执行")
#
#     def setup_method(self):
#         print("setup_method:  每个用例开始前执行")
#
#     def teardown_method(self):
#         print("teardown_method:  每个用例结束后执行")
#
#     def test_one(self):
#         print("正在执行----test_one")
#         x = "this"
#         assert 'h' in x
#
#     def test_two(self):
#         print("正在执行----test_two")
#         x = "hello"
#         assert hasattr(x, 'check')
#
#     def test_three(self):
#         print("正在执行----test_three")
#         a = "hello"
#         b = "hello world"
#         assert a in b



#fixture
# @pytest.fixture()
# def open():
#     print("打开百度首页")
# def test_func1(login):
#     print("正在执行测试用例test_func1")
#
# def test_func2(open):
#     print("正在执行测试用例test_func2")


##增加yield的使用
#fixture
# @pytest.fixture(scope="module")
# def open():
#     print("打开百度首页")
#
#     yield
#     print("最后执行的地方")
# def test_func1(open):
#     print("正在执行测试用例test_func1")
#
# def test_func2(open):
#     print("正在执行测试用例test_func2")


#参数化
# @pytest.mark.parametrize("a,b",[(1,2),(3,4)])
# def test_fucn1(a,b):
#     print("正在打印%s" % a)
#     assert a == 1


@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_foo(x, y):
    print("测试数据组合：x->%s, y->%s" % (x, y))




if __name__ == "__main__":

    pytest.main(["-s","test_zongjie.py"])