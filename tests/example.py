import unittest
#from selenium import webdriver
from src.testproject.sdk.drivers import webdriver
import page_object_models.login_page


class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome(token='8bh04dldZkEQBaX8RL6-T3Fid2oFWQVaqzD8NmVI_HE', project_name='b', job_name='')
        self.driver.get("https://sandbox-recruiter.jobhopin.com/")

    def test_login_to_ats(self):
        loginPage = page_object_models.login_page.LoginPage(self.driver)
        loginPage.login_to_home_page()


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()