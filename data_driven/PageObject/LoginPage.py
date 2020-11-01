#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# File:         LoginPage.py
# Author:       ls
# Date:         2020/10/20 15:54
#-------------------------------------------------------------------------------
import time
import traceback

from selenium import webdriver
from selenium.common.exceptions import InvalidArgumentException, NoSuchElementException, ElementNotInteractableException

from Conf.ProjVar import *
from Util.ParseConfig import *
from Util.ObjectMap import find_element,find_elements


class loginPage():
    def __init__(self,driver):
        self.driver=driver

    def get_login_link(self):
        # 返回定位元素表达式
        link=read_ini_file_option(PageElementLocator_file_path,"qqmail_loginPage","loginPage.loginAccountButton")
        element=find_element(self.driver,link.split(">")[0],link.split(">")[1])
        return element

    def click_login_link(self):
        try:
            self.get_login_link().click()
        except InvalidArgumentException:
            pass
        except NoSuchElementException:
            traceback.print_exc()
        except ElementNotInteractableException:
            traceback.print_exc()
        except:
            traceback.print_exc()

    def get_iframe(self):
        link=read_ini_file_option(PageElementLocator_file_path,"qqmail_loginPage","loginPage.loginFrame")
        element = find_element(self.driver, link.split(">")[0], link.split(">")[1])
        return element
    def switch_to_iframe(self):
        frame=self.get_iframe()
        self.driver.switch_to.frame(frame)

    def get_username(self):
        input = read_ini_file_option(PageElementLocator_file_path, "qqmail_loginPage", "loginPage.user")
        # print("username: ",input)
        element = find_element(self.driver, input.split(">")[0], input.split(">")[1])
        return element

    def set_username(self,username):
        input=self.get_username()
        input.send_keys(username)


    def get_passwd(self):
        input = read_ini_file_option(PageElementLocator_file_path, "qqmail_loginPage", "loginPage.passwd")
        element = find_element(self.driver, input.split(">")[0], input.split(">")[1])
        return element

    def set_passwd(self,passwd):
        self.get_passwd().send_keys(passwd)


    def get_login_button(self):
        link = read_ini_file_option(PageElementLocator_file_path, "qqmail_loginPage", "loginPage.loginButton")
        element = find_element(self.driver, link.split(">")[0], link.split(">")[1])
        return element

    def click_login_button(self):
        self.get_login_button().click()
        time.sleep(4)

if __name__=="__main__":
    driver=webdriver.Chrome(executable_path="d:/chromedriver")
    driver.get("http://mail.qq.com")
    lp=loginPage(driver)
    lp.switch_to_iframe()
    lp.click_login_link()
    lp.set_username("573369709")
    lp.set_passwd("myself1314")
    lp.click_login_button()
    print("success")
