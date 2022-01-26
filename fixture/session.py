from time import sleep
from selenium.webdriver.support.select import Select


class Session:
    def __init__(self, fix):
        self.fix = fix

    def login(self, username):
        browser = self.fix.driver
        self.fix.open_home_page()
        browser.find_element_by_id("userSelect").click()
        select = Select(browser.find_element_by_id('userSelect'))
        select.select_by_visible_text(username)
        browser.find_element_by_css_selector(".btn-default").click()
        sleep(5)

    def logout(self):
        browser = self.fix.driver
        browser.find_element_by_css_selector("button.logout").click()

    def is_logged_in(self):
        browser = self.fix.driver
        return len(browser.find_elements_by_css_selector("button.logout")) > 0

    def is_logged_in_as(self, username):
        browser = self.fix.driver
        return browser.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/strong/span").text == username

    def ensure_login(self, username):
        browser = self.fix.driver
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username)

    def ensure_logout(self):
        browser = self.fix.driver
        if self.is_logged_in():
            self.logout()
