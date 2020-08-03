# -*- coding: utf-8 -*-

"""
@Author: YuanYe
@time: 2020/7/13 11:29
"""
from Tools.handle_excel import excel_data
import time


class GetData:

    # 获取token
    def get_token(self, row, cols, index):
        '''
        :param row: 行
        :param cols:列
        :param index:sheet下标
        :return:
        '''
        res_data = eval(excel_data.get_cell_value(row, cols, index))
        return res_data['data']['token']

    # 获取环境变量
    def get_env(self):
        res_data = excel_data.get_cell_value(2, 2, 0)
        return res_data

    # 获取手机号
    def get_phone(self):
        res_data = excel_data.get_cell_value(3, 2, 0)
        return res_data

    # 获取更换手机号
    def get_new_phone(self):
        res_data = excel_data.get_cell_value(4, 2, 0)
        return res_data

    # 获取密码
    def get_password(self):
        res_data = excel_data.get_cell_value(5, 2, 0)
        return res_data

    # 获取新密码
    def get_new_password(self):
        res_data = excel_data.get_cell_value(6, 2, 0)
        return res_data

    def get_Timestamp(self):
        res_data = int(round(time.time() * 1000000))
        return res_data

gd = GetData()

if __name__ == '__main__':
    print(gd.get_Timestamp())
