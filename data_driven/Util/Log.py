#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# File:         Log.py
# Author:       ls
# Date:         2020/10/14 16:07
#-------------------------------------------------------------------------------
import logging.config
import logging

logging.config.fileConfig(r"C:\Users\LS\PycharmProjects\data_driven\Conf\log.conf")
logger=logging.getLogger("example01")

# 日志文件配置：多个logger，每个logger指定不同的handler
# handler：设置了日志输出行的格式
# handler：以及设定写日志到文件（是否回滚）还是到屏幕
# handler：还设定了打印日志的级别

def debug(message):
    logger.debug(message)


def warning(message):
    logger.warning(message)

def info(message):
    logger.info(message)

def error(message):
    logger.error(message)

def debug(message):
    logger.debug(message)