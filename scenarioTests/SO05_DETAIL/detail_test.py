import time
import pytest
from functions.helpers import functions
from constants.globalConstants import *


@pytest.mark.usefixtures("setup")
class Test_Scenario05(functions):

#TC1
    def test_history(self):
        self.precondition_my_applications()
        application_details = self.waitForElementVisible(APPLICATION_DETAILS_XPATH)
        application_details.click()
        self.driver.execute_script("window.scrollTo(0,500)")
        application_date = self.waitForElementVisible(APPLICATION_DATE_XPATH)
        assert application_date.text == "28.06.2024"

#TC2
    def test_detail (self):
        self.precondition_my_applications()
        application_details = self.waitForElementVisible(APPLICATION_DETAILS_XPATH)
        application_details.click()
        self.driver.execute_script("window.scrollTo(0,500)")
        application_date = self.waitForElementVisible(APPLICATION_DATE_XPATH)
        application_date.click()
        go_ad = self.waitForElementVisible(GO_AD_XPATH)
        go_ad.click()
        self.newTab()
        qualifications = self.waitForElementVisible(QUALIFICATIONS_XPATH)
        assert qualifications.text == "QUALIFICATIONS AND JOB DESCRIPTION"
        self.waitForElementVisible(SEE_MORE_XPATH).click()
        general_qualifications = self.waitForElementVisible(GENERAL_QUALIFICATIONS_XPATH)
        assert general_qualifications.text == "General Qualifications:"
        
#TC3
    def test_company_details(self):
        self.precondition_my_applications()
        application_details = self.waitForElementVisible(APPLICATION_DETAILS_XPATH)
        application_details.click()
        self.driver.execute_script("window.scrollTo(0,500)")
        application_date = self.waitForElementVisible(APPLICATION_DATE_XPATH)
        application_date.click()
        go_ad = self.waitForElementVisible(GO_AD_XPATH)
        go_ad.click()
        self.newTab()
        datailed_information_button = self.waitForElementVisible(DETAILED_INFORMATION_BUTTON_XPATH)
        datailed_information_button.click()
        time.sleep(2)
        self.take_screenshot("pictures/company_details.png")
        company_text_close = self.waitForElementVisible(COMPANY_TEXT_CLOSE_XPATH)
        company_text_close.click()
        company_page = self.waitForElementVisible(COMPANY_PAGE_XPATH)
        company_page.click()
        self.newTab()
        company_name = self.waitForElementVisible(COMPANY_NAME_XPATH)
        assert company_name.text == "Rams Türkiye"
        