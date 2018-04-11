#!/usr/bin/env python
from util.operation_excel import OperationExcel
from base.run_method import RunMethod
from data.get_data import GetData
from jsonpath_rw import jsonpath, parse

class DependData(object):
    '''
    通过case_id获取该case_id的整行数据
    '''
    def __init__(self, case_id):
        self.case_id = case_id
        self.opera_excel = OperationExcel()
        self.data = GetData()

    #通过case_id去获取该case_id的整行数据
    def get_case_line_data(self):
        rows_data = self.opera_excel.get_rows_data(self.case_id)
        return rows_data

    #执行依赖测试，获取结果
    def run_depend(self):
        run_method = RunMethod()
        row_num = self.opera_excel.get_row_num(self.case_id)
        url = self.data.get_url(row_num)
        method = self.data.get_request_method(row_num)
        data = self.data.get_data_from_json(row_num)
        header = self.data.is_header(row_num)
        res = run_method.run_main(url=url, method=method, data=data, header=header)
        return res

    #根据依赖的key去获取执行依赖测试case的响应，然后返回
    def get_data_for_key(self, row):
        depend_data = self.data.get_depend_key(row)
        response_data = self.run_depend()
        json_exe = parse(depend_data)
        madle = json_exe.find(response_data)
        return [math.value for math in madle][0]







#jsonpath-rw的用法示例
# >>> from jsonpath_rw import jsonpath, parse
# >>> json_obj = {"student":[{"male":176,"female":162},{"male":174,"female":159}]}
# >>> jsonpath_expr = parse("student[*].male")
# >>> male = jsonpath_expr.find(json_obj)
# >>> male #返回的是list,但是不是我们想要的值
# [DatumInContext(value=176, path=Fields('male'), context=DatumInContext(value={'male': 176, 'female': 162}, path=<jsonpath_rw.jsonpath.Index object at 0x000001C6B95109B0>, context=DatumInContext(value=[{'male': 176, 'female': 162}, {'male': 174, 'female': 159}], path=Fields('student'), context=DatumInContext(value={'student': [{'male': 176, 'female': 162}, {'male': 174, 'female': 159}]}, path=This(), context=None)))), DatumInContext(value=174, path=Fields('male'), context=DatumInContext(value={'male': 174, 'female': 159}, path=<jsonpath_rw.jsonpath.Index object at 0x000001C6B9510588>, context=DatumInContext(value=[{'male': 176, 'female': 162}, {'male': 174, 'female': 159}], path=Fields('student'), context=DatumInContext(value={'student': [{'male': 176, 'female': 162}, {'male': 174, 'female': 159}]}, path=This(), context=None))))]
#
# #想要获取值，要用如下方法
# >>> [match.value for match in male]
# [176, 174]