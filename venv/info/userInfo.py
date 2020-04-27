__author__ = "Starry.feng"
from utility import excel

class user:
    def __init__(self):
        self.excel = excel.ExcelUtil("../testCase/Data/user_info.xls","user_info")
        self.info = self.excel.get_excel()
        self.user = self.info[0][1]
        self.password = self.info[1][1]
        self.server= self.info[2][1]
        self.except_result = self.info[3][1]
        self.assertion_keyword = self.info[4][1]
        #self.server="https://rhel7602.nextlabs.com:8444/rms"
        #self.server="https://rms-rhel74.qapf1.qalab01.nextlabs.com:8444/rms"
        #self.server="https://rms-centos7602.qapf1.qalab01.nextlabs.com:8444/rms"
        #self.server="https://testdrm.com"