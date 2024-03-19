import requests
from bs4 import BeautifulSoup

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException

import time
from .utils import *


class Login(object):
    def __init__(self, driver) -> None:
        self.driver = driver

    def login(self):
        # # get the login url from the utils fileV
        login_url = Base.URL + "/login"
        print(login_url)
        # print("Logging in...")
        # self.driver.get(login_url)
        # # wait for the page to load
        # time.sleep(2)
        try:
            print('Loading login page...')
            self.driver.get(login_url)
            WebDriverWait(self.driver, 200).until(ec.presence_of_element_located((By.ID, 'nc_1_n1z')))
        except TimeoutException:
            print('Load timeout')
            return False

