from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import login_info as login

elms_url = "https://elms.umd.edu/"
DIRECTORYID = login.DIRECTORYID
PASSWORD = login.PASSWORD

# TODO: Optional update string based on your class to remind yourself of input to open course
course_name = str(input('Enter course name to open (Ex: cmsc433 or astr340):\n'))

# Checks for chromedriver updates
driver = webdriver.Chrome(ChromeDriverManager().install())

# Opens ELMS and logs in. Shouldn't be changed unless ELMS is updated
def open_and_login_elms():
    # Opens ELMS
    driver.get(elms_url)

    # Click on login button
    loginBtn = driver.find_element_by_link_text("LOG IN")
    loginBtn.click()

    # Find directoryId/password input box & enter info
    userName = driver.find_element_by_id('username')
    userName.send_keys(DIRECTORYID)
    passwrd = driver.find_element_by_id('password')
    passwrd.send_keys(PASSWORD)

    # Click on the login button
    login = driver.find_element_by_name('_eventId_proceed')
    login.click()

    # Switch to iFrame containing the duo mobile push button
    duoMobile = driver.find_element_by_id('duo_iframe')
    driver.switch_to.frame(duoMobile)

    # Press duo mobile push button
    wait = WebDriverWait(driver, 5)
    send_push_notification_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="auth_methods"]/fieldset/div[1]/button')))
    send_push_notification_btn.click()

    # Switch back to main webpage from duo mobile iframe 
    driver.switch_to.default_content()

    # Give time for user to accept the duo mobile push notification
    driver.implicitly_wait(10)

# Open UMD's zoom page in a new tab and login
def login_umd_zoom():
    # Open new tab & log in to UMD Zoom Acc
    driver.execute_script("window.open('https://umd.zoom.us/');")

    # Switches driver to new tab opened so we can interact w/ the zoom tab
    driver.switch_to.window(driver.window_handles[1])

    # Click on the sign in page to log into the UMD Zoom page
    signInBttn = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[3]/div[1]/a')
    signInBttn.click()

    # Wait to make sure you login before you close the zoom tab
    driver.implicitly_wait(10)
    driver.close()

    # Now what we're signed into zoom go back to ELMS & open the zooms tab
    driver.switch_to.window(driver.window_handles[0])
    zoomPage = driver.find_element_by_link_text('Zoom')
    zoomPage.click()

# Opens the clicker page for class 
# NOTE: Only works if the course page has the clickers tab on elms
def open_clickers_page():
    # Open Clickers page
    clickers = driver.find_element_by_link_text('Clickers')
    clickers.click()

    # Switch back to Elms page
    driver.switch_to.window(driver.window_handles[0])

# Based on input opens the class
def open_elms_course_page():
    # Click on the course menu
    course = driver.find_element_by_id('global_nav_courses_link')
    course.click()

    # TODO: Add to if/else statement all the classes you're taking / want
    # the script to open. The string in 'find_element_by_partial_link_text'
    # should partially match the course name of the class in the course tab on ELMS.
    # Also add the login_umd_zoom() or open_clickers_page() where necessary
    #
    # Ex:
    #   if in course tab: CMSC131-0402,0403,0404,0405,0406,0407,0408,0401: ........
    #   use 'CMSC131' in 'find_element_by_partial_link_text'

    # Depending on input opens up given class
    if course_name == 'astr340':
        driver.find_element_by_partial_link_text('ASTR340').click()
        # login_umd_zoom() # TODO: Do you need zoom open for this class? Then uncomment
        # open_clickers_page() # TODO: Does this class need clickers open? Then uncomment
    elif course_name == 'cmsc433':
        driver.find_element_by_partial_link_text('CMSC433').click()
        open_clickers_page()
        login_umd_zoom()

open_and_login_elms()
open_elms_course_page()