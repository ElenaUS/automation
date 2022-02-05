
class Page:
    def __init__(browser, fix, driver):
        browser.fix = fix
        browser.driver = driver

    def find_element(browser, *locator):
        return browser.fix.driver.find_element(*locator)

    def find_elements(browser, *locator):
        return browser.fix.driver.find_elements(*locator)

    def click(browser, *locator):
        e = browser.fix.driver.find_element(*locator)
        e.click()

    def input(browser, text, *locator):
        e = browser.fix.driver.find_element(*locator)
        e.click()
        e.send_keys(text)
