#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# File:         CaptureScreen.py
# Author:       ls
# Date:         2020/10/22 14:53
#-------------------------------------------------------------------------------
import time
from Util.Dir import make_time_dir
import os
from Util.DateAndTime import *


def captureScreen(driver):
    try:

        png_path=os.path.join(make_time_dir(),TimeUtil().get_chinesedatetime()+".png")
        print(png_path)
        driver.get_screenshot_as_file(png_path)
    except IOError as e:
        print(e)



if __name__=="__main__":
    from selenium import webdriver
    driver=webdriver.Chrome(executable_path="d:/chromedriver")
    driver .get("http://www.baidu.com")
    captureScreen(driver)