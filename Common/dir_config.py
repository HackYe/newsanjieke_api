# -*- coding: utf-8 -*-

"""
@Author: YuanYe
@time: 2020/7/9 14:22
"""

import os

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
