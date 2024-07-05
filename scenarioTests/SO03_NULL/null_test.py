import time
import pytest
from functions.helpers import functions
from constants.globalConstants import *


@pytest.mark.usefixtures("setup")
class Test_Scenario03(functions):

    def test_invalid_category(self):
        self.precondition_search_job()
        remote = self.waitForElementVisible(REMOTE_XPATH)
        remote.click()
        self.driver.execute_script("window.scrollTo(0,700)")
        senior_executive = self.waitForElementVisible(SENIOR_EXECUTIVE_XPATH)
        senior_executive.click()
        self.driver.execute_script("window.scrollTo(700,2300)")
        apply = self.waitForElementVisible(APPLY_XPATH)
        apply.click()
        imformation_message = self.waitForElementVisible(INFORMATION_MESSAGE_XPATH)
        assert imformation_message.text == "Aramana uygun bir sonuç bulunamadı. 😔"

    def test_invalid_character(self):
        self.precondition_search_job()
        keyword = self.waitForElementVisible(KEYWORD_XPATH)
        keyword.send_keys("$")
        self.jobClick()
        imformation_message = self.waitForElementVisible(INFORMATION_MESSAGE_XPATH)
        assert imformation_message.text == "Aramana uygun bir sonuç bulunamadı. 😔"

    def test_empty_search(self):
        self.precondition_search_job()
        self.jobClick()
        self.take_screenshot("pictures/empty_search.png")














        
