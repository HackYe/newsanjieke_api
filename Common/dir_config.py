# -*- coding: utf-8 -*-

"""
@Author: YuanYe
@time: 2020/7/9 14:22
"""

import os
import time

# 获取顶级目录路径
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

# host配置
server_url = os.path.join(project_path, 'Config', 'server.ini')
# mysql配置
mysql_path = os.path.join(project_path, 'Config', 'mysql.ini')
# excel路径
excel_path = os.path.join(project_path, 'Case', 'sanjieke_auto.xlsx')

# 获取配置文件路径
config_path = os.path.join(project_path, 'Config/')

# 获取case所在目录
test_case_path = os.path.join(project_path, 'TestCases')

# 获取测试报告配置文件路径
time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
report_html_path = os.path.join(project_path, 'Outputs', 'html', 'Report_{0}.html'.format(time))

# 获取测试报告目录的路径
report_path = os.path.join(project_path, 'Outputs', 'html')

if __name__ == '__main__':
    print(report_path)
