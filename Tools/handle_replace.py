# -*- coding: utf-8 -*-

"""
@Author: YuanYe
@time: 2020/7/13 10:22
"""
import re


class HeadleRe:

    def re_data(self, raw_value, new_value):
        data = '\$\{.*?}'
        key = re.search(data, raw_value).group()
        if raw_value.find(key) != -1:
            res = raw_value.replace(key, new_value)
            return res

    def str_data(self, key, raw_value, new_value):
        if str(raw_value).find(key) != -1:
            res = str(raw_value).replace(key, str(new_value))
            return res

    def find_data(self, raw_value):
        data = '\$\{.*?}'
        key = bool(re.search(data, raw_value))
        return key


headle_re = HeadleRe()

if __name__ == '__main__':
    # res = headle_re.re_data("{'app': 'sanjieke', 'platform': 'ios' , 'authorization':'${token_nologin}'}", '1112233')
    # print(res)
    data = str({'username': '${phone}', 'password': 'Aa123123'})
    # res = headle_re.str_data('${phone}', data, '15677004994')
    res = headle_re.find_data(raw_value=data)
    print(res)
