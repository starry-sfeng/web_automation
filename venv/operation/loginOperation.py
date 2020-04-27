from PO import loginPage
from time import sleep
from PO import BaseAction
from PO import homePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from info import Logger
class login_operation(object):
    def __init__(self,web_driver,log):
        self.driver = web_driver
        self.log = log
        self.login = loginPage.login(self.driver,self.log)
        self.home = homePage.home(self.driver,self.log)
    def normal_accout_login(self,username,password,except_result,assertion_keyword):
        try :
            if not isinstance(username, str):
                str(username)
            if not isinstance(password, str):
                str(password)
            self.log.debug("user start login")
            msg = "user login info, username: " + username + " password: " + password
            self.log.debug(msg)
            self.login.inputUserName(username)
            self.login.inputPassword(password)
            self.login.click_login_button()
            self.assert_mark(except_result,assertion_keyword)
        except Exception as e:
            self.log.debug("normal account login fail")
            self.log.debug(e)
            assert False

    def AD_account_login(self,username,password,except_result,assertion_keyword):
        try:
            if not isinstance(username,str):
                str(username)
            if not isinstance(password,str):
                str(password)
            self.log.debug("user start login")
            msg = "user login info, username: " + username + " password: " + password
            self.log.debug(msg)
            self.login.input_AD_userName(username)
            self.login.input_AD_password(password)
            self.login.click_AD_login_button()
            self.assert_mark(except_result,assertion_keyword)
        except Exception as e:
            print("AD account login fail")
            print(e)
            assert False

    def assert_mark(self,except_result,assertion_keyword):
        try:
            if except_result == "success":
                target_title = "Welcome"
                source_title = self.home.welcome()
                login_result = self.home.checkTitle(source_title.strip(), target_title.strip())
                if login_result == True:
                    self.log.debug("user login success")
                else:
                    self.log.debug("login page refresh fail")
                    assert False
            else:
                target_title = assertion_keyword
                source_title = self.login.get_msg()
                msg = "login prompt msg is: " + source_title
                self.log.debug(msg)
                login_result = self.login.checkTitle(source_title.strip(), target_title.strip())
                if login_result == True:
                    self.log.debug("user login success")
                else:
                    self.log.debug("login page refresh fail")
                    assert False
        except Exception as e:
            self.log.debug("normal account login fail")
            self.log.debug(e)
            assert False


            
    def logout(self):
        try:
            sleep(2)
            self.log.debug("click user icon success")
            self.home.click_user_icon()
            self.log.debug("click user icon success")
            self.home.click_logout()
            self.log.debug("click logout button success")
        except Exception as e:
            self.log.debug("user logout fail")
            self.log.debug(e)

    def is_login(self):
        try:
            if self.driver.find_element_by_id(self.home.welcome_id).is_displayed():
                self.log.debug("User Status: Login")
                return True
        except:
            self.log.debug("User Status: Logout")
            return False

    def is_logout(self):
        try:
            if self.driver.find_element_by_id(self.login.user_ped_id).is_displayed():
                self.log.debug("User Status: logout")
                return True
        except:
            self.log.debug("User Status: Login")
            return False



