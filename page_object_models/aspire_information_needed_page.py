from seleniumpagefactory.Pagefactory import PageFactory


class InformationNeededPage(PageFactory):

    def __init__(self, driver):
        # It is necessary to to initialise driver as page class member to implement Page Factory
        self.driver = driver

    locators= {
        "btnGetStarted": ('XPATH', '//span[text()="Get Started"]//ancestor::button')
    }

    def open_get_started_page(self):
        self.btnGetStarted.click_button()
