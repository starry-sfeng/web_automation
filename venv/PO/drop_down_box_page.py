__author__ = "starry"

from PO import BaseAction
from time import sleep
from selenium.webdriver.common.by import By

class drop_down_box(BaseAction.Base):
    #drop_down_css = (By.CSS_SELECTOR,"select[class='ng-pristine ng-untouched ng-valid']")
    drop_down_css = ["css","select[class='ng-pristine ng-untouched ng-valid']"]
    Last_Modified = "//option[@label = 'Last Modified']"
    Oldest_First = "//option[@label = 'Oldest First']"
    A_Z = "//option[@label = 'A-Z']"
    Z_A = "//option[@label = 'Z-A']"
    Size_Ascending = "//option[@label = 'Size Ascending']"
    Size_Descending = "//option[@label = 'Size Descending']"

    def drop_down_elem(self):
        try:
            return self.implicit_wait(self.drop_down_css,10,0)

        except Exception as e:
            self.getScreentHot("error screen")
            self.log.debug(e)

    def option_elem(self,label_type):

        try:
            select_elem = self.drop_down_elem()
            if label_type == 0:
                elem = self.choose_option(select_elem, self.Last_Modified)
            elif label_type == 1:
                elem = self.choose_option(select_elem, self.Oldest_First)
            elif label_type == 2:
                elem = self.choose_option(select_elem, self.A_Z)
            elif label_type == 3:
                elem = self.choose_option(select_elem, self.Z_A)
            elif label_type == 4:
                elem = self.choose_option(select_elem, self.Size_Ascending)
            elif label_type == 5:
                elem = self.choose_option(select_elem, self.Size_Descending)
            else:
                self.log.debug("no find label")
                assert False
            self.click(elem)
        except Exception as e:
            self.getScreentHot("error screen")
            self.log.debug(e)


