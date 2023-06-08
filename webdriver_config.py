from selenium import webdriver
from fake_useragent import UserAgent


# webdriver options
options=webdriver.ChromeOptions()
options.add_argument(f'user-agent={UserAgent().random}')
options.add_argument('--disable-blink-features=AutomationControlled')
#options.add_argument('--headless')