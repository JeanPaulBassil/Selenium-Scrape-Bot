from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select

import settings

# Function to wait until a specific element is present on the page
def wait(driver, element):
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, element))
    )

# Function to select an option from a dropdown menu
def selector(driver, selector_name, random_option_from_selector, optionNumber):
    wait(driver=driver, element=selector_name)
    wait(driver=driver, element=random_option_from_selector)

    select_list = driver.find_element(By.XPATH, selector_name)
    select = Select(select_list)
    select.select_by_visible_text(select.options[optionNumber].text)

# Function to click a checkbox on the webpage
def click_checkbox(driver, box):
    checkbox = driver.find_element(By.XPATH, box)
    checkbox.click()

# Function to click a button on the webpage
def click_button(driver, button):
    button_element = driver.find_element(By.XPATH, button)
    button_element.click()

# Main function to enter coordinates and submit them on the target webpage
def enter_coordinates_and_submit(driver, latitude, longitude):
    driver.get(settings.TARGET_URL)

    # Accept cookies if the option is present
    try:
        wait(driver=driver, element=settings.ACCEPT_COOKIE_BUTTON_XPATH)
        accept_cookies_button = driver.find_element(By.XPATH, settings.ACCEPT_COOKIE_BUTTON_XPATH)
        accept_cookies_button.click()
    except NoSuchElementException:
        pass

    # Close cookie information if the option is present
    try:
        wait(driver, settings.CLOSE_COOKIE_PAGE_XPATH)
        close_cookie_button = driver.find_element(By.XPATH, settings.CLOSE_COOKIE_PAGE_XPATH)
        close_cookie_button.click()
    except NoSuchElementException:
        pass
    
    # Wait for latitude, longitude input fields and submit button to be ready
    wait(driver=driver, element=settings.LATITUDE_INPUT_XPATH)
    wait(driver=driver, element=settings.LONGITUDE_INPUT_XPATH)
    wait(driver=driver, element=settings.SUBMIT_BUTTON_XPATH)
    
    # Enter latitude and longitude
    lat_input = driver.find_element(By.XPATH, settings.LATITUDE_INPUT_XPATH)
    long_input = driver.find_element(By.XPATH, settings.LONGITUDE_INPUT_XPATH)
    lat_input.clear()
    long_input.clear()
    lat_input.send_keys(str(latitude))
    long_input.send_keys(str(longitude))

    # Submit the entered coordinates
    submit_button = driver.find_element(By.XPATH, settings.SUBMIT_BUTTON_XPATH)
    submit_button.click()

    # Perform further actions after submitting coordinates
    wait(driver=driver, element=settings.HOURLY_DATA_BUTTON)
    hourly_data_button = driver.find_element(By.XPATH, settings.HOURLY_DATA_BUTTON)
    hourly_data_button.click()

    # Select options from various dropdowns
    selector(driver=driver, selector_name=settings.DATABASE_TYPE_SELECTOR, random_option_from_selector=settings.DATABASE_OPTION_SELECTOR, optionNumber=settings.DATABASE_OPTION_NUMBER)
    selector(driver=driver, selector_name=settings.START_YEAR_TYPE_SELECTOR, random_option_from_selector=settings.START_YEAR_OPTION_SELECTOR, optionNumber=settings.START_OPTION_NUMBER)
    selector(driver=driver, selector_name=settings.END_YEAR_TYPE_SELECTOR, random_option_from_selector=settings.END_YEAR_OPTION_SELECTOR, optionNumber=settings.END_OPTION_NUMBER)

    # Click necessary checkboxes
    click_checkbox(driver=driver, box=settings.OPTMIZE_CHECKBOX)
    click_checkbox(driver=driver, box=settings.RADIATION_CHECKBOX)

    # Click the button to download data as CSV
    click_button(driver=driver, button=settings.DOWNLOAD_AS_CSV)
