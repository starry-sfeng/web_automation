__author__ = "starry"

from PO import BaseAction
from selenium.webdriver.common.by import By
from time import sleep
from info import Logger
import os

class ready_file(BaseAction.Base):
    browers_css = (By.CSS_SELECTOR, "a[ng-model= 'files']")
    proceed_css = (By.CSS_SELECTOR, "button[data-ng-click*=proceed]")

    def click_browers_button(self, file_url):
        try:
            elem = self.find_Element(*self.browers_css)
            self.click(elem)
            sleep(0.5)
            self.log.debug("ready share file")
            self.log.debug("file is loading")
            result = os.system(file_url)
            if result == 0:
                self.log.debug("file loading success")
            else:
                self.log.debug("file loading fail")
                assert False

        except Exception as e:
            self.getScreentHot("error screen.jpg")
            self.log.debug(e)

    def click_proceed_button(self):
        try:
            elem = self.find_Element(*self.proceed_css)
            self.click(elem)

        except Exception as e:
            self.getScreentHot("error screen")
            self.log.debug(e)
