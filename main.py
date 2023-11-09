from driver_setup import setup_driver  # Importing the function to set up the WebDriver
import scraper  # Importing the scraper module

def main():
    driver = setup_driver()  # Setting up the WebDriver

    # TODO: Insert GUI Here
    try:
        # Running the scraper function with specified coordinates
        scraper.enter_coordinates_and_submit(driver, 35, 34) # TODO: Replace Hardcoded values by input from GUI
    finally:
        driver.quit()  # Ensuring the WebDriver is closed after scraping

# Ensuring the script runs only if it is the main program
if __name__ == '__main__':
    main()
