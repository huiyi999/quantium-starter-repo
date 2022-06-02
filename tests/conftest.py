"""
Created on 2022-06-02
@author: chy
"""
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

# driver = webdriver.Chrome('/usr/local/bin/chromedriver')
# # Optional argument, if not specified will search path.
#
# driver.get('http://www.google.com/')

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

options = webdriver.ChromeOptions()
options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
service = ChromeService(executable_path='/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=service, options=options)



def pytest_setup_options():
    options = Options()
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    return options
