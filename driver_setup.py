from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver():
    driver = webdriver.Chrome()
    return driver
