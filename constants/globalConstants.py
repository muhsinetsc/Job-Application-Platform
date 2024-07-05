from selenium.webdriver.common.by import By


#URL Globals
BASE_URL = "https://www.kariyer.net/"


#Preconditions: 

#precondition_search_job
SEARCH_JOB_XPATH = (By.XPATH,"//*[@id='header-nav-1']/a/span")

#precondition_application
LOGIN_XPATH = (By.XPATH,"//*[@id='navbar-wrapper']/nav/div/ul[2]/li[2]/button")
CANDIDATE_XPATH = (By.XPATH,"//*[@id='login-buttons-wrapper']/a[1]")
USERNAME_ID = (By.ID,"username")
PASS_ID = (By.ID,"pass")
LOGIN_BUTTON_XPATH = (By.XPATH,"//*[@id='__layout']/div/div[2]/div[2]/div[2]/div/div[1]/div/form/div[5]/div/div/button")
CLOSE_POPUP_CSS_SELECTOR = (By.CSS_SELECTOR,"body > div.k-guide > div.k-guide-container > i")
JOB_SEARCH_BUTTON_XPATH = (By.XPATH,"/html/body/div[1]/div/div/div[1]/div/header/div[2]/div[1]/div/nav/div/ul[1]/li[1]/a/span")
NOT_INTEREESTED_XPATH = (By.CSS_SELECTOR,"#target-banner___BV_modal_footer_ > div > button.btn.md.mr-2.close-banner")


#precondition_my_applications
MY_WORK_XPATH = (By.XPATH,"/html/body/div[1]/div/div/div[1]/div/header/div[2]/div[1]/div/nav/div/ul[1]/li[2]/button")
APPLICATIONS_XPATH = (By.XPATH,"//div[@id='navbar-wrapper']/nav/div/ul[1]/li[2]/div/div[1]/a[@href='/tum-basvurular']")


# XPATH Locators

#SO01_LIST
#TC1
AT_WORK_XPATH = (By.XPATH,"//*[@id='__BVID__71']/div/div[2]/div[1]/div/div/div")
REMOTE_XPATH = (By.XPATH,"//*[@id='__BVID__71']/div/div[2]/div[2]/div/div/div")
APPLY_XPATH = (By.XPATH,"//*[@id='submitButtonContainer']/button")

#TC2
CHOOSE_CITY_XPATH = (By.XPATH,"//*[@id='__BVID__59']/div[2]/div/span[2]")
ANKARA_XPATH = (By.XPATH,"//*[@id='__BVID__59']/div[2]/div[2]/div[2]/div[4]/div/div/div/label/div")
CITY_SELECTED_XPATH = (By.XPATH,"/html/body/div[1]/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div/div[2]/div/span[1]")
CHOOSE_DISTRICT_XPATH = (By.XPATH,"//*[@id='__BVID__59']/div[3]/div/span[2]")
AKYURT_XPATH = (By.XPATH,"/html/body/div[1]/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div/div/div/label/div")

#TC3
INFORMATION_XPATH = (By.XPATH,"/html//div[@id='filter-section']/div[@class='k-space large right']/div/div[2]/div[4]/div/div/div[2]/div/div[@class='checkbox-field kNetScroll']/div[2]/div[1]/div[@class='checkbox-items']/div/div/label[@class='custom-control-label']/div[@class='value w-auto']")
FULL_TIME_XPATH = (By.XPATH,"/html//div[@id='filter-section']/div[@class='k-space large right']/div/div[2]/div[7]/div/div/div[2]/div/div/div[2]/div[1]/div[@class='checkbox-items']/div/div/label[@class='custom-control-label']/div[@class='value w-auto']")
CLEAN_FILTERS_XPATH = (By.XPATH,"//*[@id='__layout']/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/h3/a") 


#SO02_FILTER XPATH
#TC1
KEYWORD_XPATH = (By.XPATH,"/html//div[@id='search-top']//div[@class='k-global-job-search']/form//div[@class='col-7']/div[@class='mr-2']/div[@class='k-auto-complete']/div[1]/div//input")
JOB_SEARCH_XPATH = (By.XPATH,"//*[@id='search-top']/div/div/div/form/div/div[2]/div/div[2]/div/button")
RECOMMENDED_XPATH = (By.XPATH,"/html/body/div[1]/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/button/div")

#TC2
KEYWORD_CITY_XPATH = (By.XPATH,"/html/body/div[1]/div/div/div[1]/div/header/div[2]/div[3]/div/div[2]/div[1]/div/div/div/div/div/form/div/div[2]/div/div[1]/div/div/div[1]/div/div/input")
ISTANBUL_XPATH = (By.XPATH,"//*[@id='__layout']/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div/span")

#TC3
KEYWORD_COMPANY_XPATH = (By.XPATH,"/html/body/div[1]/div/div/div[1]/div/header/div[2]/div[3]/div/div[2]/div[1]/div/div/div/div/div/form/div/div[1]/div/div/div[1]/div/div/input")
ETIYA_XPATH = (By.XPATH,"/html/body/div[1]/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div[3]/div/div/div/span")


#SO03_NULL

SENIOR_EXECUTIVE_XPATH = (By.XPATH,"//*[@id='__BVID__206']/div/div[2]/div[1]/div/div/div")
INFORMATION_MESSAGE_XPATH = (By.XPATH,"//*[@id='__layout']/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div[3]/div/div[2]/div[1]/div/div/div/div/div[1]/div[1]/div")

#SO04_SAVE


