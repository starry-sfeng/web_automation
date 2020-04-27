__author__ = "starry"

from PO import BaseAction
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class search(BaseAction.Base):
    search_css = (By.CSS_SELECTOR, "div[class^='rms-file-search' ]>form>input")

    def search_file(self,keyWord):
        try:
            elem = self.find_Element(*self.search_css)
            self.click(elem)
            self.clear(elem)
            self.send(elem,keyWord)
            sleep(2)
            self.send(elem,Keys.ENTER)

        except Exception as e:
            self.getScreentHot("error screen")
            self.log.debug(e)
