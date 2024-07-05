import time
import pytest
from functions.helpers import functions
from constants.globalConstants import *


@pytest.mark.usefixtures("setup")
class Test_Scenario02(functions):

#TC1
    def test_keyword(self):
        self.precondition_search_job()
        keyword = self.waitForElementVisible(KEYWORD_XPATH)
        keyword.send_keys("Software Engineer")
        self.jobClick()
        recommended = self.waitForElementVisible(RECOMMENDED_XPATH)
        recommended.click()
        old_again = self.waitForElementVisible(OLD_AGAIN_CSS_SELECTOR)
        old_again.click()
        self.take_screenshot("pictures/keyword.png")

#TC2
    def test_keyword_city(self):
        self.precondition_search_job()
        keyword_city = self.waitForElementVisible(KEYWORD_CITY_XPATH)
        keyword_city.send_keys("İstanbul")
        job_search = self.waitForElementVisible(JOB_SEARCH_XPATH)
        job_search.click()
        istanbul = self.waitForElementVisible(ISTANBUL_XPATH)
        assert istanbul.text == "İstanbul"

#TC3
    def test_keyword_company(self): 
        self.precondition_search_job()
        keyword_company = self.waitForElementVisible(KEYWORD_COMPANY_XPATH)
        keyword_company.send_keys("ETIYA")
        job_search = self.waitForElementVisible(JOB_SEARCH_XPATH)
        job_search.click()
        etiya = self.waitForElementVisible(ETIYA_XPATH)
        assert etiya.text == "ETIYA"