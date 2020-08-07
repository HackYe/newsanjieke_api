# -*- coding: utf-8 -*-

"""
@Author: YuanYe
@time: 2020/8/7 17:51
"""

import urllib.request
from Common.dir_config import report_path
import re
from bs4 import BeautifulSoup
import lxml


def read_html(file_name):
    from lxml import etree
    f = open(file_name, "r", encoding="utf-8")  # 读取文件
    f = f.read()
    html = etree.HTML(f.encode('utf-8'))  # 把字符串转化为可处理的格式
    return html


def read_html_text(html):
    result = html.xpath('//*[@id="show_detail_line"]/a[1]')
    result2 = html.xpath('//*[@id="show_detail_line"]/a[2]')
    result3 = html.xpath('//*[@id="show_detail_line"]/a[3]')
    print(result)
    print(result2)
    print(result3)


def get_content(url):
    resp = urllib.request.urlopen(url)
    html = resp.read()
    bs = BeautifulSoup(html)
    return bs.textarea.get_text()


if __name__ == '__main__':
    data = '/Users/yuanye/PycharmProjects/newsanjieke_api/Outputs/html/Report_2020-08-07-17-16-51.html'
    res = read_html(data)
    read_html_text(res)
