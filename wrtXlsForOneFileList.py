#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime
import updatedApiChecker as cheker
import os
import xlrd
import xlwt
import copy as another_copy
from xlutils.copy import copy

# 根据 filelist.txt check代码
# 测试用目录
fileDir = "/Users/wangpei/workspace/AliSourcingProject/AliSourcingBuyerPoseidons/src-hook/com/alibaba/intl/android/apps" \
          "/poseidon/utils/EnvironmentInspector.java"


# 获得list对象
def read_file_list_as_lines(path="fileList.txt"):
    with open(path, "r+") as f:
        lines = f.readlines()
    return lines


def get_res_dic_list_from_file_list(lines):
    res_list = []
    for file_dir in lines:
        res_dic = {}
        res_dic = cheker.check_file_for_api_allinone(file_dir)
        # print(res_dic)
        res_list.append(res_dic)
    print("res_list_for_this_fileList.txt", res_list)
    return res_list


def wrt_res_list_to_excel_append(res_list=[], path='example1.xls'):
    wb = xlrd.open_workbook(path)
    sheets_name = wb.sheet_names()
    ws = wb.sheet_by_name(sheets_name[0])
    rows_exists = ws.nrows
    print("开始写的行号为： ", rows_exists)
    new_wb = copy(wb)
    new_ws = new_wb.get_sheet(0)
    if not res_list:
        print("搜索结果列表为空,直接退出写入文件操作")
        return
    # col_list = []
    for item in res_list:
        v_list = []
        for k, v in item.items():
            # print("k: ", k)
            # print("v:", v)
            v_list.append(v)  # 将一个结果dic中的v append成一个v_list
        # print(v_list)
        # col_num = [0 for x in range(0, len(v_list))]  # 用以记录每行字符长度
        length = len(v_list)
        if v_list[length - 1] == 0:  # 如果是空记录 跳过不记录
            continue
        else:
            for j in range(0, len(v_list)):
                new_ws.write(rows_exists, 0, rows_exists)  # 写id
                if isinstance(v_list[j], list):
                    new_ws.write(rows_exists, j + 1, repr(v_list[j]))
                else:
                    new_ws.write(rows_exists, j + 1, v_list[j])  # 写数据
                # if type(v_list[j]) is int:
                #     col_num[j] = 11
                # elif type(v_list[j]) is str:
                #     col_num[j] = len(v_list[j])
            # col_list.append(another_copy.copy(col_num))
            rows_exists += 1

    # 获取每一列最大宽度
    # col_max_num = get_max_col(col_list)
    # print(col_list)
    # print(col_max_num)
    # for i in range(0, len(col_max_num)):
    #     new_ws.col(i + 1).width = 256 * (col_max_num[i] + 2)
    new_wb.save(path)
    print("结果列表所有数据写入成功.")


def set_width_via_context(xls_path):  # 设置自适应列宽
    wb = xlrd.open_workbook(xls_path)
    sheets_name = wb.sheet_names()
    ws = wb.sheet_by_name(sheets_name[0])
    col_list = []
    row_num = ws.nrows
    col_num = ws.ncols
    for row in range(row_num):
        col_num_list = [0 for x in range(0, col_num)]
        for col in range(0, col_num):
            if type(ws.cell_value(row, col)) is int:
                col_num_list[col] = 11
            elif type(ws.cell_value(row, col)) is str:
                col_num_list[col] = len(ws.cell_value(row, col))
        col_list.append(another_copy.copy(col_num_list))
    # return col_list
    col_max_num = get_max_col(col_list)
    new_wb = copy(wb)
    new_ws = new_wb.get_sheet(0)
    for i in range(0, len(col_max_num)):
        new_ws.col(i).width = 256 * (col_max_num[i] + 2)
    new_wb.save(xls_path)
    print("自适应调整列宽成功")


def get_max_col(max_list):
    line_list = []
    # i表示行，j代表列
    if len(max_list) == 0:
        return line_list
    for j in range(len(max_list[0])):
        line_num = []
        for i in range(len(max_list)):
            line_num.append(max_list[i][j])  # 将每列的宽度存入line_num
        line_list.append(max(line_num))  # 将每列最大宽度存入line_list
    return line_list


def wrt_xls_file_header(path='output.xls'):
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('sheet1')
    ws.write(0, 0, "id")
    ws.write(0, 1, "git-name")
    ws.write(0, 2, "package:file")
    ws.write(0, 3, "getExternalStorageDirectory调用次数")
    ws.write(0, 4, "ESD所在line")

    ws.write(0, 5, "getExternalStoragePublicDirectory调用次数")
    ws.write(0, 6, "ESPD所在line")

    ws.write(0, 7, "getDownloadCacheDirectory调用次数")
    ws.write(0, 8, "DCD所在line")

    ws.write(0, 9, "getStorageDirectory调用次数")
    ws.write(0, 10, "SD所在line")

    ws.write(0, 11, "getDataDirectory调用次数")
    ws.write(0, 12, "DD所在line")

    ws.write(0, 13, "getRootDirectory调用次数")
    ws.write(0, 14, "RD所在line")

    ws.write(0, 15, "mnt硬编码次数")
    ws.write(0, 16, "mnt所在line")

    ws.write(0, 17, "sdCard硬编码次数")
    ws.write(0, 18, "sdCard所在line")

    ws.write(0, 19, 'total命中次数')
    wb.save(path)


def wrt_res_xls_content(source_txt_path='fileList.txt', xls_output_path='output.xls'):
    lines = read_file_list_as_lines(source_txt_path)
    res_list = get_res_dic_list_from_file_list(lines)
    wrt_res_list_to_excel_append(res_list, xls_output_path)


if __name__ == "__main__":
    wrt_res_xls_content()
