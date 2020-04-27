__author__ = "starry"

from PO import BaseAction,file_list_page,ready_file_page,upload_result_page,upload_file_page
from PO import view_fileInfo_page,workspace_page,homePage,file_menu_page
from info import userInfo
from time import sleep
from operation import loginOperation

class workspace_operation(object):
    def __init__(self,web_driver,log):
        self.driver = web_driver
        self.log = log
        self.user_info = userInfo.user()
        self.user_login = loginOperation.login_operation(self.driver,self.log)
        self.home = homePage.home(self.driver,self.log)
        self.view_fileInfo = view_fileInfo_page.view_file_info(self.driver,self.log)
        self.file_menu = file_menu_page.file_menu(self.driver,self.log)
        self.upload_file = upload_file_page.upload_file(self.driver,self.log)
        self.ready_file = ready_file_page.ready_file(self.driver,self.log)
        self.upload_result = upload_result_page.upload_result(self.driver,self.log)
        self.file_list = file_list_page.file_list(self.driver,self.log)
        self.workspace = workspace_page.workSpace(self.driver,self.log)


    def workspace_protect_file(self):
        self.log.debug("---------- test protect file in workspace ----------")
        self.user_login.normal_accout_login(self.user_info.user,self.user_info.password,self.user_info.except_result,self.user_info.assertion_keyword)
        sleep(0.5)
        self.home.click_workspace()
        sleep(0.5)
        self.workspace.click_upload_button()
        sleep(0.5)
        self.ready_file.click_browers_button(r"C:\upload02.exe")
        sleep(0.5)
        self.ready_file.click_proceed_button()
        sleep(0.5)
        self.upload_file.select_watermark_right(False)
        sleep(0.5)
        self.upload_file.click_upload_button()
        sleep(0.5)

        file_name1 = self.upload_result.workSpace_get_protect_file_name()
        sleep(1)
        file_name2 = "The rights-protected file '" + self.file_list.get_first_fileName_list()+ "' has been uploaded to the workspace."
        if file_name1 == file_name2:
            self.log.debug("file protect and upload success")
        else:
            self.log.debug("file protect fail")
            assert False
        sleep(0.5)

        sleep(10)
        self.file_menu.click_frist_file_menu(0)
        sleep(0.5)
        self.file_menu.click_view_file_info_icon()
        sleep(0.5)
        self.view_fileInfo.get_protect_file_actual_rights()

        # print("----- test end -----")
        self.log.debug("----- test end -----")

