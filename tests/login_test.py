#from src.testproject.sdk.drivers import webdriver
from drivers.base_driver import BaseDriver
import time

# Constant
BROWSER = 'Chrome'
TOKEN = '8bh04dldZkEQBaX8RL6-T3Fid2oFWQVaqzD8NmVI_HE'
PROJECT_NAME = 'basic_test'
JOB_NAME = 'a'


def invalid_login_test():
    #driver = webdriver.Chrome(token='8bh04dldZkEQBaX8RL6-T3Fid2oFWQVaqzD8NmVI_HE', project_name='basic_test', job_name='')
    driver = BaseDriver.browser(BROWSER,TOKEN, PROJECT_NAME, JOB_NAME)
    driver.get("https://staging-talent-partner.jobhopin.com/login")
    driver.maximize_window()
    driver.find_element_by_xpath("//input[@name='email']").send_keys("John@mailinator.com")
    driver.find_element_by_xpath("//input[@name='password']").send_keys("12345")
    driver.find_element_by_xpath("//button[@type='submit']/span").click()
    time.sleep(5)
    passed = driver.find_element_by_xpath("//button[@type='submit']/span").is_displayed()
    print("Test passed") if passed else print("Test failed")

    driver.quit()


def valid_login_test():
    #driver = webdriver.Chrome(token='8bh04dldZkEQBaX8RL6-T3Fid2oFWQVaqzD8NmVI_HE', project_name='basic_test',job_name='')
    driver = BaseDriver.browser(BROWSER, TOKEN, PROJECT_NAME, JOB_NAME)
    driver.get("https://staging-talent-partner.jobhopin.com/login")
    driver.maximize_window()
    driver.find_element_by_xpath("//input[@name='email']").send_keys("tien.tran@jobhopin.com")
    driver.find_element_by_xpath("//input[@name='password']").send_keys("tien123456")
    driver.find_element_by_xpath("//button[@type='submit']/span").click()
    time.sleep(5)
    passed = driver.find_element_by_xpath("//span[contains(@class, 'icon-icon_search')]").is_displayed()
    print("Test passed") if passed else print("Test failed")

    driver.quit()


if __name__ == "__main__":
    invalid_login_test()
    valid_login_test()