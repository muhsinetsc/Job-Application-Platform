import time
from selenium.webdriver.support.wait import WebDriverWait
from constants.globalConstants import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains 


class functions:
    def waitForElementVisible(self, locator, timeout= 20):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        
    def waitForElementsVisible(self, locator, timeout = 20):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def take_screenshot(self, filename):
        self.driver.get_screenshot_as_file(filename)
    
    def closePopup(self):
        close_popup = self.waitForElementVisible(CLOSE_POPUP_CSS_SELECTOR)
        close_popup.click()

    def actions(self,locator):
        actions = ActionChains(self.driver)
        actions.move_to_element(locator).perform()
        
    def newTab(self):
        window_after = self.driver.window_handles[-1]
        self.driver.switch_to.window(window_after)
 
    def precondition_search_job(self):
        search_job = self.waitForElementVisible(SEARCH_JOB_XPATH)
        search_job.click()

    def jobClick(self):
        job_search = self.waitForElementVisible(JOB_SEARCH_XPATH)
        job_search.click()


    def precondition_application(self):
        login = self.waitForElementVisible(LOGIN_XPATH)
        login.click()
        candidate = self.waitForElementVisible(CANDIDATE_XPATH)
        candidate.click()
        username = self.waitForElementVisible(USERNAME_ID)
        username.send_keys("tobeto1212@gmail.com")
        password = self.waitForElementVisible(PASS_ID)
        password.send_keys("Passwordtobeto1212")
        login_button = self.waitForElementVisible(LOGIN_BUTTON_XPATH)
        login_button.click()
        self.closePopup()
        try:
            not_interested = self.waitForElementVisible(By.XPATH, NOT_INTEREESTED_XPATH)
            not_interested.click()
            print("Element clicked.")
        except:
            print("Element not found or not visible.")
            
        job_search = self.waitForElementVisible(JOB_SEARCH_BUTTON_XPATH)
        job_search.click()
        time.sleep(1)
   

    def precondition_my_applications(self):
        login = self.waitForElementVisible(LOGIN_XPATH)
        login.click()
        candidate = self.waitForElementVisible(CANDIDATE_XPATH)
        candidate.click()
        username = self.waitForElementVisible(USERNAME_ID)
        username.send_keys("tobeto1212@gmail.com")
        password = self.waitForElementVisible(PASS_ID)
        password.send_keys("Passwordtobeto1212")
        login_button = self.waitForElementVisible(LOGIN_BUTTON_XPATH)
        login_button.click()
        self.closePopup()
        try:
            not_interested = self.waitForElementVisible(By.XPATH, NOT_INTEREESTED_XPATH)
            not_interested.click()
            print("Element clicked.")
        except:
            print("Element not found or not visible.")

        my_work = self.waitForElementVisible(MY_WORK_XPATH)
        self.actions(my_work)
        applications = self.waitForElementVisible(APPLICATIONS_XPATH)
        applications.click()
        time.sleep(1)

