from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("E:\备份\window_tools\chromedriver.exe")

driver.get("http://192.168.1.102:1080/webtours")
driver.switch_to.frame("body")
driver.switch_to.frame("navbar")
driver.find_element_by_name("username").send_keys("jalen11")
driver.find_element_by_name("password").send_keys("1")
driver.find_element_by_name("login").click()
# sleep(3)
driver.implicitly_wait(1)

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
driver.implicitly_wait(1)

driver.switch_to.default_content()
driver.switch_to.frame("body")
driver.switch_to.frame("info")
driver.find_element_by_xpath('//tbody/tr[2]/td[1]/input').click()
driver.find_element_by_name("reserveFlights").click()
driver.implicitly_wait(1)

driver.switch_to.default_content()
driver.switch_to.frame("body")
driver.switch_to.frame("info")
driver.find_element_by_name("firstName").send_keys("zhangsan")
sleep(2)
driver.quit()