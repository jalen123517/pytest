from selenium import webdriver
import unittest
from time import sleep
from test5 import Test
import HTMLTestRunner
import time
now=time.strftime("%Y%m%d%H%M%S",time.localtime())
reportFile = "./" + now + "_result.html"
fp=open(reportFile,'wb')
suite = unittest.TestSuite()
# suite.addTest(Test('test1'))
tests = unittest.defaultTestLoader.discover("./",pattern="test5.py")
suite.addTests(tests)
# runner = unittest.TextTestRunner(verbosity=2)
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'报告标题功 能测试报告', description=u'报告的说明与描述', tester=u'测试员姓名')
runner.run(suite)
fp.close()