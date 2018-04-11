#!/usr/bin/env python
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from base.run_method import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
import json
from data.depend_data import DependData


class RunTest(object):
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.contain = CommonUtil()

    #程序执行的主入口
    def go_on_run(self):
        res = None
        pass_count = []
        fail_count = []
        rows_count = self.data.get_case_lines()
        for i in range(1, rows_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.data.get_url(i)
                method = self.data.get_request_method(i)
                data = self.data.get_data_from_json(i)
                header = self.data.is_header(i)
                expect = self.data.get_except_data(i)
                depend_case = self.data.is_depend(i)
                if depend_case != None:
                    self.depend_data = DependData()
                    #获取依赖响应数据
                    depend_response_data = self.depend_data.get_data_for_key(i)
                    #获取依赖的key
                    depend_key = self.data.get_depend_filed(i)
                    data[depend_key] = depend_response_data

                res = self.run_method.run_main(url, method, data, header)
                if self.contain.is_contain(expect, str(res)):
                    self.data.write_result(i+1, 'pass')
                    pass_count.append(i)
                else:
                    self.data.write_result(i, json.dumps(res))
                    fail_count.append(i)
        print(len(pass_count))
        print(len(fail_count))

if __name__ == '__main__':
    run = RunTest()
    print(run.go_on_run())

