#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# File:         HomePage.py
# Author:       ls
# Date:         2020/10/20 18:18
#-------------------------------------------------------------------------------
from Conf.ProjVar import *
from Util.ParseConfig import *
from Util.ObjectMap import find_element,find_elements
# from PageObject.LoginPage import *
import  time


class homePage():
    def __init__(self,driver):
        self.driver=driver

    def get_address_link(self):
        link=read_ini_file_option(PageElementLocator_file_path,"qqmail_homePage","homePage.addressLink")
        element=find_element(self.driver,link.split(">")[0],link.split(">")[1])
        return element

    def click_address_link(self):
        self.get_address_link().click()
        time.sleep(3)


if __name__=="__main__":
    driver = webdriver.Chrome(executable_path="d:/chromedriver")
    driver.get("http://mail.qq.com")
    lp = loginPage(driver)
    lp.switch_to_iframe()
    lp.click_login_link()
    lp.set_username("573369709")
    lp.set_passwd("myself1314")
    lp.click_login_button()
    print("login success")

    hp=homePage(driver)
    hp.click_address_link()
    print("home success")