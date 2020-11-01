#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# File:         AddressPage.py
# Author:       ls
# Date:         2020/10/21 09:28
#-------------------------------------------------------------------------------
from Conf.ProjVar import *
from Util.ParseConfig import *
from Util.ObjectMap import find_element,find_elements
from PageObject.HomePage import *
from PageObject.LoginPage import *
import time
from datetime import datetime

class addressPage():
    def __init__(self,driver):
        self.driver=driver

    def get_iframe(self):
        link = read_ini_file_option(PageElementLocator_file_path, "qqmail_contactsPage", "contactsPage.loginFrame")
        element = find_element(self.driver, link.split(">")[0], link.split(">")[1])

        return element

    def switch_to_iframe(self):
        frame = self.get_iframe()
        self.driver.switch_to.frame(frame)

    def get_create_button(self):
        button = read_ini_file_option(PageElementLocator_file_path, "qqmail_contactsPage", "contactsPage.addContactButton")
        element = find_element(self.driver, button.split(">")[0], button.split(">")[1])
        return element

    def click_address_button(self):
        self.get_create_button().click()

    def get_name(self):
        input = read_ini_file_option(PageElementLocator_file_path, "qqmail_contactsPage", "contactsPage.name")
        element = find_element(self.driver, input.split(">")[0], input.split(">")[1])
        return element

    def input_name(self,name):
        if name is None:
            name=""
        self.get_name().send_keys(name)

    def get_email(self):
        input = read_ini_file_option(PageElementLocator_file_path, "qqmail_contactsPage", "contactsPage.email")
        element = find_element(self.driver, input.split(">")[0], input.split(">")[1])
        return element

    def set_email(self,email):
        if email is None:
            email=""
        self.get_email().send_keys(email)

    def get_tel(self):
        input = read_ini_file_option(PageElementLocator_file_path, "qqmail_contactsPage", "contactsPage.tel")
        element = find_element(self.driver, input.split(">")[0], input.split(">")[1])
        return element

    def set_tel(self,tel):
        if tel is None:
            tel=""
        self.get_tel().send_keys(tel)

    def get_country(self):
        input = read_ini_file_option(PageElementLocator_file_path, "qqmail_contactsPage", "contactsPage.country")
        element = find_element(self.driver, input.split(">")[0], input.split(">")[1])
        return element

    def set_country(self,country):
        if country is None:
            country=""
        self.get_country().send_keys(country)

    def get_province(self):
        input = read_ini_file_option(PageElementLocator_file_path, "qqmail_contactsPage", "contactsPage.province")
        element = find_element(self.driver, input.split(">")[0], input.split(">")[1])
        return element

    def set_province(self,province):
        if province is None:
            province = ""
        self.get_province().send_keys(province)

    def get_city(self):
        input = read_ini_file_option(PageElementLocator_file_path, "qqmail_contactsPage", "contactsPage.city")
        element = find_element(self.driver, input.split(">")[0], input.split(">")[1])
        return element

    def set_city(self,city):
        if city is None:
            city = ""
        self.get_city().send_keys(city)
        time.sleep(1)

    def get_streat(self):
        input = read_ini_file_option(PageElementLocator_file_path, "qqmail_contactsPage", "contactsPage.street")
        element = find_element(self.driver, input.split(">")[0], input.split(">")[1])
        return element

    def set_streat(self,streat):
        if streat is None:
            streat = ""
        self.get_streat().send_keys(streat)

    def get_birthday(self):
        input = read_ini_file_option(PageElementLocator_file_path, "qqmail_contactsPage", "contactsPage.birthday")
        element = find_element(self.driver, input.split(">")[0], input.split(">")[1])
        return element

    def set_birthday(self,birthday):
        if birthday is None:
            birthday = ""
        if isinstance(birthday,datetime):
            birthday=str(birthday)

        self.get_birthday().send_keys(birthday)

    def get_qqacount(self):
        input = read_ini_file_option(PageElementLocator_file_path, "qqmail_contactsPage", "contactsPage.qq_acount")
        element = find_element(self.driver, input.split(">")[0], input.split(">")[1])
        return element

    def set_qqacount(self,qqacount):
        if qqacount is None:
            qqacount = ""
        self.get_qqacount().send_keys(qqacount)

    def get_saveButton(self):
        button = read_ini_file_option(PageElementLocator_file_path, "qqmail_contactsPage", "contactsPage.saveButton")
        element = find_element(self.driver, button.split(">")[0], button.split(">")[1])
        return element

    def click_saveButton(self):
        self.get_saveButton().click()
        self.driver.switch_to.default_content()

    def get_cancelButton(self):
        button = read_ini_file_option(PageElementLocator_file_path, "qqmail_contactsPage", "contactsPage.cancelButton")
        element = find_element(self.driver, button.split(">")[0], button.split(">")[1])
        return element

    def click_cancelButton(self):
        self.get_cancelButton().click()
        self.driver.switch_to.default_content()

    def get_msg(self):
        span = read_ini_file_option(PageElementLocator_file_path, "qqmail_contactsPage", "contactsPage.msg")
        element = find_element(self.driver, span.split(">")[0], span.split(">")[1])

        return element.text


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

    hp = homePage(driver)
    hp.click_address_link()
    print("home success")


    ap=addressPage(driver)
    time.sleep(1)
    ap.switch_to_iframe()
    time.sleep(1)
    ap.click_address_button()
    ap.input_name("ssss")
    ap.set_email("111@qq.com")
    ap.set_tel("1111111")
    ap.set_country("中国")
    ap.set_province("山西")
    ap.set_city("襄垣")
    ap.set_streat("西关村一号")
    ap.set_birthday("2020-10-21")
    ap.set_qqacount("1234567")
    ap.click_saveButton()
    print("address success")
    driver.switch_to.default_content()
    print(ap.get_msg())

    # driver.quit()

