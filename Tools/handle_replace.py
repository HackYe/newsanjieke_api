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
        '''
        :param key: 需要替换的格式，如${phone}
        :param raw_value: 需要替换的data
        :param new_value: 需要替换的新值
        :return:返回替换成功的
        '''
        if str(raw_value).find(key) != -1:
            res = str(raw_value).replace(key, str(new_value))
            return res

    def find_data(self, raw_value):
        '''
        :param raw_value: 需要替换的data
        :return: 返回True和False
        '''
        data = '\$\{.*?}'
        key = bool(re.search(data, raw_value))
        return key

    # 发现符合正则要求的数量
    def find_data_quantity(self, raw_value):
        data = '\$\{.*?}'
        pattern = re.compile(data)
        res = pattern.findall(raw_value)
        return len(res)

    # 发现符合正则要求的字符串
    def find_data_str(self, raw_value):
        data = '\$\{.*?}'
        pattern = re.compile(data)
        res = pattern.findall(raw_value)
        return res

    # 批量替换
    def strs_data(self, data, res_list):
        for item in range(len(res_list)):
            data = data.replace('${rely_keys}', str(res_list[item]), 1)
        return data


headle_re = HeadleRe()

if __name__ == '__main__':
    # res = headle_re.re_data("{'app': 'sanjieke', 'platform': 'ios' , 'authorization':'${token_nologin}'}", '1112233')
    # print(res)
    # data = str({'username': '${sku_id}', 'password': 'Aa123123'})
    # res = headle_re.str_data('${phone}', data, '15677004994')
    # res = headle_re.find_data(raw_value=data)
    import re



    result = ['654', 2]
    data = str(
        '{\'pay_channel\':\'wechat\',\'sku_id\':\'${rely_keys}\',\'coupons_code\':\'\',\'type\':\'${rely_keys}\',\'return_url\':\'sanjieke://sanjieke.cn/\'}')


    data = headle_re.strs_data(data,result)
    print(data)
    # def strs_data(data, res_list):
    #     for item in range(len(res_list)):
    #         data = data.replace('${rely_keys}', str(res_list[item]), 1)
    #     return data
    # data = strs_data(data, result)
    # print(data)



    # for item in range(len(result)):
    #     data = data.replace('${rely_keys}', str(result[item]), 1)
    # print(data)