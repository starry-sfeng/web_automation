# coding=utf-8
__author__ = "Starry_feng"
from selenium import webdriver
from time import sleep
from info import userInfo

class launch_app:
    def __init__(self):
        self.driver_location = r'C:\chromedriver_win32\chromedriver.exe'
        self.info = userInfo.user()
        self.url = self.info.server
    def launch(self):
        print(self.driver_location)
        print(self.url)
        self.driver = webdriver.Chrome(self.driver_location)
        self.driver.maximize_window()
        self.driver.get(self.url)
        title = self.driver.title
        if title != "SkyDRM":
            self.driver.find_element_by_id("details-button").click()
            sleep(0.5)
            self.driver.find_element_by_id("proceed-link").click()
        for i in range(60):

            print(self.driver.title)
            login_title = self.driver.title
            if login_title == "SkyDRM":
                print("ok")
            break

            sleep(0.5)
        return self.driver


