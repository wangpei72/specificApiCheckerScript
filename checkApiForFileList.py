#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime
import updatedApiChecker as cheker
import os
import xlrd
import xlwt

# 根据 filelist.txt check代码

# 获得list对象
def read_file_list_as_list():
    with open("fileList.txt", "rw+") as f:
        list = f.readlines()
    return list


def get_res_dic_list_from_file_list():
    res_list = []
    for file_dir in list:
        res_dic = {}
        res_dic = cheker.check_file_for_api_allinone(file_dir)
        # print(res_dic)
        res_list.append(res_dic)
    print(res_list)
    return res_list


def wrt_res_list_to_excel_append(res_list=[]):
    if not res_list:
        return
    # style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('sheet1')
    ws.write(0, 0, "id")
    ws.write(0, 1, "git-name")
    ws.write(0, 2, "package:file")
    ws.write(0, 3, "ESD调用次数")
    ws.write(0, 4, "ESD所在line")

    ws.write(0, 5, "ESPD调用次数")
    ws.write(0, 6, "ESPD所在line")

    ws.write(0, 7, "DCD调用次数")
    ws.write(0, 8, "DCD所在line")

    ws.write(0, 9, "SD调用次数")
    ws.write(0, 10, "SD所在line")

    ws.write(0, 11, "DD调用次数")
    ws.write(0, 12, "DD所在line")

    ws.write(0, 13, "RD调用次数")
    ws.write(0, 14, "RD所在line")

    wb.save('example1.xls')



    # 建xls表sample
    # style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
    #                      num_format_str='#,##0.00')
    # style1 = xlwt.easyxf(num_format_str='D-MMM-YY')
    #
    # workbook = xlwt.Workbook(encoding='utf-8')
    # ws = workbook.add_sheet('sheet1')
    # ws.write(0, 0, 1234.56, style0)
    # ws.write(1, 0, datetime.now(), style1)
    # ws.write(2, 0, 1)
    # ws.write(2, 1, 1)
    # ws.write(2, 2, xlwt.Formula("A3+B3"))
    #
    # workbook.save('example.xls')


wrt_res_list_to_excel()