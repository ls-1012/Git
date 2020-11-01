#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# File:         ProjVar.py
# Author:       ls
# Date:         2020/10/20 14:42
#-------------------------------------------------------------------------------
import os
# 工程根目录
proj_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ini配置文件路径
PageElementLocator_file_path=os.path.join(proj_path,"Conf","PageElementLocator.ini")

# 邮箱登录信息
contacts_file_path=os.path.join(proj_path,"TestData","qq邮箱联系人.xlsx")



login_info_sheet="qq账号"
contacts_info_sheet="联系人"

# login_info_sheet.id=0
login_info_sheet_username=1
login_info_sheet_passwd=2
login_info_sheet_data_sheet=3
login_info_sheet_is_run=4
login_info_sheet_excute_result=5
login_info_sheet_excute_time=6


contacts_info_sheet_name=1
contacts_info_sheet_email=2
contacts_info_sheet_tel=3
contacts_info_sheet_country=4
contacts_info_sheet_province=5
contacts_info_sheet_city=6
contacts_info_sheet_street=7
contacts_info_sheet_birthday=8
contacts_info_sheet_qqacount=9
contacts_info_sheet_is_run=10
contacts_info_sheet_assert_content=11
contacts_info_sheet_excute_result=12
contacts_info_sheet_excute_time=13

# def get_id():
#     return id
#
# def get_username():
#     return username
#
# def get_passwd():
#     return passwd
#
# def get_data_sheet():
#     return data_sheet
#
# def get_is_run():
#     return is_run


def get_excute_result():
    return excute_result

def get_excute_time():
    return excute_time