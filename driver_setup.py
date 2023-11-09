from selenium import webdriver
# ChromeDriverManager is imported but not used, consider removing it if not needed
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver():
    # Initialize a Chrome WebDriver instance
    driver = webdriver.Chrome()
    return driver
