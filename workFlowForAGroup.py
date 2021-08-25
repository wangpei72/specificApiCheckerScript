#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import fileListGetter as getter
import wrtXlsForOneFileList as writer


def get_file_lists(group_dir):  # 会在指定目录下生成所有txt文件
    getter.get_file_lists_allinone(group_dir, "fileListsFromGroupSDK")


def wrt_all_lists_res(file_lists_dir, xls_output_path='output.xls'):
    cur_dir =os.path.dirname(os.path.realpath(__file__))
    txt_files = os.listdir(file_lists_dir)
    for txt_file in txt_files:
        # 这里源txt文件可能存在相对路径和绝对路径相冲突的问题
        writer.wrt_res_xls_content(file_lists_dir + "/" + txt_file, xls_output_path)


def worflow_start(group_dir, file_lists_dir, xls_ouput_path='output.xls'):
    get_file_lists(group_dir)
    writer.wrt_xls_file_header(xls_ouput_path)
    wrt_all_lists_res(file_lists_dir)
    writer.set_width_via_context(xls_ouput_path)


if __name__ == "__main__":
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    file_lists_dir = os.path.join(cur_dir, "fileListsFromGroupSDK")
    group_dir = "/Users/wangpei/git-groups/"
    worflow_start(group_dir, file_lists_dir)

