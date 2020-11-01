#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# File:         Action.py
# Author:       ls
# Date:         2020/10/21 13:04
# -------------------------------------------------------------------------------
import time
from PageObject.HomePage import *
from PageObject.LoginPage import *
from PageObject.AddressPage import *
from selenium import webdriver


def login(user, passwd):
    driver = webdriver.Chrome(executable_path="d:/chromedriver")
    driver.get("http://mail.qq.com")
    lp = loginPage(driver)
    lp.switch_to_iframe()
    lp.click_login_link()
    lp.set_username(user)
    lp.set_passwd(passwd)
    lp.click_login_button()
    print("login success")
    return driver


def addContacts(driver, name=None, email=None, tel=None, country=None, province=None, city=None, street=None,
                birthday=None, qqacount=None, is_run=None, assertcount=None):
    hp = homePage(driver)
    hp.click_address_link()
    print("home success")

    ap = addressPage(driver)
    time.sleep(1)
    ap.switch_to_iframe()
    time.sleep(1)
    ap.click_address_button()
    ap.input_name(name)
    ap.set_email(email)
    ap.set_tel(tel)
    ap.set_country(country)
    ap.set_province(province)
    ap.set_city(city)
    ap.set_streat(street)
    ap.set_birthday(birthday)
    ap.set_qqacount(qqacount)
    ap.click_saveButton()
    print("address success")
    time.sleep(3)
    text = ap.get_msg()
    if assertcount in text:
        return True
    else:
        ap.switch_to_iframe()
        ap.click_cancelButton()
        return


if __name__ == "__main__":
    driver = login("573369709", "myself1314")
    print(addContacts(driver, "芦女士", "18518183300@qq.com", "18518183300", "中国", "北京", "昌平", "龙泽苑街道", "2010-10-10",
                      "55789909"))
    print(addContacts(driver, "uuuu"))
