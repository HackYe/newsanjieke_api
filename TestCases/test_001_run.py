# -*- coding: utf-8 -*-

"""
@Author: YuanYe
@time: 2020/7/9 17:07
"""
import unittest
import ddt
import HTMLTestRunnerNew
import json
from Base.base_request import request
from Tools.handle_excel import excel_data
from Tools.handle_init import handle_ini
from Tools.handle_replace import headle_re
from Tools.handle_mysql import handle_mysql
from Tools.handle_result import handle_result_json
from Common.get_data import gd

test_data = excel_data.get_excel_data()
# sheet名称
sheet_name = 'initialization'


# print(test_data)


@ddt.ddt
class TestRunMain(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # 连接数据库
        handle_mysql.__init__()

    @classmethod
    def tearDownClass(cls) -> None:
        # 每次执行用例后手机号+1
        excel_data.excel_write_data(3, 2, gd.get_phone() + 1)
        # 关闭数据库连接
        handle_mysql.close()

    @ddt.data(*test_data)
    def test_run_case(self, test_data):
        global header, code, msg, data_list, res_data, url_list
        global data_value, url_value
        case_id = test_data[0]
        i = excel_data.get_rows_number(case_id)
        is_run = test_data[2]
        if str(is_run).upper() == 'YES':
            print('正在测试的用例是{}'.format(test_data[1]))
            method = test_data[8]
            url = test_data[7]
            data_condition = test_data[3]
            rely_value = test_data[4]
            url_condition = test_data[5]
            url_rely_value = test_data[6]
            if rely_value != None:
                rely_value = str(rely_value).split(',')
            if url_rely_value != None:
                url_rely_value = str(url_rely_value).split(',')
            # data的前置条件
            if data_condition != None:
                data_list = []
                if str(data_condition).find(',') != -1:
                    rely_key = str(data_condition).split(',')
                    test_value = zip(rely_key, rely_value)
                    for items in test_value:
                        rows_number = excel_data.get_rows_number(items[0])
                        data_value = excel_data.get_cell_value(rows_number, 15)
                        res = eval(items[1])
                        data_list.append(res)
                else:
                    rows_number = excel_data.get_rows_number(data_condition)
                    data_value = excel_data.get_cell_value(rows_number, 15)
            if url_condition != None:
                url_list = []
                if str(url_condition).find(',') != -1:
                    url_rely_key = str(url_condition).split(',')
                    test_value = zip(url_rely_key, url_rely_value)
                    for items in test_value:
                        rows_number = excel_data.get_rows_number(items[0])
                        url_value = excel_data.get_cell_value(rows_number, 15)
                        res = eval(items[1])
                        url_list.append(res)
                else:
                    rows_number = excel_data.get_rows_number(url_condition)
                    url_value = excel_data.get_cell_value(rows_number, 15)
            mysql_query = test_data[17]
            if mysql_query != None:
                if headle_re.find_data(mysql_query):
                    mysql_query = headle_re.str_data('${phone}', mysql_query, gd.get_phone())
            data = test_data[9]
            #处理url
            if url != None:
                try:
                    if str(url).find('${rely_key}') != -1:
                        url = headle_re.str_data('${rely_key}', url, eval(excel_data.get_cell_value(i, 7)))
                    # rely_keys为多个前置条件替换通用str
                    elif str(url).find('${rely_keys}') != -1:
                        res_data = headle_re.strs_data(url, url_list)
                        url = res_data
                    else:
                        pass
                except:
                    pass

            #处理data
            if data != None:
                try:
                    if str(data).find('${phone}') != -1:
                        data = eval(headle_re.str_data('${phone}', data, gd.get_phone()))
                        if str(data).find('${sql}') != -1:
                            data = eval(headle_re.str_data('${sql}', data, handle_mysql.fetch_one(mysql_query)))
                    # rely_key为单个前置条件替换通用str
                    elif str(data).find('${rely_key}') != -1:
                        data = eval(headle_re.str_data('${rely_key}', data, eval(excel_data.get_cell_value(i, 5))))
                    # rely_keys为多个前置条件替换通用str
                    elif str(data).find('${rely_keys}') != -1:
                        res_data = headle_re.strs_data(data, data_list)
                        data = eval(res_data)
                    else:
                        data = eval(data)
                except:
                    pass
            is_header = test_data[11]
            if is_header.upper() == 'YES':
                header = eval(handle_ini.get_value(key='header', node='no_token', file_name='header.ini'))
                # print('不带token的header是------>', header)
            elif is_header.upper() == 'TOKEN':
                header = handle_ini.get_value(key='header', node='token', file_name='header.ini')
                # 读取header
                header = eval(headle_re.re_data(header, gd.get_token(3, 15, 1)))
                # 替换header里变量
                # print('带token的header是------>', header)
            else:
                header = None
            file = test_data[16]
            if file != None:
                # 判断是否有值
                file = eval(test_data[16])
            # cookies的先不写
            # cookie_method = test_data[8]
            # if cookie_method == 'yes':
            #     pass
            # if cookie_method == 'write':
            #     pass
            # if is_header == 'yes':
            #     pass
            excepect_method = test_data[12]
            excepect_result = test_data[13]
            res = request.run_main(method, url, data, header, file)
            try:
                code = res['code']
                # print('code是------------>', code)
                msg = res['msg']
                # print('msg是------------->', msg)
            except:
                excel_data.excel_write_data(i, 15, str(res), sheet_name)
                try:
                    message = res['message']
                    status_code = res['status_code']
                    if excepect_method == 'code':
                        try:
                            self.assertEqual(excepect_result, status_code)
                            excel_data.excel_write_data(i, 16, 'PASS', sheet_name)
                            return
                        except:
                            excel_data.excel_write_data(i, 16, 'FAIL', sheet_name)
                            return
                    elif excepect_method == 'msg':
                        try:
                            self.assertEqual(excepect_result, message)
                            excel_data.excel_write_data(i, 16, 'PASS', sheet_name)
                            return
                        except:
                            excel_data.excel_write_data(i, 16, 'FAIL', sheet_name)
                            return
                    elif excepect_method == 'json':
                        try:
                            json_res = handle_result_json(res, eval(excepect_result))
                            self.assertTrue(json_res)
                            excel_data.excel_write_data(i, 16, 'PASS', sheet_name)
                            return
                        except:
                            excel_data.excel_write_data(i, 16, 'FAIL', sheet_name)
                            return
                except:
                    excel_data.excel_write_data(i, 16, 'ERROR', sheet_name)
                    return
            result = str(res).encode('UTF-8')
            # 设置编码格式
            excel_data.excel_write_data(i, 15, result, sheet_name)
            if excepect_method == 'code':
                try:
                    self.assertEqual(excepect_result, code)
                    excel_data.excel_write_data(i, 16, 'PASS', sheet_name)
                except Exception as e:
                    excel_data.excel_write_data(i, 16, 'FAIL', sheet_name)
                    raise e
            elif excepect_method == 'msg':
                try:
                    self.assertEqual(excepect_result, msg)
                    excel_data.excel_write_data(i, 16, 'PASS', sheet_name)
                except Exception as e:
                    excel_data.excel_write_data(i, 16, 'FAIL', sheet_name)
                    raise e
            elif excepect_method == 'json':
                try:
                    json_res = handle_result_json(res, eval(excepect_result))
                    self.assertTrue(json_res)
                    excel_data.excel_write_data(i, 16, 'PASS', sheet_name)
                except Exception as e:
                    excel_data.excel_write_data(i, 16, 'FAIL', sheet_name)
                    raise e
            elif excepect_method == 'sql':
                try:
                    self.assertEqual(excepect_result, handle_mysql.fetch_one(mysql_query))
                    excel_data.excel_write_data(i, 16, 'PASS', sheet_name)
                except Exception as e:
                    excel_data.excel_write_data(i, 16, 'FAIL', sheet_name)
                    raise e
            print('返回的数据是--------->', res)


if __name__ == '__main__':
    unittest.main()
