from driver_setup import setup_driver
import scraper

def main():
    driver = setup_driver()
    try:
        scraper.enter_coordinates_and_submit(driver, 35, 34)
    finally:
        driver.quit()

if __name__ == '__main__':
    main()
