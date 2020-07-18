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

print(test_data)


@ddt.ddt
class TestRunMain(unittest.TestCase):

    @ddt.data(*test_data)
    def test_run_case(self, test_data):
        global header, code, msg
        global res_value
        case_id = test_data[0]
        i = excel_data.get_rows_number(case_id)
        is_run = test_data[2]
        if str(is_run).upper() == 'YES':
            method = test_data[6]
            url = test_data[5]
            condition = test_data[3]
            if condition != None:
                rows_number = excel_data.get_rows_number(condition)
                res_value = excel_data.get_cell_value(rows_number, 13)
            mysql_query = test_data[15]
            if mysql_query != None:
                if headle_re.find_data(mysql_query):
                    mysql_query = headle_re.str_data('${phone}', mysql_query, gd.get_phone())
                else:
                    pass
            data = test_data[7]
            if data != None:
                if headle_re.find_data(data):
                    data = eval(headle_re.str_data('${phone}', data, gd.get_phone()))
                    if headle_re.find_data(str(data)):
                        data = eval(headle_re.str_data('${sql}', data,
                                                       handle_mysql.fetch_one(mysql_query)))
                else:
                    data = eval(data)
            is_header = test_data[9]
            if is_header.upper() == 'YES':
                header = eval(handle_ini.get_value(key='header', node='no_token', file_name='header.ini'))
                # print('不带token的header是------>', header)
            elif is_header.upper() == 'TOKEN':
                header = handle_ini.get_value(key='header', node='token', file_name='header.ini')
                # 读取header
                header = eval(headle_re.re_data(header, eval(excel_data.get_cell_value(i, 5))))
                # 替换header里变量,excel读取到的都是str都需要eval
                # print('带token的header是------>', header)
            else:
                header = None
            file = test_data[14]
            if file != None:
                # 判断是否有值
                file = eval(test_data[14])
            # cookies的先不写
            # cookie_method = test_data[8]
            # if cookie_method == 'yes':
            #     pass
            # if cookie_method == 'write':
            #     pass
            # if is_header == 'yes':
            #     pass
            excepect_method = test_data[10]
            excepect_result = test_data[11]
            res = request.run_main(method, url, data, header, file)
            try:
                code = res['code']
                print('code是------------>', code)
                msg = res['msg']
                print('msg是------------->', msg)
            except:
                excel_data.excel_write_data(i, 13, str(res))
                try:
                    message = res['message']
                    status_code = res['status_code']
                    if excepect_method == 'code':
                        try:
                            self.assertEqual(excepect_result, status_code)
                            excel_data.excel_write_data(i, 14, 'PASS')
                            return
                        except Exception as e:
                            excel_data.excel_write_data(i, 14, 'FAIL')
                            raise e
                    elif excepect_method == 'msg':
                        try:
                            self.assertEqual(excepect_result, message)
                            excel_data.excel_write_data(i, 14, 'PASS')
                            return
                        except Exception as e:
                            excel_data.excel_write_data(i, 14, 'FAIL')
                            raise e
                    elif excepect_method == 'json':
                        try:
                            json_res = handle_result_json(res, eval(excepect_result))
                            self.assertTrue(json_res)
                            excel_data.excel_write_data(i, 14, 'PASS')
                            return
                        except Exception as e:
                            excel_data.excel_write_data(i, 14, 'FAIL')
                            raise e
                except:
                    excel_data.excel_write_data(i, 14, 'ERROR')

            result = str(res).encode('UTF-8')
            # 设置编码格式
            excel_data.excel_write_data(i, 13, result)
            if excepect_method == 'code':
                try:
                    self.assertEqual(excepect_result, code)
                    excel_data.excel_write_data(i, 14, 'PASS')
                except Exception as e:
                    excel_data.excel_write_data(i, 14, 'FAIL')
                    raise e
            elif excepect_method == 'msg':
                try:
                    self.assertEqual(excepect_result, msg)
                    excel_data.excel_write_data(i, 14, 'PASS')
                except Exception as e:
                    excel_data.excel_write_data(i, 14, 'FAIL')
                    raise e
            elif excepect_method == 'json':
                try:
                    json_res = handle_result_json(res, eval(excepect_result))
                    self.assertTrue(json_res)
                    excel_data.excel_write_data(i, 14, 'PASS')
                except Exception as e:
                    excel_data.excel_write_data(i, 14, 'FAIL')
                    raise e
            elif excepect_method == 'sql':
                try:
                    self.assertEqual(excepect_result, handle_mysql.fetch_one(mysql_query))
                    excel_data.excel_write_data(i, 14, 'PASS')
                except Exception as e:
                    excel_data.excel_write_data(i, 14, 'FAIL')
                    raise e
            print('返回的数据是--------->', res)


if __name__ == '__main__':
    unittest.main()
