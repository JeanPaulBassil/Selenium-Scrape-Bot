from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select


import settings


def wait(driver, element):
    WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, element))
    )

def selector(driver, selector_name, random_option_from_selector, optionNumber):
    wait(driver=driver, element=selector_name)
    wait(driver=driver, element=random_option_from_selector)

    select_list = driver.find_element(By.XPATH, selector_name)
    select = Select(select_list)
    select.select_by_visible_text(select.options[optionNumber].text)

def click_checkbox(driver, box):
    optimize_slope_and_azimuth = driver.find_element(By.XPATH, box)
    optimize_slope_and_azimuth.click()

def click_button(driver, button):
    download_as_csv = driver.find_element(By.XPATH, button)
    download_as_csv.click()

def enter_coordinates_and_submit(driver, latitude, longitude):
    driver.get(settings.TARGET_URL)

    try:
        wait(driver=driver, element=settings.ACCEPT_COOKIE_BUTTON_XPATH)
        accept_cookies_button = driver.find_element(By.XPATH, settings.ACCEPT_COOKIE_BUTTON_XPATH)
        accept_cookies_button.click()
    except NoSuchElementException:
        pass

    try:
        wait(driver, settings.CLOSE_COOKIE_PAGE_XPATH)
        accept_cookies_button = driver.find_element(By.XPATH, settings.CLOSE_COOKIE_PAGE_XPATH)
        accept_cookies_button.click()
    except NoSuchElementException:
        pass
    
    wait(driver=driver, element=settings.LATITUDE_INPUT_XPATH)
    wait(driver=driver, element=settings.LONGITUDE_INPUT_XPATH)
    wait(driver=driver, element=settings.SUBMIT_BUTTON_XPATH)
    
    lat_input = driver.find_element(By.XPATH, settings.LATITUDE_INPUT_XPATH)
    long_input = driver.find_element(By.XPATH, settings.LONGITUDE_INPUT_XPATH)

    lat_input.clear()
    long_input.clear()

    lat_input.send_keys(str(latitude))
    long_input.send_keys(str(longitude))

    submit_button = driver.find_element(By.XPATH, settings.SUBMIT_BUTTON_XPATH)

    submit_button.click()

    wait(driver=driver, element=settings.HOURLY_DATA_BUTTON)
    hourly_data_button = driver.find_element(By.XPATH, settings.HOURLY_DATA_BUTTON)
    hourly_data_button.click()

    selector(driver=driver, selector_name=settings.DATABASE_TYPE_SELECTOR, random_option_from_selector=settings.DATABASE_OPTION_SELECTOR, optionNumber=settings.DATABASE_OPTION_NUMBER)
    selector(driver=driver, selector_name=settings.START_YEAR_TYPE_SELECTOR, random_option_from_selector=settings.START_YEAR_OPTION_SELECTOR, optionNumber=settings.START_OPTION_NUMBER)
    selector(driver=driver, selector_name=settings.END_YEAR_TYPE_SELECTOR, random_option_from_selector=settings.END_YEAR_OPTION_SELECTOR, optionNumber=settings.END_OPTION_NUMBER)

    
    click_checkbox(driver=driver, box=settings.OPTMIZE_CHECKBOX)
    click_checkbox(driver=driver, box=settings.RADIATION_CHECKBOX)

    click_button(driver=driver, button=settings.DOWNLOAD_AS_CSV)


