# -*- coding: utf-8 -*-

"""
@Author: YuanYe
@time: 2020/7/13 18:59
"""

import pymysql
from Tools.handle_init import handle_ini


class HandleMysql:

    def __init__(self):
        host = handle_ini.get_value('host', 'Mysql', 'mysql.ini')
        user = handle_ini.get_value('user', 'Mysql', 'mysql.ini')
        password = handle_ini.get_value('password', 'Mysql', 'mysql.ini')
        port = int(handle_ini.get_value('port', 'Mysql', 'mysql.ini'))
        # 连接数据库
        self.mysql = pymysql.connect(host=host, user=user, password=password, port=port, charset='utf8')
        self.cursor = self.mysql.cursor(pymysql.cursors.DictCursor)

    def fetch_one(self, sql):
        self.cursor.execute(sql)
        self.mysql.commit()
        return self.cursor.fetchone()  # 返回一条数据，元组

    def fetch_all(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()  # 返回多条数据的时候，元组里面套元组

    def close(self):
        self.cursor.close()  # 关闭游标
        self.mysql.close()  # 关闭连接


handle_mysql = HandleMysql()
if __name__ == '__main__':
    res = handle_mysql.fetch_one(
        "SELECT `code` FROM sjk_user.validation_code WHERE target = '+8613299203435' ORDER BY id DESC LIMIT 1")
    print(eval((res)['code']))
    handle_mysql.close()
