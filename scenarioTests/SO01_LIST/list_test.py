import time
import pytest
from functions.helpers import functions
from constants.globalConstants import *


@pytest.mark.usefixtures("setup")
class Test_Scenario01(functions):
    
#TC1
    def test_category_selections(self):
        self.precondition_search_job()
        at_work = self.waitForElementVisible(AT_WORK_XPATH)
        at_work.click()
        remote = self.waitForElementVisible(REMOTE_XPATH)
        remote.click()
        self.driver.execute_script("window.scrollTo(0,2100)")
        apply = self.waitForElementVisible(APPLY_XPATH)
        apply.click()
        self.driver.execute_script("window.scrollTo(0,500)")
        self.take_screenshot("pictures/category_selections.png")

#TC2
    def test_location_list(self):
        self.precondition_search_job()
        choose_city = self.waitForElementVisible(CHOOSE_CITY_XPATH)
        choose_city.click()
        ankara = self.waitForElementVisible(ANKARA_XPATH)
        ankara.click()
        city_selected = self.waitForElementVisible(CITY_SELECTED_XPATH)
        assert city_selected.text == "1 şehir seçildi"
        choose_city = self.waitForElementVisible(CHOOSE_CITY_XPATH)
        choose_city.click()
        choose_district = self.waitForElementVisible(CHOOSE_DISTRICT_XPATH)
        choose_district.click()
        akyurt = self.waitForElementVisible(AKYURT_XPATH)
        akyurt.click()
        self.driver.execute_script("window.scrollTo(0,2100)")
        apply = self.waitForElementVisible(APPLY_XPATH)
        apply.click()
        self.take_screenshot("pictures/location_list.png")
#TC3
    def test_clean_filters(self):
        self.precondition_search_job()
        at_work = self.waitForElementVisible(AT_WORK_XPATH)
        at_work.click()
        self.driver.execute_script("window.scrollTo(0,500)")
        information = self.waitForElementVisible(INFORMATION_XPATH)
        information.click()
        self.driver.execute_script("window.scrollTo(500,1500)")
        full_time = self.waitForElementVisible(FULL_TIME_XPATH)
        full_time.click()
        self.driver.execute_script("window.scrollTo(1500,2100)")
        apply = self.waitForElementVisible(APPLY_XPATH)
        apply.click()
        clean_filters = self.waitForElementVisible(CLEAN_FILTERS_XPATH)
        clean_filters.click()