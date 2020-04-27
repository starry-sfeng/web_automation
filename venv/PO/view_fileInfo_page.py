__author__ = "starry"
from PO import BaseAction
from selenium.webdriver.common.by import By

class view_file_info(BaseAction.Base):
    rights_list_css = "li>div>h6[class='ng-binding']"
    rights_list_css1 = ["css","li>div>h6[class='ng-binding']"]
    def rights_numbers(self):
        number = self.elements_number(self.rights_list_css)
        print("rights number is:",number)
        return number

    def get_protect_file_actual_rights(self):
        number = self.rights_numbers()
        rights = []
        i = 0
        while i < number:
            elem = self.findElement2(self.rights_list_css1,i)
            text = self.getText(elem)
            rights.append(text)
            i = i + 1

        print(rights)

