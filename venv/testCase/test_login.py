# coding=utf-8
__author__ = "Starry_feng"
from PO import loginPage
from operation import loginOperation
from selenium import webdriver
from common import launch_webdriver
from info import userInfo,Logger
from utility import excel
import unittest
import ddt
import os

PATH = lambda p: os.path.abspath(p)
path = PATH(os.getcwd())
print(path)
normal_user = excel.ExcelUtil(path + r'\Data\case_login.xls', 'normal_accout_login')
AD_user = excel.ExcelUtil(path + r'\Data\case_login.xls', 'AD_account_login')
@ddt.ddt
class user_login(unittest.TestCase):
    
    def setUp(self):

        self.launch = launch_webdriver.launch_app()
        self.driver = self.launch.launch()
        self.log = Logger.Logger()
        self.logger = self.log.logger
        self.logger.debug(
            "<------------------------------------------------------------------------------------------------------->")
        self.logger.debug(
            "<-----------------------------------------------test start---------------------------------------------->")
        self.logger.debug(
            "<------------------------------------------------------------------------------------------------------->")
        self.login_Operation = loginOperation.login_operation(self.driver,self.logger)

    @ddt.data(*normal_user.next())
    def test_normal_account_login(self,data):
        try:

            user_name = data['username']
            password = data['password']
            except_result = data['except_result']
            assertion_keyword =  data['assertion_keyword']
            run = data['run']
            if run.strip() == 'y':
                if self.login_Operation.is_login():
                    self.login_Operation.logout()
                self.login_Operation.normal_accout_login(user_name, password,except_result,assertion_keyword)
            else:
                try:
                    self.logger.debug("skip this case")
                    exit(0)
                except SystemExit as e:
                    print(e)
        except Exception as e:
            self.logger.debug(e)
            assert False

        finally:

            self.logger.debug(
                "<------------------------------------------------------------------------------------------------------->")
            self.logger.debug(
                "<---------------------------------------test normal account end----------------------------------------->")
            self.logger.debug(
                "<------------------------------------------------------------------------------------------------------->")
            self.logger.debug("\n")
            self.logger.debug("\n")
            self.logger.debug("\n")
            self.logger.removeHandler(self.log.th)
            self.logger.removeHandler(self.log.sh)

    @ddt.data(*AD_user.next())
    @unittest.skip(u"暂不执行")
    def test_AD_account_login(self,data):
        try:

            user_name = data['username']
            password = data['password']
            except_result = data['except_result']
            assertion_keyword = data['assertion_keyword']
            run = data['run']
            if run.strip() == 'y':
                if self.login_Operation.is_login():
                    self.login_Operation.logout()
                self.login_Operation.AD_account_login(user_name, password, except_result, assertion_keyword)
            else:
                try:
                    exit(0)
                except SystemExit as e:
                    print(e)

        except Exception as e:
            self.logger.debug(e)
            assert False

        finally:
            self.logger.debug(
                "<------------------------------------------------------------------------------------------------------->")
            self.logger.debug(
                "<-----------------------------------------test ad account end------------------------------------------->")
            self.logger.debug(
                "<------------------------------------------------------------------------------------------------------->")
            self.logger.debug("\n")
            self.logger.debug("\n")
            self.logger.debug("\n")
            self.logger.removeHandler(self.log.th)
            self.logger.removeHandler(self.log.sh)

            
    '''            
    def asset_login(self):
        self.driver = webdriver.Chrome(r"C:\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://rms-centos7513.qapf1.qalab01.nextlabs.com:8444/rms/main#/home");
        self.text =  self.driver.find_element_by_xpath("//div[@id='footer']/div/p").text
        print(self.text)
    #def tearDown(self) -> None:
    '''     
    
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
    
if __name__ == '__main__':
    suit = unittest.TestLoader().loadTestsFromTestCase(user_login)
    unittest.TextTestRunner(verbosity=2).run(suit)