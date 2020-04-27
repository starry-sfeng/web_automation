__author__ = "starry"
from PO import BaseAction,homePage,search_feature,workspace_page,myvalutPage,file_list_page
from info import userInfo
from operation import loginOperation
from time import sleep

class search_operation(object):
    def __init__(self,web_driver,log):
        self.driver = web_driver
        self.log = log
        self.user_info = userInfo.user()
        self.user_login = loginOperation.login_operation(self.driver,self.log)
        self.home = homePage.home(self.driver,self.log)
        self.file_list = file_list_page.file_list(self.driver,self.log)
        self.workspace = workspace_page.workSpace(self.driver,self.log)
        self.myvault = myvalutPage.myvalut(self.driver,self.log)
        self.search = search_feature.search(self.driver,self.log)


    def search_workspace_file(self,keyWord):
        # print("---------- test search file in workspace ----------")
        self.log.debug("---------- test search file in workspace ----------")
        self.user_login.normal_accout_login(self.user_info.user,self.user_info.password,self.user_info.except_result,self.user_info.assertion_keyword)
        sleep(0.5)
        self.home.click_workspace()
        sleep(0.5)
        self.search.search_file(keyWord)

        # print("---------- test end ----------")
        self.log.debug("---------- test end ----------")

    def search_myvault_file(self,keyWord):
        # print("---------- test search file in workspace ----------")
        self.log.debug("---------- test search file in myvault ----------")
        self.user_login.normal_accout_login(self.user_info.user,self.user_info.password,self.user_info.except_result,self.user_info.assertion_keyword)
        sleep(0.5)
        self.home.click_myVault()
        sleep(0.5)
        self.search.search_file(keyWord)

        self.log.debug("---------- test end ----------")
