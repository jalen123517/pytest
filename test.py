from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
import pandas

driver = webdriver.Chrome("E:\备份\window_tools\chromedriver.exe")
fp = open("1.txt",mode="r")
data = pandas.read_excel(r'c:\Users\jalen\Desktop\cases.xls',dtype={"用户名":"str","密码":"str","预期结果":"str"})
datalist = data.values.tolist()
print(datalist)

for i in fp:
    username = i.split("\t")[0]
    password = i.split("\t")[1].strip("\n")

    driver.get("http://192.168.1.102:1080/webtours/")
    driver.switch_to.frame("body")
    driver.switch_to.frame("info")
    sign_up = driver.find_element_by_link_text("sign up now")
    # driver.switch_to.active_element(sign_up)
    sign_up.click()


    user_name = driver.find_element_by_name("username")
    user_name.send_keys(username)

    passwd = driver.find_element_by_name("password")
    passwd.send_keys(password)

    passwordConfirm = driver.find_element_by_name("passwordConfirm")
    passwordConfirm.send_keys(password)

    register = driver.find_element_by_name("register")
    register.click()

    driver.switch_to.default_content()
    driver.switch_to.frame("body")
    driver.switch_to.frame("info")
    # print(driver.find_element_by_tag_name("body").text)
    str_var = driver.find_element_by_tag_name("body").text
    if "username is taken" in str_var:
        print("%s该账号已经注册过" % username)
    else:
        print("%s该账号没有被注册过" % username)

    sleep(3)

    # driver.quit()
