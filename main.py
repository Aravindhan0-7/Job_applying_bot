from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

PHONE="PHONE_NO."

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3958896715&f_AL=true&geoId=106888327&keywords=ai%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")

#reject

#signin
time.sleep(2)
sign_in=driver.find_element(by=By.XPATH,value="/html/body/div[2]/a[1]")
sign_in.click()
time.sleep(2)
#login
mail=driver.find_element(by=By.ID,value="username")
mail.send_keys("EMAIL_ID)
password=driver.find_element(by=By.ID,value="password")
password.send_keys("PASSWORD",Keys.ENTER)


#apply jobs
time.sleep(3)
job_1=driver.find_element(by=By.CSS_SELECTOR,value='.jobs-apply-button--top-card button')
job_1.click()

time.sleep(5)
enter_no=driver.find_element(by=By.ID,value='single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3958896715-1442669789-phoneNumber-nationalNumber')
enter_no.send_keys(PHONE)
time.sleep(2)
next_button=driver.find_element(by=By.XPATH,value='//*[@id="ember390"]')
next_button.click()



