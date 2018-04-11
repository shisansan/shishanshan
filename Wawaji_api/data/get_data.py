#!/usr/bin/env python
from util.operation_excel import OperationExcel
from data.data_config import *
from util.operation_json import OperatioJson

class GetData(object):
    def __init__(self):
        self.operat_excel = OperationExcel()
        self.glob_var = Globle_var()
        self.operat_json = OperatioJson()

    #获取excel行数，就是case个数
    def get_case_lines(self):
        return self.operat_excel.get_line()

    #获取是否执行
    def get_is_run(self, row):
        flag = None
        col = self.glob_var.get_run()
        run_model = self.operat_excel.get_cell_value(row, col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    #是否携带henader
    def is_header(self, row):
        col = self.glob_var.get_header()
        header = self.operat_excel.get_cell_value(row, col)
        if header == 'yes':
            return self.glob_var.get_header_value()
        else:
            return None

    #获得请求方式
    def get_request_method(self, row):
        col = self.glob_var.get_run_way()
        request_method = self.operat_excel.get_cell_value(row, col)
        return request_method

    #获取host
    def get_host(self, row):
        col = self.glob_var.get_host()
        host = self.operat_excel.get_cell_value(row, col)
        return host

    #获取URL
    def get_url(self, row):
        col = self.glob_var.get_url()
        url = self.operat_excel.get_cell_value(row, col)
        return self.get_host(row)+url

    #获取请求数据
    def get_request_data(self, row):
        col = self.glob_var.get_data()
        data = self.operat_excel.get_cell_value(row, col)
        if data == '':
            return None
        return data

    #通过获取关键字拿到data数据
    def get_data_from_json(self, row):
        data = self.get_request_data(row)
        if data != None:
            request_data = self.operat_json.get_data(self.get_request_data(row))
            return request_data
        else:
            return None

    #获取预期结果
    def get_except_data(self, row):
        col = self.glob_var.get_expect()
        expect = self.operat_excel.get_cell_value(row, col)
        if expect == '':
            return None
        return expect

    #写入运行结果
    def write_result(self, row, value):
        col = self.glob_var.get_result()
        self.operat_excel.write_value(row, col+1, value)

    #获取依赖数据的key
    def get_depend_key(self, row):
        col = self.glob_var.get_data_depend()
        depend_key = self.operat_excel.get_cell_value(row, col)
        if depend_key == '':
            return None
        else:
            return depend_key

    #判断是否有case依赖
    def is_depend(self, row):
        col = self.glob_var.get_field_depend()
        depend_case_id = self.operat_excel.get_cell_value(row, col)
        if depend_case_id == '':
            return None
        else:
            return depend_case_id

    #获取数据依赖字段
    def get_depend_filed(self, row):
        col = self.glob_var.get_field_depend()
        data = self.operat_excel.get_cell_value(row, col)
        if data == '':
            return None
        else:
            return data



if __name__ == '__main__':
    get_data = GetData()
    data = get_data.get_request_data(1)
    expect = get_data.get_except_data(1)
    print(data)
    print(type(data))
    print(expect)
    print(type(expect))
    get_data.write_result(1, 2)


