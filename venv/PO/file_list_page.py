__author__ = "starry"

from PO import BaseAction
from selenium.webdriver.common.by import By
from time import sleep
from utility import Screen

class file_list(BaseAction.Base):
    def __init__(self):
        self.screen = Screen.screen(self.driver,self.log)
    first_fileName_list_xpath = (By.XPATH, "//li[@class='list-group-item rms-file-list ng-scope'][1]/div/div/div/div/a")
    first_fileName_list_xpath1 = ["xpath", "//li[@class='list-group-item rms-file-list ng-scope'][1]/div/div/div/div/a"]

    def get_first_fileName_list(self):

        try:
            elem = self.find_Element(*self.first_fileName_list_xpath)
            #elem = self.implicit_wait(self.first_fileName_list_xpath1,15,0)
            file_Name = self.getText(elem)
            print("file name is:",file_Name)
            return file_Name

        except Exception as e:
            # self.getScreentHot("error screen")
            self.screen.getScreentHot("error screen")
            self.log.debug(e)
