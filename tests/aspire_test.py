import unittest
#from selenium import webdriver
from src.testproject.sdk.drivers import webdriver
from page_object_models import aspire_login_page, aspire_otp_verify_page, aspire_information_needed_page


class HelloWorld(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome(token='8bh04dldZkEQBaX8RL6-T3Fid2oFWQVaqzD8NmVI_HE', project_name='b', job_name='')
        self.driver.get("https://feature-qa.customer-frontend.staging.aspireapp.com/sg/login")

    def test_login_to_ats(self):
        login_page = aspire_login_page.LoginPage(self.driver)
        login_page.login_with_phone_number()


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()