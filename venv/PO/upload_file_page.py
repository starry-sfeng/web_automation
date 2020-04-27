__author__ = "starry"

from PO import BaseAction
from selenium.webdriver.common.by import By

class upload_file(BaseAction.Base):
    #file_rights_css = ['css', 'div[class=toggle-directive]']
    # file rights button
    myvault_file_rights_css = ['css', "div[ng-show*='&']>div>div>div>div>div[class=toggle-directive]"]
    myvault_watermark_css = (By.CSS_SELECTOR,"div[ng-show*='&']>div>div>div>div>div>div[class=toggle-directive]")
    file_rights_css = ['css', "div[ng-show*='|']>div>div>div>div>div[class=toggle-directive]"]
    watermark_css = (By.CSS_SELECTOR,"div[ng-show*='|']>div>div>div>div>div>div[class=toggle-directive]")
    input_Email_id = (By.XPATH, "//ul[@id='mailShareTagsModal']/li/input")
    create_File_and_share_xpath = (By.XPATH, "//div[@data-ng-show='!success']/button[2]")
    upload_css = (By.XPATH,"//div[@data-ng-show='!success']/button[3]")


    def select_print_right(self,is_myvault):
        try:
            self.log.debug("give file print right")
            if is_myvault:
                elem = self.findElement2(self.myvault_file_rights_css, 0)
                self.click(elem)
            else:
                elem = self.findElement2(self.file_rights_css, 0)
                self.click(elem)

        except Exception as e:
            self.getScreentHot("error screen.jpg")
            self.log.debug(e)



    def select_ReShare_right(self,is_myvault):
        try:
            self.log.debug("give file reshare right")
            if is_myvault:
                elem = self.findElement2(self.myvault_file_rights_css, 1)
                self.click(elem)
            else:
                elem = self.findElement2(self.file_rights_css, 1)
                self.click(elem)

        except Exception as e:
            self.getScreentHot("error screen.jpg")
            self.log.debug(e)


    def select_SaveAs_right(self, is_myvault):
        try:
            self.log.debug("give file save as right")
            if is_myvault:
                elem = self.findElement2(self.myvault_file_rights_css, 2)
                self.click(elem)
            else:
                elem = self.findElement2(self.file_rights_css, 2)
                self.click(elem)

        except Exception as e:
            self.getScreentHot("error screen.jpg")
            self.log.debug(e)


    def select_Edit_right(self, is_myvault):
        try:
            self.log.debug("give file edit right")
            if is_myvault:
                elem = self.findElement2(self.myvault_file_rights_css, 3)
                self.click(elem)
            else:
                elem = self.findElement2(self.file_rights_css, 3)
                self.click(elem)

        except Exception as e:
            self.getScreentHot("error screen.jpg")
            self.log.debug(e)


    def select_watermark_right(self, is_myvault):
        try:
            self.log.debug("give file watermark right")
            if is_myvault:
                elem = self.find_Element(*self.myvault_watermark_css)
                self.click(elem)
            else:
                elem = self.find_Element(*self.watermark_css)
                self.click(elem)

        except Exception as e:
            self.getScreentHot("error screen.jpg")
            self.log.debug(e)


    def select_all_rights(self,is_myvault):
        self.select_Edit_right(is_myvault)
        self.select_print_right(is_myvault)
        self.select_ReShare_right(is_myvault)
        self.select_SaveAs_right(is_myvault)
        self.select_watermark_right(is_myvault)

    def click_input_email_button(self):
        try:
            self.log.debug("input user email")
            elem = self.find_Element(*self.input_Email_id)
            self.click(elem)
            self.clear(elem)
            self.send(elem, "john.tyler@qapf1.qalab01.nextlabs.com")

        except Exception as e:
            self.getScreentHot("error screen")
            self.log.debug(e)


    def click_Upload_share_File_button(self):
        try:
            self.log.debug("upload & share file")
            elem = self.find_Element(*self.create_File_and_share_xpath)
            self.click(elem)

        except Exception as e:
            self.getScreentHot("error screen")
            self.log.debug(e)


    def click_upload_button(self):
        try:
            self.log.debug("click to upload file")
            elem = self.find_Element(*self.upload_css)
            self.click(elem)

        except Exception as e:
            self.getScreentHot("error screen")
            self.log.debug(e)


