#coding:utf-8
from selenium import webdriver
import os
from time import sleep
#driver = webdriver.Chrome()
driver=webdriver.Chrome("D:\\Google\\Chrome\\Application\\chromedriver.exe")
driver.get("https://github.com/login")
driver.implicitly_wait(10)
#driver.find_element_by_id("kw").send_keys("python")
# 输入账号
driver.find_element_by_id("login_field").send_keys("qunfm")
# 输入密码
sleep(3)
driver.find_element_by_id("password").send_keys("lixue131")
sleep(3)
driver.find_element_by_name("commit").click()

#driver.quit()
