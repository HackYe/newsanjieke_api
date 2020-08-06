# -*- coding: utf-8 -*-

"""
@Author: YuanYe
@time: 2020/8/3 15:58
"""

# -*- coding: utf-8 -*-

"""
@Author: YuanYe
@time: 2020/7/3 10:17
"""

import unittest
import HTMLTestRunnerNew
from Common.HTMLTestRunner_cn import HTMLTestRunner as html_new
from Common.dir_config import *
from Common.get_data import gd


# 导入测试报告文件


class HTMLTestRunner:

    def html_report_01(self):
        discover = unittest.defaultTestLoader.discover(test_case_path, "test_*.py")

        with open(report_html_path, 'wb+') as file:
            runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                                      title='三节课接口测试报告',
                                                      description='三节课' + str(gd.get_env()) + '接口测试报告',
                                                      tester='YuanYe')
            runner.run(discover)

    def html_report_02(self):
        discover = unittest.defaultTestLoader.discover(test_case_path, "test_*.py")

        runner = html_new(
            title="三节课接口测试报告",
            description='三节课' + str(gd.get_env()) + '接口测试报告',
            stream=open(report_html_path, "wb+"),
            verbosity=2,
            retry=0,
            save_last_try=True)
        runner.run(discover)


if __name__ == '__main__':
    Run = HTMLTestRunner()
    Run.html_report_02()
