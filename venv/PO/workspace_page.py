__author__ = "starry"

from PO import BaseAction
from selenium.webdriver.common.by import By

class workSpace(BaseAction.Base):
    upload_css = (By.CSS_SELECTOR, "img[uib-tooltip='Upload File to WorkSpace']")


    def click_upload_button(self):
        try:
            elem = self.find_Element(*self.upload_css)
            self.click(elem)

        except Exception as e:
            self.getScreentHot("error screen")
            self.log.debug(e)


