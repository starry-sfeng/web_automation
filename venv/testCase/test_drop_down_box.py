__author__ = "satrry"

import unittest
import ddt
from operation import loginOperation
from selenium import webdriver
from operation import drop_down_operation
from common import launch_webdriver
from info import Logger

class order_by(unittest.TestCase):
    def setUp(self) -> None:
        self.launch = launch_webdriver.launch_app()
        self.driver = self.launch.launch()
        self.log = Logger.Logger()
        self.logger = self.log.logger
        self.logger.debug(
            "<------------------------------------------------------------------------------------------------------->")
        self.logger.debug(
            "<----------------------------------------------test drop_down_box--------------------------------------->")
        self.logger.debug(
            "<------------------------------------------------------------------------------------------------------->")
        self.order = drop_down_operation.drop_down(self.driver,self.logger)

    def test_myvault_sort_file(self):

        try:
            self.order.myvault_choose_drop_dwon(2)

        except Exception as e:
            print(e)
            assert False

    @unittest.skip(u"暂不执行")
    def test_workspace_sort_file(self):

        try:
            self.order.workspace_choose_drop_dwon(2)

        except Exception as e:
            print(e)
            assert False

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        self.logger.debug(
            "<------------------------------------------------------------------------------------------------------->")
        self.logger.debug(
            "<----------------------------------------------test end------------------------------------------------->")
        self.logger.debug(
            "<------------------------------------------------------------------------------------------------------->")
        self.logger.debug("\n")
        self.logger.debug("\n")
        self.logger.debug("\n")
        self.logger.removeHandler(self.log.th)
        self.logger.removeHandler(self.log.sh)
        # print("-------------------- Done ----------------------- ")


if __name__ == "__main__":
    suit = unittest.TestLoader().loadTestsFromTestCase(order_by)
    unittest.TextTestRunner(verbosity=2).run(suit)