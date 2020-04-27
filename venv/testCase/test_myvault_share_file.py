__author__ = "Starry.feng"

import unittest
import ddt
from operation import loginOperation
from selenium import webdriver
from operation import myvaultOperation
from common import launch_webdriver
from info import Logger

class Myvalut_Share(unittest.TestCase):

    def setUp(self) -> None:
        self.launch = launch_webdriver.launch_app()
        self.driver = self.launch.launch()
        self.log = Logger.Logger()
        self.logger = self.log.logger
        self.logger.debug(
            "<------------------------------------------------------------------------------------------------------->")
        self.logger.debug(
            "<---------------------------------------------test myvault_share_file----------------------------------->")
        self.logger.debug(
            "<------------------------------------------------------------------------------------------------------->")
        self.myvault = myvaultOperation.myvault_operation(self.driver,self.logger)

    @unittest.skip(u"暂不执行")
    def test_shareMyvaultFile(self):

        try:
            self.myvault.share_file()

        except Exception as e:
            print(e)
            assert False

    @unittest.skip(u"暂不执行")
    def test_myDriver(self):
        try:
            self.myvault.myDriver()

        except Exception as e:
            print(e)
            assert False

    def test_share(self):
        try:
            self.myvault.share()

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
    suit = unittest.TestLoader().loadTestsFromTestCase(Myvalut_Share)
    unittest.TextTestRunner(verbosity=2).run(suit)