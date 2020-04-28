# coding=utf-8
__author__ = "Starry_feng"
from PO import BaseAction
from selenium.webdriver.common.by import By
from utility import Screen
class login(BaseAction.Base):
    def __init__(self):
        self.screen = Screen.screen(self.driver,self.log)

    user_name_id = (By.ID, "username")
    user_ped_id = (By.ID,"password")
    login_button_id =  (By.ID,"submit-btn")
    forget_pwd_xpth = (By.XPATH,"//div[@id=forgot-password-div]/a")
    create_new_account = (By.XPATH,"//div[@id=create-account-button-div]/a")
    ldap_username_id = (By.ID,"ldap-username")
    ldap_password_id = (By.ID,"ldap-password")
    ldap_login_button_id =(By.ID,"ldap-login-btn")
    logo_class = (By.CLASS_NAME,"logo")
    msg_id = (By.CSS_SELECTOR, "div[id=display-error]>span")


    def inputUserName(self,username):
        try:
            elem = self.find_Element(*self.user_name_id)
            self.click(elem)
            self.clear(elem)
            self.send(elem,username)
        except Exception as e:
            # self.getScreentHot("error screen")
            self.screen.getScreentHot("error screen")
            self.log.debug(e)

    def inputPassword(self,password):
        try:
            elem = self.find_Element(*self.user_ped_id)
            self.click(elem)
            self.clear(elem)
            self.send(elem, password)

        except Exception as e:
            # self.getScreentHot("error screen")
            self.screen.getScreentHot("error screen")
            self.log.debug(e)

    def click_login_button(self):
        try:
            elem = self.find_Element(*self.login_button_id)
            self.click(elem)

        except Exception as e:
            # self.getScreentHot("error screen")
            self.screen.getScreentHot("error screen")
            self.log.debug(e)


    def input_AD_userName(self,username):
        elem = self.find_Element(*self.ldap_username_id)
        self.click(elem)
        self.clear(elem)
        self.send(elem,username)

    def input_AD_password(self,password):
        elem = self.find_Element(*self.ldap_password_id)
        self.click(elem)
        self.clear(elem)
        self.send(elem,password)

    def click_AD_login_button(self):
        elem = self.find_Element(*self.ldap_login_button_id)
        self.click(elem)
        
    def get_msg(self):
        elem = self.find_Element(*self.msg_id)
        return self.getText(elem)

