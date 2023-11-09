TARGET_URL = 'https://re.jrc.ec.europa.eu/pvg_tools/en/'

LATITUDE_INPUT_XPATH = '//*[@id="inputLat"]'
LONGITUDE_INPUT_XPATH = '//*[@id="inputLon"]'
SUBMIT_BUTTON_XPATH = '//*[@id="btninputLatLon"]'

ACCEPT_COOKIE_BUTTON_XPATH = '/html/body/div[1]/div/div/div[2]/a[1]'
CLOSE_COOKIE_PAGE_XPATH = '/html/body/div[1]/div/div/div[2]/button'

HOURLY_DATA_BUTTON = '//*[@id="tabsTools"]/ul/li[6]/a'

DATABASE_TYPE_SELECTOR = '//*[@id="select_database_hourly"]'
DATABASE_OPTION_SELECTOR = '//*[@id="select_database_hourly"]/option[1]'
DATABASE_OPTION_NUMBER = 0

START_YEAR_TYPE_SELECTOR = '//*[@id="hstartyear"]'
START_YEAR_OPTION_SELECTOR = '//*[@id="hstartyear"]/option[1]'
START_OPTION_NUMBER = -2

END_YEAR_TYPE_SELECTOR = '//*[@id="hendyear"]'
END_YEAR_OPTION_SELECTOR = '//*[@id="hendyear"]/option[1]'
END_OPTION_NUMBER = -1

OPTMIZE_CHECKBOX = '//*[@id="hourlyoptimalangles"]'
RADIATION_CHECKBOX = '//*[@id="components"]'

DOWNLOAD_AS_CSV = '//*[@id="hourlydownloadcsv"]'