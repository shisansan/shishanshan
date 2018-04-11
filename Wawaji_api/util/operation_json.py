#!/usr/bin/env python
import json

class OperatioJson(object):
    def __init__(self, filename=None):
        if filename:
            self.filename = filename
        else:
            self.filename = '../dataconfig/json.json'
        self.data = self.read_data()

     #读取json文件
    def read_data(self):
        with open(self.filename) as fp:
            data = json.load(fp)
            return data

    #根据关键字获取数据
    def get_data(self, id):
        return self.data[id]

if __name__ == '__main__':
    oper = OperatioJson()
    print(oper.get_data('phone'))