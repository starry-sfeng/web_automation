__author__ = "Starry.feng"
from PO import BaseAction
from PO import myvalutPage
from operation import loginOperation
from info import userInfo,Logger
from PO import homePage,view_fileInfo_page,file_menu_page,upload_file_page,ready_file_page,upload_result_page,file_list_page
from time import sleep

class myvault_operation(object):
    def __init__(self,web_driver,log):
        self.driver =  web_driver
        self.log = log
        self.user_info = userInfo.user()
        self.user_login = loginOperation.login_operation(self.driver,self.log)
        self.home = homePage.home(self.driver,self.log)
        self.myvault = myvalutPage.myvalut(self.driver,self.log)
        self.view_fileInfo = view_fileInfo_page.view_file_info(self.driver,self.log)
        self.file_menu = file_menu_page.file_menu(self.driver,self.log)
        self.upload_file = upload_file_page.upload_file(self.driver,self.log)
        self.ready_file = ready_file_page.ready_file(self.driver,self.log)
        self.upload_result = upload_result_page.upload_result(self.driver,self.log)
        self.file_list = file_list_page.file_list(self.driver,self.log)

    def share_file(self):
        self.user_login.normal_accout_login(self.user_info.user,self.user_info.password,self.user_info.except_result,self.user_info.assertion_keyword)
        sleep(0.5)
        self.home.click_myVault()
        sleep(0.5)
        self.myvault.click_shared_files_xpath()
        print("end")

    def myDriver(self):
        self.user_login.normal_accout_login(self.user_info.user,self.user_info.password,self.user_info.except_result,self.user_info.assertion_keyword)
        sleep(0.5)
        self.home.click_myVault()
        sleep(0.5)
        self.myvault.click_driver_button()
        print("end")

    def share(self):
        #print("---------- test share file in myspace ----------")
        self.log.debug("---------- test share file in myspace ----------")
        self.user_login.normal_accout_login(self.user_info.user,self.user_info.password,self.user_info.except_result,self.user_info.assertion_keyword)
        sleep(0.5)
        self.home.click_myVault()
        sleep(0.5)
        self.myvault.click_share_button()
        sleep(0.5)
        self.ready_file.click_browers_button(r"C:\upload02.exe")

        sleep(2)
        self.ready_file.click_proceed_button()

        sleep(0.5)

        self.upload_file.click_input_email_button()
        sleep(1)

        self.upload_file.select_all_rights(True)
        sleep(0.5)

        self.upload_file.click_Upload_share_File_button()

        file_name1 = self.upload_result.get_protect_file_name()
        sleep(0.5)
        self.upload_result.click_ok_button()
        sleep(1)
        file_name2 = self.file_list.get_first_fileName_list()
        if file_name1 == file_name2:
            # print("file protect and upload success")
            self.log.debug("file protect and upload success")
        else:
            # print("file protect fail")
            self.log.debug("file protect fail")
            assert False
        sleep(0.5)

        self.file_menu.click_frist_file_menu(0)
        self.file_menu.click_frist_file_menu(0)
        sleep(0.5)

        self.file_menu.click_view_file_info_icon()
        sleep(0.5)
        self.view_fileInfo.get_protect_file_actual_rights()

        # print("end")
        self.log.debug("---------- test end ----------")
        
     
            