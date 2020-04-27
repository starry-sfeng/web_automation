__author__ = "starry"

from PO import BaseAction
from selenium.webdriver.common.by import By
from time import sleep

class upload_result(BaseAction.Base):
    protect_file_name_css = (By.CSS_SELECTOR, "span[class^='rms']>b[class= 'ng-binding']")
    protect_file_name_css1 = ["css", "span[class^='rms']>b[class= 'ng-binding']"]
    protect_file_name_xpath = ["xpath", "//span[@class='rms-files color-light-blue inline-block']/b[@class= 'ng-binding']"]
    ok_button_css = (By.CSS_SELECTOR, "button[type=button][class*=color][data-ng-click='ok()']")
    workspace_getFile_name_css = (By.CSS_SELECTOR,"[id = rms-snackbar]>div")

    def get_protect_file_name(self):
        try:
            self.log.debug("get create file name")
            elem = self.implicit_wait(self.protect_file_name_css1,10,0)
            protect_file_name =  self.getText(elem)
            print("create protect file name is: ",protect_file_name)
            return protect_file_name

        except Exception as e:
            self.getScreentHot("error screen")
            self.log.debug(e)

    def workSpace_get_protect_file_name(self):
        try:
            self.log.debug("get create file name")
            elem= self.find_Element(*self.workspace_getFile_name_css)
            protect_file_name =  self.getText(elem)
            print("create protect file name is: ",protect_file_name)
            return protect_file_name

        except Exception as e:
            self.getScreentHot("error screen")
            self.log.debug(e)

    def click_ok_button(self):
        try:
            elem = self.find_Element(*self.ok_button_css)
            self.click(elem)

        except Exception as e:
            self.getScreentHot("error screen")
            self.log.debug(e)
