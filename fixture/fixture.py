# -*- coding: utf-8 -*-
from selenium import webdriver
from fixture.session import Session
from fixture.check_profile import Check


class Fixture:
    def __init__(self, base_url, browser="Safari"):
        if browser == "Safari":
            self.driver = webdriver.Safari()
        elif browser == "Chrome":
            self.driver = webdriver.Chrome()
        elif browser == "Firefox":
            self.driver = webdriver.Firefox()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        browser = self.driver
        browser.implicitly_wait(10)
        browser.base_url = base_url
        self.session = Session(self)
        self.check = Check(self)
        browser.maximize_window()
        browser.delete_all_cookies()

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def open_home_page(self):
        browser = self.driver
        browser.get(browser.base_url)

    def destroy(self):
        self.driver.quit()
