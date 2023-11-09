# URL of the target website to be scraped
TARGET_URL = 'https://re.jrc.ec.europa.eu/pvg_tools/en/'

# XPaths for various elements on the webpage
LATITUDE_INPUT_XPATH = '//*[@id="inputLat"]'  # XPath for latitude input
LONGITUDE_INPUT_XPATH = '//*[@id="inputLon"]'  # XPath for longitude input
SUBMIT_BUTTON_XPATH = '//*[@id="btninputLatLon"]'  # XPath for the submit button

# XPaths for cookie consent elements
ACCEPT_COOKIE_BUTTON_XPATH = '/html/body/div[1]/div/div/div[2]/a[1]'  # XPath for accept cookies button
CLOSE_COOKIE_PAGE_XPATH = '/html/body/div[1]/div/div/div[2]/button'  # XPath for closing cookie information

# XPath for the hourly data button on the website
HOURLY_DATA_BUTTON = '//*[@id="tabsTools"]/ul/li[6]/a'

# XPaths and options for dropdown selectors
DATABASE_TYPE_SELECTOR = '//*[@id="select_database_hourly"]'  # XPath for database type selector
DATABASE_OPTION_SELECTOR = '//*[@id="select_database_hourly"]/option[1]'  # XPath for a specific option in the database type selector
DATABASE_OPTION_NUMBER = 0  # Index of the selected option for database type

START_YEAR_TYPE_SELECTOR = '//*[@id="hstartyear"]'  # XPath for start year selector
START_YEAR_OPTION_SELECTOR = '//*[@id="hstartyear"]/option[1]'  # XPath for a specific option in the start year selector
START_OPTION_NUMBER = -2  # Index of the selected option for start year

END_YEAR_TYPE_SELECTOR = '//*[@id="hendyear"]'  # XPath for end year selector
END_YEAR_OPTION_SELECTOR = '//*[@id="hendyear"]/option[1]'  # XPath for a specific option in the end year selector
END_OPTION_NUMBER = -1  # Index of the selected option for end year

# XPaths for checkboxes
OPTMIZE_CHECKBOX = '//*[@id="hourlyoptimalangles"]'  # XPath for optimize checkbox
RADIATION_CHECKBOX = '//*[@id="components"]'  # XPath for radiation checkbox

# XPath for the button to download data as CSV
DOWNLOAD_AS_CSV = '//*[@id="hourlydownloadcsv"]'
