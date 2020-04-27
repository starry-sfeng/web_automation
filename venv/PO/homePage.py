# coding=utf-8
__author__ = "Starry_feng"
from PO import BaseAction
from selenium.webdriver.common.by import By

class home(BaseAction.Base):
    
    myVault_xpath= (By.XPATH,"//div[@id='myvault-btn']/div/div[2]/button")
    user_icon_css = (By.CSS_SELECTOR,"button[class='btn dropdown-toggle']")
    logout_css = (By.CSS_SELECTOR,"a[data-ng-click='doLogout()']")
    welcome_id = ["id","welcome"]
    workspace_css = (By.CSS_SELECTOR,"button[data-ng-click*='workspace_files']")


    def click_myVault(self):
        # print("------welcome to myvault------")
        try:
            self.log.debug("------welcome to myvault------")
            elem = self.find_Element(*self.myVault_xpath)
            self.click(elem)
        except Exception as e:
            self.getScreentHot("error screen")
            self.log.debug(e)

    def click_workspace(self):
        # print("------welcome to worksapce------")
        try:
            self.log.debug("------welcome to worksapce------")
            elem = self.find_Element(*self.workspace_css)
            self.click(elem)
        except Exception as e:
            self.getScreentHot("error screen")
            self.log.debug(e)

    def click_user_icon(self):
        try:
            elem = self.find_Element(*self.user_icon_css)
            self.click(elem)
        except Exception as e:
            self.getScreentHot("error screen")
            self.log.debug(e)

    def click_logout(self):
        try:
            elem = self.find_Element(*self.logout_css)
            self.click(elem)
        except Exception as e:
            self.getScreentHot("error screen")
            self.log.debug(e)

    def welcome(self):
        try:
            elem = self.implicit_wait(self.welcome_id,10,0)
            return  self.getText(elem)
        except UnboundLocalError as e:
            self.log.debug(e)
            self.getScreentHot("error screen")
            assert False
        except Exception as e:
            self.log.debug(e)
            self.getScreentHot("error screen")
            assert False
