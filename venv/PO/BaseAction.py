# coding=utf-8
__author__ = "Starry_feng"
from common import launch_webdriver
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from utility import Screen
class Base(object):

    def __init__(self,web_driver,log):
        self.driver= web_driver
        self.log = log
        self.screen = Screen.screen(self.driver,self.log)

    def implicit_wait(self, element,time,index):
        try:
            type = element[0].lower()
            value = element[1]

            if type == 'id':
                elem = WebDriverWait(self.driver,time).until(lambda driver : driver.find_element_by_id(value))
                #elem = self.driver.find_element_by_id(value)
            elif type == "name":
                elem = WebDriverWait(self.driver, time).until(lambda driver: driver.find_element_by_name(value))
                #elem = self.driver.find_element_by_name(value)
            elif type == "class":
                elem = WebDriverWait(self.driver, time).until(lambda driver: driver.find_element_by_class_name(value))
                #elem = self.driver.find_element_by_class_name(value)
            elif type =="link_text":
                elem = WebDriverWait(self.driver, time).until(lambda driver: driver.find_element_link_text(value))
                #elem = self.driver.find_element_by_link_text(value)
            elif type =="xpath":
                elem = WebDriverWait(self.driver, time).until(lambda driver: driver.find_element_by_xpath(value))
                #elem = self.driver.find_element_by_xpath(value)
            elif type == "css":
                elem = WebDriverWait(self.driver, time).until(lambda driver: driver.find_elements_by_css_selector(value)).pop(index)
                #elem = self.driver.find_elements_by_css_selector(value)
            elif type == "tag_name":
                elem = WebDriverWait(self.driver, time).until(lambda driver: driver.find_element_by_tag_name(value))
                #elem = self.driver.find_element_by_tag_name(value)
            else:
                raise NameError (" type is error")
                assert False
        except Exception as e:
            # print("no find label",element)
            msg = "no find label " + element[1]
            self.log.debug(msg)
            self.log.debug(e)
        return elem

    def findElement2(self, element,index):
        try:
            type = element[0].lower()
            value = element[1]

            if type == "css":
                elem = self.driver.find_elements_by_css_selector(value).pop(index)

            else:
                raise NameError (" type is error")
                assert False
        except Exception as e:
            print("id  %s has no find, please chece it" % (id))
            self.log.debug(e)
        return elem

    def elements_number(self,element):

        elem = self.driver.find_elements_by_css_selector(element)
        print("elements number is: ",len(elem))
        return len(elem)

    def find_Element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except Exception as e:
            print( u"%s can not find this element %s element" % (self, loc))
            self.log.debug(e)

    def choose_option(self,select_elem,label):
        return select_elem.find_element_by_xpath(label)

    def alert_operation(self,operation):
        alert = self.driver.switch_to_alert()
        if operation ==1:
            alert.accept()
        elif operation ==2:
            alert:dismiss()
        elif operation==3:
            return  alert.text()
        else:
            # print("have a error in alert")
            self.log.debug("input operation incorrect in alert")
            assert False

    def open(self,url):
        try:
            if url.strip() !="":
                self.driver.get(url)
            else:
                raise ValueError("url is null")
                assert False
        except Exception as e:
            self.log.debug(e)

    def send(self,elem,send_value):
        try:
            elem.send_keys(send_value)
        except Exception as e:
            self.log.debug(e)
            assert False

    def click(self,elem):
        try:
            elem.click()
        except Exception as e:
            self.log.debug(e)
            assert False

    def clear(self,elem):
        try:
            elem.clear()
        except Exception as e:
            self.log.debug(e)
            assert False

    def quit1(self):
        try:
            self.driver.quit()
        except Exception as e:
            self.log.debug(e)
            assert False

    def getAtrribute(self,elem,attribute):
        try:
            return elem.get_attribute(attribute)
        except Exception as e:
            self.log.debug(e)
            assert False

    def getText(self,elem):
        try:
            return elem.text
        except Exception as e:
            self.log.debug(e)
            assert False

    def getTitle(self):
        try:
            return self.driver.title
        except Exception as e:
            self.log.debug(e)
            assert False

    def getCurrentUrl(self):
        try:
            return self.driver.current_url
        except Exception as e:
            self.log.debug(e)
            assert False

    # def getScreentHot(self,file_name):
    #     try:
    #         folder = "../testCase/scrren/"
    #         path = folder + file_name+ str(time.time()) +".png"
    #         log = "screen path is: "+ path
    #         self.log.debug(log)
    #         if os.path.exists(folder):
    #             self.driver.get_screenshot_as_file(path)
    #
    #         else:
    #             os.makedirs(folder)
    #             self.driver.get_screenshot_as_file(path)
    #
    #     except Exception as e:
    #         self.log.debug(e)
    #         assert False

    def maximizeWindow(self):
        try:
            self.driver.maximize_window()
        except Exception as e:
            self.log.debug(e)
            assert False

    def back(self):
        try:
            self.driver.back()
        except Exception as e:
            self.log.debug(e)
            assert False

    def forward(self):
        try:
            self.driver.forward()
        except Exception as e:
            self.log.debug(e)
            assert False
    def refreash(self):
        try:
            self.driver.refresh()
        except Exception as e:
            self.log.debug(e)
            assert False

    def windowSize(self):
        try:
            self.driver.get_window_size()
        except Exception as e:
            self.log.debug(e)
            assert False

    def checkTitle(self,source_title, target_title):
        if  source_title.lower() == target_title.lower():
            return True
        else:
            self.screen.getScreentHot("error screen")
            return False
            assert False































