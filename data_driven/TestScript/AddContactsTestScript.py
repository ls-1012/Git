#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# File:         AddContactsTestScript.py
# Author:       ls
# Date:         2020/10/21 14:29
# -------------------------------------------------------------------------------

from Conf.ProjVar import *
# from Conf.ProjVar import contacts_file_path,login_info_sheet
from Util.operator_Excel import OPExcel
from Action.Action import addContacts, login
from Util.DateAndTime import TimeUtil
from Util.CaptureScreen import *

opExcel = OPExcel(contacts_file_path)


def get_User_info(sheetname):
    # opExcel=get_ExcelInstance(contacts_file_path)
    global opExcel
    opExcel.set_sheet_by_sheetname(sheetname)
    loginUserInfo = opExcel.getExcelContent()
    return loginUserInfo


def run():
    loginUserInfo = get_User_info(login_info_sheet)
    for line_idx in range(1, len(loginUserInfo)):
        flag = True
        if loginUserInfo[line_idx][login_info_sheet_is_run].lower() != 'y':
            continue
        else:
            username = loginUserInfo[line_idx][login_info_sheet_username]
            passwd = loginUserInfo[line_idx][login_info_sheet_passwd]
            data_sheet = loginUserInfo[line_idx][login_info_sheet_data_sheet]
            is_run = loginUserInfo[line_idx][login_info_sheet_is_run]
            # 这两行没啥用，可以去掉
            excute_result = loginUserInfo[line_idx][login_info_sheet_excute_result]
            excute_time = loginUserInfo[line_idx][login_info_sheet_excute_time]
            print(username, passwd, data_sheet, is_run, excute_result, excute_time)
            driver = login(username, passwd)
            contactsUserInfo = get_User_info(data_sheet)
            for contact_idx in range(1, len(contactsUserInfo)):
                if contactsUserInfo[contact_idx][contacts_info_sheet_is_run].lower() != 'y':
                    continue
                else:
                    contact_tuple = contactsUserInfo[contact_idx][
                                    contacts_info_sheet_name:contacts_info_sheet_assert_content + 1]

                    print("contact_tuple:", *contact_tuple, "contact_tuple的长度：", len(contact_tuple))
                    opExcel.writeContent(contact_idx + 1, contacts_info_sheet_excute_time,
                                         TimeUtil().get_datetime())
                    if addContacts(driver, *contact_tuple):
                        # True说明添加成功,将执行结果和时间写入对应列中
                        opExcel.writeContent(contact_idx + 1, contacts_info_sheet_excute_result, "success")

                    else:
                        # 说明添加失败，可以用来统计执行结果，将执行结果和时间写入对应列中，并标记失败
                        captureScreen(driver)
                        opExcel.writeContent(contact_idx + 1, contacts_info_sheet_excute_result, "fail")
                        flag = False

            driver.quit()

            # 切回第一个sheet OK了
            opExcel.set_sheet_by_sheetname(login_info_sheet)
            if flag == False:
                # 将qq账号sheet页对应的列写入执行失败结果和时间
                opExcel.writeContent(line_idx + 1, login_info_sheet_excute_result, "fail")

            else:
                # 将qq账号sheet页对应的列写入执行失败结果和时间
                opExcel.writeContent(line_idx + 1, login_info_sheet_excute_result, "success")
            opExcel.writeContent(line_idx + 1, login_info_sheet_excute_time, TimeUtil().get_datetime())


if __name__ == "__main__":
    run()
