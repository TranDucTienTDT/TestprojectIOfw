from src.testproject.sdk.drivers import webdriver
import time


def search_without_filter():
    driver = webdriver.Chrome(token='8bh04dldZkEQBaX8RL6-T3Fid2oFWQVaqzD8NmVI_HE', project_name='basic_test',
                              job_name='')
    driver.get("https://staging-talent-partner.jobhopin.com/login")
    driver.maximize_window()
    driver.find_element_by_xpath("//input[@name='email']").send_keys("tien.tran@jobhopin.com")
    driver.find_element_by_xpath("//input[@name='password']").send_keys("tien123456")
    driver.find_element_by_xpath("//button[@type='submit']/span").click()
    time.sleep(5)
    criteria_dropdown_list = driver.find_element_by_xpath("//input[@name='criteria']")
    #criteria_option_all = driver.find_element_by_xpath("//ul/li[1]")
    #criteria_job_title = driver.find_element_by_xpath("//ul/li[2]")
    #criteria_skill = driver.find_element_by_xpath("//ul/li[3]")
    #criteria_job_link = driver.find_element_by_xpath("//ul/li[4]")
    search_box = driver.find_element_by_xpath("//input[@type='text']")
    search_button = driver.find_element_by_xpath("//button[@type='submit']/span")
    #position_collum = driver.find_element_by_xpath("//div/p[contains(text(),'php')]")


    search_box.send_keys("php")
    search_button.click()
    time.sleep(10)

    table_headers = driver.find_elements_by_xpath("//thead/tr/th/span")
    table_cells = driver.find_elements_by_xpath("//tbody/tr/th//p")

    for header in table_headers:
        print(header.text + "|")

    for cell in table_cells:
        print(cell.text + "|")

    driver.quit()


if __name__ == "__main__":
    search_without_filter()