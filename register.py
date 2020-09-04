from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
import unittest
drvier = None
class Reg(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global driver
        driver = webdriver.Chrome("E:\备份\window_tools\chromedriver.exe")
        # driver
        print("starting")

    @classmethod
    def tearDownClass(cls):
        driver.quit()
        print("done")

    # def setUp(self):
    #     print(1)
    # def tearDown(self):
    #     print(2)
    def test1_login(self):
        u'''登陆'''
        driver.get("http://192.168.1.102:1080/webtours")
        driver.switch_to.default_content()
        driver.switch_to.frame("body")
        driver.switch_to.frame("navbar")
        driver.find_element_by_name("username").send_keys("jalen11")
        driver.find_element_by_name("password").send_keys("1")
        driver.find_element_by_name("login").click()
        # sleep(3)
        driver.implicitly_wait(1)
        sleep(1)
        driver.switch_to.frame("body")
        driver.switch_to.frame("info")
        result = driver.find_element_by_tag_name("body").text
        assert "yes" in "yes111"
    def test2_dingpiao(self):
        u'''订票'''
        driver.switch_to.default_content()
        driver.switch_to.frame("body")
        driver.switch_to.frame("navbar")
        driver.find_element_by_xpath('//img[@src="/WebTours/images/flights.gif"]').click()
        # sleep(2)
        driver.implicitly_wait(1)
        driver.switch_to.default_content()
        driver.switch_to.frame("body")
        driver.switch_to.frame("info")

        depart = driver.find_element_by_name("depart")
        # print(depart.text)
        Select(depart).select_by_index(0)
        arrive = driver.find_element_by_name("arrive")
        Select(arrive).select_by_index(2)
        driver.find_element_by_name("findFlights").click()
        sleep(2)
        driver.switch_to.default_content()
        driver.switch_to.frame("body")
        driver.switch_to.frame("info")
        driver.find_element_by_name("reserveFlights").click()
        sleep(1)
        driver.switch_to.default_content()
        driver.switch_to.frame("body")
        driver.switch_to.frame("info")
        driver.find_element_by_name("buyFlights").click()
        sleep(1)
        driver.switch_to.default_content()
        driver.switch_to.frame("body")
        driver.switch_to.frame("info")
        driver.find_element_by_name("Book Another").click()
        sleep(5)
        assert "yes" in "yes111"
    def test3_logout(self):
        u'''推出'''
        driver.switch_to.default_content()
        driver.switch_to.frame("body")
        driver.switch_to.frame("navbar")
        driver.find_element_by_xpath('//img[@src="/WebTours/images/signoff.gif"]').click()
        assert "yes" in "yes11"

if __name__ ==  "__main__":
    unittest.main(verbosity=2)
