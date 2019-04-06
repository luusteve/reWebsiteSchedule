from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(r"PATH to chromedriver.exe" ,options = chrome_options)
minerva = "https://www.mcgill.ca/minerva"
#Enter student email
id = ""
#Enter password
pasw = ""
#Enter desired semester
semester = ""
#input CRN code
desiredCourse = ""
driver.get(minerva)

idInput = driver.find_element_by_id("mcg_un")
paswInput = driver.find_element_by_id("mcg_pw")
idInput.send_keys(id)
paswInput.send_keys(pasw)
id = ""
pasw = ""
idInput.submit()
driver.find_element_by_link_text("Student Menu").click()
driver.find_element_by_link_text("Registration Menu").click()
driver.find_element_by_link_text("Quick Add or Drop Course Sections").click()
select = Select(driver.find_element_by_id('term_id'))
select.select_by_visible_text(semester)
driver.find_element_by_xpath("//input[@type ='submit' and @value='Submit']").click()
while True:
    CRNinput = driver.find_element_by_id("crn_id1")
    CRNinput.send_keys(desiredCourse)
    driver.find_element_by_xpath("//input[@type ='submit' and @name ='REG_BTN' and @value='Submit Changes']").click()
    time.sleep(30)
