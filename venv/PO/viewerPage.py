__author__ = "starry"

from PO import BaseAction

class viewer(BaseAction.Base):

    def switch_driver(self,current_window):
        all_windows = self.all_windows()
        print(self.getCurrentUrl())
        cooks =self.driver.get_cookies()
        print(cooks)
        print(current_window)
        print(all_windows)
        print(1111)

