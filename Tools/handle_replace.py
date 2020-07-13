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


headle_re = HeadleRe()

if __name__ == '__main__':
    res = headle_re.re_data("{'app': 'sanjieke', 'platform': 'ios' , 'authorization':'${token_nologin}'}",'1112233')
    print(res)
