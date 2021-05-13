from seleniumpagefactory.Pagefactory import PageFactory


class OtpVerifyPage(PageFactory):

    def __init__(self, driver):
        # It is necessary to to initialise driver as page class member to implement Page Factory
        self.driver = driver

    locators= {
        "txtOTP": ('XPATH', '//div[@class="digit-input"]/div/div')
    }

    def input_otp(self):
        self.txtOTP.set_text("1")

    def resent_opt(self):
        pass