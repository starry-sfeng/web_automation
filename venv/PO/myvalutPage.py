__author__ = "Starry.feng"

from PO import BaseAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class myvalut(BaseAction.Base):

    myvault_class_name = (By.CLASS_NAME,"menu-label ng-binding color-green")
    driver_css = (By.CSS_SELECTOR,"a[class='cc-pc-menu-item'][data-ng-click*='0']")
    all_files_xpath = (By.XPATH,"//div[@id='repo-list-menu-id']/uib-accordion/div")
    shared_files_xapth = (By.XPATH,"//div[@id='repo-list-menu-id']/div[1]")
    share_css = (By.CSS_SELECTOR,"a[data-ng-click='openShareWidget()']")


    def click_myvault_button(self):
        try:
            elem = self.find_Element(*self.myvault_class_name)
            self.click(elem)
        except Exception as e:
            self.getScreentHot("error screen")
            self.log.debug(e)

    def click_driver_button(self):
        try:
            elem = self.find_Element(*self.driver_css)
            self.click(elem)
        except Exception as e:
            self.getScreentHot("error screen")
            self.log.debug(e)

    def click_all_files_button(self):
        try:
            elem = self.find_Element(*self.all_files_xpath)
            self.click(elem)
        except Exception as e:
            self.getScreentHot("error screen")
            self.log.debug(e)

    def click_shared_files_xpath(self):
        try:
            elem = self.find_Element(*self.shared_files_xapth)
            self.click(elem)

        except Exception as e:
            self.getScreentHot("error screen")
            self.log.debug(e)

    def click_share_button(self):
        try:
            elem = self.find_Element(*self.share_css)
            self.click(elem)

        except Exception as e:
            self.getScreentHot("error screen")
            self.log.debug(e)











