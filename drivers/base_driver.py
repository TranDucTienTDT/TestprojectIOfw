from src.testproject.sdk.drivers import webdriver
import logging

logging.basicConfig(level=logging.INFO)


class BaseDriver():



    # Declare driver for browser
    def browser(self, BROWSER, TOKEN, PROJECT_NAME, JOB_NAME):
        if BROWSER == 'Chrome':
            return webdriver.Chrome(token=TOKEN, project_name=PROJECT_NAME, job_name=JOB_NAME)
        elif BROWSER == 'Firefox':
            return webdriver.Firefox(token=TOKEN, project_name=PROJECT_NAME, job_name=JOB_NAME)
        elif BROWSER == 'Safari':
            return webdriver.Safari(token=TOKEN, project_name=PROJECT_NAME, job_name=JOB_NAME)
        else:
            print('Browser is not supported.')
