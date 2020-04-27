__author__ = "starry"

import unittest
import ddt
from operation import loginOperation
from selenium import webdriver
from operation import workspaceOperation
from common import launch_webdriver
from info import Logger

class workSpace_protect(unittest.TestCase):
    def setUp(self) -> None:
        self.launch = launch_webdriver.launch_app()
        self.driver = self.launch.launch()
        self.log = Logger.Logger()
        self.logger = self.log.logger
        self.logger.debug(
            "<------------------------------------------------------------------------------------------------------->")
        self.logger.debug(
            "<---------------------------------------test workspace_protect_file------------------------------------->")
        self.logger.debug(
            "<------------------------------------------------------------------------------------------------------->")
        self.workspace = workspaceOperation.workspace_operation(self.driver,self.logger)
    @unittest.skip(u"case 未完成")
    def test_workSpace_protect_File(self):

        try:
            self.workspace.workspace_protect_file()

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
        self.logger.removeHandler(self.log.sh)
        self.logger.removeHandler(self.log.th)
        # print("-------------------- Done ----------------------- ")

if __name__ == "__main__":
    suit = unittest.TestLoader().loadTestsFromTestCase(workSpace_protect)
    unittest.TextTestRunner(verbosity=2).run(suit)