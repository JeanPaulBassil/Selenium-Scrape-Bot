# Selenium Web Scraper for PVGIS Website

## Overview
This Selenium-based web scraper is designed to automate the process of gathering solar radiation and PV system performance data from the [PVGIS website](https://re.jrc.ec.europa.eu/pvg_tools/en/). It navigates through the site, enters specified geographical coordinates, and downloads the relevant data in CSV format.

## Features
- **Automated Navigation**: Navigates through the PVGIS website's interface.
- **Data Entry**: Inputs latitude and longitude coordinates.
- **Cookie Consent Handling**: Manages cookie consent pop-ups.
- **Data Download**: Downloads hourly solar radiation and PV performance data.

## Prerequisites
- Python 3.x
- Selenium WebDriver
- ChromeDriver (or any compatible driver for your preferred browser)

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/JeanPaulBassil/Selenium-Scrape-Bot.git
   ```
2. Install required Python packages:
   ```
   pip install selenium webdriver_manager
   ```

## Usage
1. Import and instantiate the main scraping function from `scraper.py`.
2. Call the `enter_coordinates_and_submit` function with desired latitude and longitude parameters.
3. The script will open the browser, navigate the website, and download the CSV file with the data.

Example:
```python
from scraper import enter_coordinates_and_submit
from driver_setup import setup_driver

driver = setup_driver()
enter_coordinates_and_submit(driver, latitude=40.7128, longitude=-74.0060)
```

## Structure
- `driver_setup.py`: Sets up the Selenium WebDriver.
- `scraper.py`: Contains the main scraping logic and functions.
- `settings.py`: Stores URLs, XPaths, and other constants.
- `main.py`: Example implementation showing how to use the scraper.

## Contributing
Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