#SO05_DETAIL
APPLICATION_DETAILS_XPATH = (By.XPATH,"//*[@id='__layout']/div/div[2]/div[3]/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/div[2]")
APPLICATION_DATE_XPATH = (By.XPATH,"/html/body/div[1]/div/div/div[2]/div[3]/div[2]/div/div/div/div/div[2]/div[2]/div/div[3]/div/div[3]/div[1]/div[1]/div[2]")

GO_AD_XPATH = (By.XPATH,"//*[@id='__layout']/div/div[2]/div[3]/div[2]/div/div/div/div/div[2]/div[2]/div/div[3]/div/div[3]/div[2]/div[1]")
QUALIFICATIONS_XPATH = (By.XPATH,"/html/body/div[1]/div/div/div[2]/main/section/div/div/div[1]/div[2]/div/div[1]/div/h2")
SEE_MORE_XPATH = (By.XPATH,"//*[@id='__layout']/div/div[2]/main/section/div/div/div[1]/div[2]/footer/button")
GENERAL_QUALIFICATIONS_XPATH = (By.XPATH,"//*[@id='__layout']/div/div[2]/main/section/div/div/div[1]/div[2]/div/div[1]/div/div/p[5]")

DETAILED_INFORMATION_BUTTON_XPATH = (By.XPATH,"//*[@id='__layout']/div/div[2]/main/section/div/div/div[2]/div[1]/div/div[3]/a")
COMPANY_TEXT_XPATH = (By.XPATH,"/html/body/div[4]/div[1]/div/div/div/p/text()[2]")
COMPANY_TEXT_CLOSE_XPATH = (By.XPATH,"//body/div[3]/div[@role='dialog']//div[@class='modal-content']//button[@type='button']")
COMPANY_PAGE_XPATH = (By.XPATH,"//*[@id='__layout']/div/div[2]/main/section/div/div/div[2]/div[1]/div/div[2]/a")


#SO06_UPDATE
#TC1
CLICK_JOB_XPATH = (By.XPATH,"/html/body/div[1]/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/div[1]")
MAKE_APPLY_XPATH = (By.XPATH,"/html/body/div[1]/div/div/div[2]/main/section/div/div/div[1]/div[1]/div/div/div[1]/div[1]/div[2]/button[1]")
CHANGE_RESUME_XPATH = (By.XPATH,"//*[@id='application']/div/section[2]/div[1]/div/div/div/div")
VIEW_XPATH = (By.XPATH,"//*[@id='application']/div/section[2]/div[1]/div/div[2]/div/div[2]/a")
CONTACT_INFORMATION_XPATH = (By.XPATH,"//*[@id='contact']/div/div[2]/div/div/div")
LINKEDIN_XPATH = (By.XPATH,"//*[@id='contact']/div/div[2]/div/div/div/div[2]/div[7]/div/div/input")
SAVE_XPATH = (By.XPATH,"//*[@id='contact']/div/div[2]/div/div/div/div[3]/div/button[2]")
SAVE_MEDIA_XPATH = (By.XPATH,"//*[@id='contact']/div/div[2]/div/div/div/div/div[2]/div[4]/div[2]/div/div/span[2]/span")

#TC2
DOWN_ARROW_XPATH = (By.XPATH,"//div[@id='application']/div/section[2]/div[1]/div/div[@class='resume-card']//img")
CV_XPATH = (By.XPATH,"//div[@id='application']/div/section[2]/div[1]/div//ul/li[2]")
UPDATE_CV_POPUP_XPATH = (By.XPATH,"/html//div[@id='__layout']/div[@class='default-layout']//div[@class='toasters-fixed']/div//div[@class='toaster-title']")

#TC3
USER_XPATH = (By.XPATH,"//*[@id='navbar-wrapper']/nav/div/ul[2]/li[2]/button/i")
MY_ACCOUNT_XPATH = (By.XPATH,"//*[@id='user-top-menu-profile-url']")
CV_ICON_XPATH = (By.XPATH,"//*[@id='resume-list-section']/div[1]/section[2]/a/div/div[1]/div[2]/div/span")
EDIT_CV_XPATH = (By.XPATH,"//*[@id='resume-list-section']/div[1]/section[2]/a/div/div[1]/div[2]/div/div/div/div[1]")
SKILLS_XPATH = (By.XPATH,"//html[@id='index-page']/body[@class='header-static md-theme-default']/div[@class='candidate']/div//div[@class='nonexist-menu']/ul/li[7]/a[@href='javascript:void(0)']")
ADD_SKILL_XPATH = (By.XPATH,"//html[@id='index-page']//div[@id='abilities']/div[@class='resume-edit--box']/div[@class='content-body empty-section']//div[@class='col-12 frame-abilities']/div/div//input")
ADD_SKILL_CLICK_XPATH = (By.XPATH,"//html[@id='index-page']//div[@id='abilities']/div[@class='resume-edit--box']//div[@class='col-12 frame-abilities']/div/div/div[@class='multiselect__content-wrapper']/ul[@class='multiselect__content']//span[@class='multiselect__option multiselect__option--highlight']/span[.='Ms Office Programs']")
TALENT_OKEY_XPATH = (By.XPATH,"//*[@id='abilities']/div/div[2]/div/div/div/div[2]/div/div/div/button[2]")


# CSS SELECTOR Locators

#SO02_FILTER
OLD_AGAIN_CSS_SELECTOR = (By.CSS_SELECTOR,"#__layout > div > div.content-wrapper > div.jobs-list-container > div.k-skeleton-joblist.mt-lg-0 > div.clean-container-padding.container > div:nth-child(2) > div.col > div.row.d-md-block.d-none.justify-content-end > div > div > div > ul > li:nth-child(2)")


#SO05_DETAIL
COMPANY_TEXT_CSS_SELECTOR = (By.CSS_SELECTOR,"#__BVID__126___BV_modal_title_")
