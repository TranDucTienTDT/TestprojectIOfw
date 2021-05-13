import time

from seleniumpagefactory.Pagefactory import PageFactory


class LoginPage(PageFactory):

    def __init__(self, driver):
        # It is necessary to to initialise driver as page class member to implement Page Factory
        self.driver = driver

    # define locators dictionary where key name will became WebElement using PageFactory
    locators = {
        "btnChooseCountry": ('XPATH', '//div[@role="img"]'),
        "txtRegisterPhoneNumber": ('XPATH', '//input[@name="phone"]'),
        "txtRegisterEmail": ('XPATH', '//input[@name="email"]'),
        "btnLoginWithEmail": ('XPATH', '//span[text()="Login with phone"]//ancestor::button'),
        "btnLogin": ('XPATH', '//span[text()="Login"]//ancestor::button'),
        "lnkRegister": ('XPATH', '//a[contains(text(), "Register")]'),
        "btnOpenChat": ('XPATH', '//div[@role="button"]/div[@class="chat-content"]'),

    }

    def login_with_phone_number(self):
        self.txtRegisterPhoneNumber.click()
        self.txtRegisterPhoneNumber.set_text("2345678")
        time.sleep(10)
        self.btnLogin.click_button()

    def login_with_email(self):
        self.btnLoginWithEmail.click_button()
        self.txtRegisterEmail.set_text("tien1@mailinator.com")
        self.btnLogin.click_button()
