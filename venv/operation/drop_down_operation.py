__author__ = "starry"

from PO import homePage,myvalutPage,workspace_page,drop_down_box_page
from info import userInfo
from operation import loginOperation
from time import sleep

class drop_down(object):
    def __init__(self,web_driver,log):
        self.driver = web_driver
        self.log = log
        self.user_login = loginOperation.login_operation(self.driver,self.log)
        self.user_info = userInfo.user()
        self.home = homePage.home(self.driver,self.log)
        self.drop = drop_down_box_page.drop_down_box(self.driver,self.log)

    def myvault_choose_drop_dwon(self,label_type):
        print("---------- test sort file in workspace ----------")
        self.user_login.normal_accout_login(self.user_info.user,self.user_info.password,self.user_info.except_result,self.user_info.assertion_keyword)
        sleep(0.5)
        self.home.click_myVault()
        sleep(0.5)
        self.drop.option_elem(label_type)

        print("---------- test end ----------")

    def workspace_choose_drop_dwon(self,label_type):
        print("---------- test sort file in workspace ----------")
        self.user_login.normal_accout_login(self.user_info.user,self.user_info.password,self.user_info.except_result,self.user_info.assertion_keyword)
        sleep(0.5)
        self.home.click_workspace()
        sleep(0.5)
        self.drop.option_elem(label_type)

        print("---------- test end ----------")