# -*- coding: utf-8 -*-
from time import sleep
from model.data import Data


class Check:
    def __init__(self, fix):
        self.fix = fix

    def check_profile(self, user):
        browser = self.fix.driver
        text2 = browser.find_element_by_css_selector(".ng-binding").text
        assert str(text2) == user.username, "Имена равны"

    def create_amount(self, amount):
        browser = self.fix.driver
        sleep(4)
        browser.find_element_by_xpath("//button[contains(.,'Deposit')]").click()
        sleep(4)
        browser.find_element_by_xpath("//input[@type='number']").click()
        browser.find_element_by_xpath("//input[@type='number']").send_keys(amount.amount)
        browser.find_element_by_xpath("//form/button").click()
        sleep(7)
        self.cache_get = None

    cache_get = None

    def get_list(self):
        if self.cache_get is None:
            browser = self.fix.driver
            self.cache_get = []
            browser.find_element_by_xpath("//button[contains(.,'Transactions')]").click()
            sleep(5)
            for element in browser.find_elements_by_css_selector("tr.ng-scope"):
                id_number = element.get_attribute("id")
                self.cache_get.append(Data(id=id_number))
            sleep(4)
            browser.find_element_by_xpath("//button[contains(.,'Back')]").click()
        return list(self.cache_get)
