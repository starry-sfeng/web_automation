__author__ = "starry"

from PO import BaseAction,file_menu_page
from selenium.webdriver.common.by import By
from time import sleep
from utility import Screen

class file_list(BaseAction.Base):
    def __init__(self, web_driver, log):
        self.driver = web_driver
        self.log = log
        self.file_menu = file_menu_page.file_menu(self.driver,self.log)
        self.screen = Screen.screen(self.driver,self.log)
    first_fileName_list_xpath = (By.XPATH, "//li[@class='list-group-item rms-file-list ng-scope'][1]/div/div/div/div/a")
    first_fileName_list_xpath1 = ["xpath", "//li[@class='list-group-item rms-file-list ng-scope'][1]/div/div/div/div/a"]
    file_list_css = "li[class='list-group-item rms-file-list ng-scope']>div>div>div>div>a"
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

    def get_all_file(self):
        elems = self.css_elements(self.file_list_css)
        return elems

    def find_myault_file_index(self,fileName):

        elems = self.get_all_file()
        i = 0
        for elem in elems:
            i = i+1
            if self.getText(elem) == fileName:
                return i

    def open_myvault_file(self,fileName):
        current_window = self.current_window()
        index = self.find_myault_file_index(fileName)
        self.file_menu.click_file_menu(index)
        sleep(0.5)
        self.file_menu.click_file_menu(index)
        sleep(0.5)
        self.file_menu.click_view_file_icon()
        return current_window

