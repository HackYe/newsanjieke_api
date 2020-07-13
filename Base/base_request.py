# -*- coding: utf-8 -*-

"""
@Author: YuanYe
@time: 2020/7/9 11:27
"""

import requests
import json
from Tools.handle_init import handle_ini
from Common.get_data import gd


class BaseRequest:
    def send_post(self, url, data, header=None, file=None, cookie=None):
        '''
        发送post请求
        '''
        response = requests.post(url=url, data=data, headers=header, files=file, cookies=cookie)
        res = response.text
        return res

    def send_get(self, url, data, header=None, file=None, cookie=None):
        '''
        发送get请求
        '''
        response = requests.get(url=url, params=data, headers=header, files=file, cookies=cookie)
        res = response.text
        return res

    def run_main(self, method, url, data, header=None, file=None, cookie=None):
        '''
        执行方法，传递method、url、data等参数
        '''
        base_url = handle_ini.get_value(node=gd.get_env())
        # print(base_url)
        if 'http' not in url:
            url = base_url + url
        if method.upper() == 'GET':
            res = self.send_get(url, data, header, file, cookie)
        else:
            res = self.send_post(url, data, header, file, cookie)
        try:
            res = json.loads(res)
        except:
            print('这个结果是一个text')
        # print('------>', res)
        return res


request = BaseRequest()

if __name__ == "__main__":
    request = BaseRequest()
    request.run_main('get', '/coupon/list', "{'username':'11111'}")
