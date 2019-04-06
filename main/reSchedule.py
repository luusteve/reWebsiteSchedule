from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

start_time = time.time()
driver = webdriver.Chrome(r"..\drivers\chromedriver.exe" ,options = chrome_options)
minerva = "https://www.mcgill.ca/minerva"
#Enter student email
id = "EMAIL ID"
#Enter password
pasw = "PASSWORD"
#Enter desired semester Example: Summer 2019
semester = "Summer 2019"
#input CRN code
desiredCourse = "CRN"
driver.get(minerva)
i = 0

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
    try:
        i += 1
        if (i % 10) == 0:
            print(str(i) + " TRIES in:" )
            end = time.time()
            hours, rem = divmod(end - start_time, 3600)
            minutes, seconds = divmod(rem, 60)
            print("{:0>2}:{:0>2}:{:05.2f}\n".format(int(hours), int(minutes), seconds))
        CRNinput = driver.find_element_by_id("crn_id1")
        CRNinput.send_keys(desiredCourse)
        driver.find_element_by_xpath("//input[@type ='submit' and @name ='REG_BTN' and @value='Submit Changes']").click()
        time.sleep(20)
    except:
        print("REFRESH")
        print(str(i) + " TRIES in:")
        end = time.time()
        hours, rem = divmod(end - start_time, 3600)
        minutes, seconds = divmod(rem, 60)
        print("{:0>2}:{:0>2}:{:05.2f}\n".format(int(hours), int(minutes), seconds))
        time.sleep(2)
        driver.refresh()

