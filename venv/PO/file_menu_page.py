__author__ = "starry"

from PO import BaseAction
from selenium.webdriver.common.by import By
from utility import Screen

class file_menu(BaseAction.Base):
    def __init__(self, web_driver, log):
        self.driver = web_driver
        self.log = log
        self.screen = Screen.screen(self.driver,self.log)
    file_menu_css = ['css', "a[title='Menu']"]
    view_file_info_icon_css =(By.CSS_SELECTOR,"a[title = 'View File Info']")
    view_file_icon_css =(By.CSS_SELECTOR,"a[title = 'View file']")
    view_activity_icon_css = (By.CSS_SELECTOR, "a[title = 'View Activity']")
    share_file_icon_css = (By.CSS_SELECTOR, "a[title = 'Share File'][class$='ng-scope']")
    download_file_icon_css = (By.CSS_SELECTOR, "a[title = 'Download File']")
    extract_content_icon_css = (By.CSS_SELECTOR, "a[title = 'Extract Content']")
    delete_icon_css = (By.CSS_SELECTOR, "a[title = 'Delete']")
    modify_rights_icon_css = (By.CSS_SELECTOR, "a[title = 'Modify Rights']")

    def click_file_menu(self,file_index):

        try:
            self.log.debug("click file menu")
            elem = self.implicit_wait(self.file_menu_css,10,file_index)
            self.click(elem)
        except Exception as e:
            # self.getScreentHot("error screen")
            self.screen.getScreentHot("error screen")
            self.log.debug(e)

    def click_view_file_icon(self):
        try:
            self.log.debug("click view file icon")
            elem = self.find_Element(*self.view_file_icon_css)
            self.click(elem)

        except Exception as e:
            # self.getScreentHot("error screen")
            self.screen.getScreentHot("error screen")
            self.log.debug(e)

    def click_view_file_info_icon(self):
        try:
            self.log.debug("click view file info icon")
            elem = self.find_Element(*self.view_file_info_icon_css)
            self.click(elem)

        except Exception as e:
            # self.getScreentHot("error screen")
            self.screen.getScreentHot("error screen")
            self.log.debug(e)

    def click_view_activity_icon(self):
        try:
            self.log.debug("click view activity icon")
            elem = self.find_Element(*self.view_activity_icon_css)
            self.click(elem)
        except Exception as e:
            # self.getScreentHot("error screen")
            self.screen.getScreentHot("error screen")
            self.log.debug(e)

    def click_share_file_icon(self):
        try:
            self.log.debug("click share icon")
            elem = self.find_Element(*self.share_file_icon_css)
            self.click(elem)
        except Exception as e:
            # self.getScreentHot("error screen")
            self.screen.getScreentHot("error screen")
            self.log.debug(e)

    def click_download_icon(self):
        try:
            self.log.debug("click download icon")
            elem = self.find_Element(*self.download_file_icon_css)
            self.click(elem)
        except Exception as e:
            # self.getScreentHot("error screen")
            self.screen.getScreentHot("error screen")
            self.log.debug(e)

    def click_extract_icon(self):
        try:
            self.log.debug("click extract icon")
            elem = self.find_Element(*self.extract_content_icon_css)
            self.click(elem)
        except Exception as e:
            # self.getScreentHot("error screen")
            self.screen.getScreentHot("error screen")
            self.log.debug(e)

    def click_delete_icon(self):
        try:
            self.log.debug("click delete icon")
            elem = self.find_Element(*self.download_file_icon_css)
            self.click(elem)
        except Exception as e:
            # self.getScreentHot("error screen")
            self.screen.getScreentHot("error screen")
            self.log.debug(e)

    def click_modify_icon(self):
        try:
            self.log.debug("click modify icon")
            elem = self.find_Element(*self.modify_rights_icon_css)
            self.click(elem)
        except Exception as e:
            # self.getScreentHot("error screen")
            self.screen.getScreentHot("error screen")
            self.log.debug(e)
