# -*- coding: utf-8 -*-

"""
@Author: YuanYe
@time: 2020/7/9 14:21
"""
from Common import dir_config
import configparser


class HandleInit:

    def load_ini(self, file_name=None):
        if file_name == None:
            file_name = 'server.ini'
        file_path = dir_config.config_path + file_name
        cf = configparser.ConfigParser()
        cf.read(file_path, encoding="utf-8-sig")
        return cf

    def get_value(self, key=None, node=None, file_name=None):
        '''
        获取ini里面的value
        '''
        if node == None:
            node = 'Pre'
        if key == None:
            key = 'host'
        cf = self.load_ini(file_name)
        try:
            data = cf.get(node, key)
        except Exception:
            print("没有获取到值")
            data = None
        return data


handle_ini = HandleInit()

if __name__ == '__main__':
    print(handle_ini.get_value(node='no_token', key='header', file_name='header.ini'))
    print(handle_ini.load_ini())
