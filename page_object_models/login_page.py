from drivers.base_element import BasePageElement
from locators.ats_locators import LoginPageLocators


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):
    """Login page action methods come here. I.e. Python.org"""

    def define_element(self):
        base_element1 = self.driver.find_element_by_xpath(LoginPageLocators.email_txt)

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""
        return "Python" in self.driver.title

    def login_to_home_page(self):
        """Login"""
        base_element1 = self.driver.find_element_by_xpath(LoginPageLocators.email_txt)
        base_element1.send_keys("abc")

        base_element2 = self.driver.find_element_by_xpath(LoginPageLocators.password_txt)
        base_element2.send_keys("abc")

        base_element = self.driver.find_element_by_xpath(LoginPageLocators.login_btn)
        base_element.click()
