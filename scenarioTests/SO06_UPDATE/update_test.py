import time
import pytest
from functions.helpers import functions
from constants.globalConstants import *


@pytest.mark.usefixtures("setup")
class Test_Scenario06(functions):


    def test_contact_update(self):
        self.precondition_application()
        self.closePopup()
        keyword = self.waitForElementVisible(KEYWORD_XPATH)
        keyword.send_keys("Software Tester  TCI Aircraft Interiors")
        self.jobClick()
        click_job = self.waitForElementVisible(CLICK_JOB_XPATH)
        click_job.click()
        self.newTab()
        make_apply = self.waitForElementVisible(MAKE_APPLY_XPATH)
        make_apply.click()
        change_resume = self.waitForElementVisible(CHANGE_RESUME_XPATH)
        change_resume.click()
        view = self.waitForElementVisible(VIEW_XPATH)
        view.click()
        self.newTab()
        contact_information = self.waitForElementVisible(CONTACT_INFORMATION_XPATH)
        contact_information.click()
        linkedin = self.waitForElementVisible(LINKEDIN_XPATH)
        linkedin.send_keys("https://tr.linkedin.com/")
        self.driver.execute_script("window.scrollTo(0,500)")
        save = self.waitForElementVisible(SAVE_XPATH)
        save.click()
        save_media = self.waitForElementVisible(SAVE_MEDIA_XPATH)
        assert save_media.text == "https://tr.linkedin.com/"

    def test_information_update(self):
        self.precondition_application()
        self.closePopup()
        keyword = self.waitForElementVisible(KEYWORD_XPATH)
        keyword.send_keys("Software Tester  TCI Aircraft Interiors")
        self.jobClick()
        click_job = self.waitForElementVisible(CLICK_JOB_XPATH)
        click_job.click()
        self.newTab()
        make_apply = self.waitForElementVisible(MAKE_APPLY_XPATH)
        make_apply.click()
        change_resume = self.waitForElementVisible(CHANGE_RESUME_XPATH)
        change_resume.click()
        down_arrow = self.waitForElementVisible(DOWN_ARROW_XPATH)
        down_arrow.click()
        cv = self.waitForElementVisible(CV_XPATH)
        cv.click()
        update_cv = self.waitForElementVisible(UPDATE_CV_POPUP_XPATH)
        assert update_cv.text == "Özgeçmişin değiştirildi."

    def test_skill(self):
        self.precondition_application()
        self.closePopup()
        user = self.waitForElementVisible(USER_XPATH)
        user.click()
        my_account = self.waitForElementVisible(MY_ACCOUNT_XPATH)
        my_account.click()
        self.closePopup()
        cv_icon = self.waitForElementVisible(CV_ICON_XPATH)
        cv_icon.click()
        edit_cv = self.waitForElementVisible(EDIT_CV_XPATH)
        edit_cv.click()
        self.newTab()
        skills = self.waitForElementVisible(SKILLS_XPATH)
        skills.click()
        add_skill = self.waitForElementVisible(ADD_SKILL_XPATH)
        add_skill.send_keys("Ms Office Programs")
        add_skill_click = self.waitForElementVisible(ADD_SKILL_CLICK_XPATH)
        add_skill_click.click()
        talent_okey = self.waitForElementVisible(TALENT_OKEY_XPATH)
        talent_okey.click()
        time.sleep(1)
        self.take_screenshot("pictures/skill.png")
        