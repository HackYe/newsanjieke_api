# -*- coding: utf-8 -*-

"""
@Author: YuanYe
@time: 2020/8/7 15:23
"""

import unittest
from BeautifulReport import BeautifulReport
from Common.HTMLTestRunner_cn import HTMLTestRunner as html_new
from Common.get_data import gd
from Common import Send_email
from Common.dir_config import *
import os
import time


# 第一个样式的报告
def run_01():
    discover = unittest.defaultTestLoader.discover(test_case_path, pattern='test_*.py', top_level_dir=None)
    now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
    reportName = now + '_repot.html'
    description = "三节课接口测试报告"
    BeautifulReport(discover).report(filename=reportName, description=description, report_dir=report_path)
    # print(discover)
    report = os.path.join(report_path, reportName)

    # 发送邮件
    Send_email.email(report)


# 第二个样式的报告
def run_02():
    discover = unittest.defaultTestLoader.discover(test_case_path, pattern='test_*.py',
                                                   top_level_dir=None)
    now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
    reportName = now + '_report.html'
    report = os.path.join(report_path, reportName)
    runner = html_new(title="三节课接口测试报告",
                      description='三节课' + str(gd.get_env()) + '接口测试报告',
                      stream=open(report, "wb+"),
                      verbosity=2,
                      retry=0,
                      save_last_try=True)
    # print(discover)
    runner.run(discover)
    # 发送邮件
    Send_email.email(report)


if __name__ == "__main__":
    run_02()