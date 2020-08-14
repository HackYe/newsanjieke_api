# -*- coding: utf-8 -*-

"""
@Author: YuanYe
@time: 2020/8/7 17:51
"""

from bs4 import BeautifulSoup


# 读取html
def html_read(file):
    soup = BeautifulSoup(open(file, encoding='utf-8'), features='html.parser')
    return soup


# 读取概要
def read_summary(file):
    summary = html_read(file).select('#show_detail_line > a.abstract.detail_button')
    for i in summary:
        return i.text


# 读取成功
def read_success(file):
    success = html_read(file).select('#show_detail_line > a.passed.detail_button')
    for i in success:
        return i.text


# 读取失败
def read_fail(file):
    fail = html_read(file).select('#show_detail_line > a.failed.detail_button')
    for i in fail:
        return i.text


# 读取错误
def read_error(file):
    error = html_read(file).select('#show_detail_line > a.errored.detail_button')
    for i in error:
        return i.text


# 读取错误
def read_jumpover(file):
    jumpover = html_read(file).select('#show_detail_line > a.skiped.detail_button')
    for i in jumpover:
        return i.text


# 读取所有
def read_all(file):
    all = html_read(file).select('#show_detail_line > a.all.detail_button')
    for i in all:
        return i.text


# 一键读取
def one_click_reading(file):
    summary = read_summary(file)
    success = read_success(file)
    fail = read_fail(file)
    error = read_error(file)
    all = read_all(file)
    res = summary, success, fail, error, all
    result = str(res).replace('\'', '')
    return result


if __name__ == '__main__':
    data = '/Users/yuanye/PycharmProjects/newsanjieke_api/Outputs/html/Report_2020-08-07-17-16-51.html'
    res = one_click_reading(data)
    print(type(res))
