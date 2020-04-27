__author__ = "satrry"

import unittest
import ddt
from operation import loginOperation
from selenium import webdriver
from operation import searchOperation
from common import launch_webdriver
from info import Logger

class searchFile(unittest.TestCase):
    def setUp(self) -> None:
        self.launch = launch_webdriver.launch_app()
        self.driver = self.launch.launch()
        self.log = Logger.Logger()
        self.logger = self.log.logger
        self.logger.debug("<------------------------------------------------------------------------------------------------------->")
        self.logger.debug("<----------------------------------------------test search file----------------------------------------->")
        self.logger.debug("<------------------------------------------------------------------------------------------------------->")
        self.search = searchOperation.search_operation(self.driver,self.logger)


    def test_search_workspace_file(self):

        try:
            self.search.search_workspace_file("ex")

        except Exception as e:
            print(e)
            assert False

    @unittest.skip(u"暂不执行")
    def test_search_myvault_file(self):

        try:
            self.search.search_myvault_file("ex")

        except Exception as e:
            print(e)
            assert False

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        self.logger.debug("<------------------------------------------------------------------------------------------------------->")
        self.logger.debug("<----------------------------------------------test end------------------------------------------------->")
        self.logger.debug("<------------------------------------------------------------------------------------------------------->")
        self.logger.debug("\n")
        self.logger.debug("\n")
        self.logger.debug("\n")
        self.logger.removeHandler(self.log.th)
        self.logger.removeHandler(self.log.sh)
        # print("-------------------- Done ----------------------- ")

if __name__ == "__main__":
    suit = unittest.TestLoader().loadTestsFromTestCase(searchFile)
    unittest.TextTestRunner(verbosity=2).run(suit)
