#!/usr/bin/env python

class Globle_var(object):
    Id = 0
    name = 1
    host = 2
    url = 3
    run = 4
    request_method = 5
    header = 6
    case_depend = 7
    data_depend = 8
    field_depend = 9
    data = 10
    expect = 11
    result = 12


    def get_id(self):
        return Globle_var.Id

    def get_host(self):
        return Globle_var.host

    def get_url(self):
        return Globle_var.url

    def get_run(self):
        return Globle_var.run

    def get_run_way(self):
        return Globle_var.request_method

    def get_header(self):
        return Globle_var.header

    def get_case_depend(self):
        return Globle_var.case_depend

    def get_data_depend(self):
        return  Globle_var.data_depend

    def get_field_depend(self):
        return Globle_var.field_depend

    def get_data(self):
        return Globle_var.data

    def get_expect(self):
        return Globle_var.expect

    def get_result(self):
        return Globle_var.result

    def get_header_value(self):
        header = {
            'X-USER-ID': '82001019',
            'X-USER-TOKEN': '67c3b96c-4556-4390-a61b-72998f3ac1c5'
        }
        return header


