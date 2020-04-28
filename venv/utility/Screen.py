__author__ = "Starry"
import os
import time
class screen(object):

    def __init__(self,web_driver,logger):
        self.driver = web_driver
        self.log = logger

    def getScreentHot(self,file_name):
        try:
            folder = "../testCase/scrren/"
            path = folder + file_name+ str(time.time()) +".png"
            log = "screen path is: "+ path
            self.log.debug(log)
            if os.path.exists(folder):
                self.driver.get_screenshot_as_file(path)

            else:
                os.makedirs(folder)
                self.driver.get_screenshot_as_file(path)

        except Exception as e:
            self.log.debug(e)
            assert False