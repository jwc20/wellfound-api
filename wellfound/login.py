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

    def login(self, email, password):
        login_url = Base.URL + "/login"
        print(login_url)

        # <input placeholder="Email" class="u-fontSize14 js-email" autofocus="autofocus" type="email" value="" name="user[email]" id="user_email">
        # get the email input field
        email_input = self.driver.find_element_by_id('user_email')
        email_input.send_keys(email)

        # <input placeholder="Password" class="u-fontSize14" type="password" name="user[password]" id="user_password">
        # get the password input field
        password_input = self.driver.find_element_by_id('user_password')
        password_input.send_keys(password)

        # <input type="submit" name="commit" value="Log in" class="c-button c-button--blue s-vgPadLeft1_5 s-vgPadRight1_5" ontouchstart="" data-disable-with="Log in">
        # get the login button
        login_button = self.driver.find_element_by_name('commit')
        login_button.click()


        # wait for the page to load
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.presence_of_element_located((By.ID, 'nc_1_n1z')))

        try:
            print('Loading login page...')
            self.driver.get(login_url)
            WebDriverWait(self.driver, 200).until(ec.presence_of_element_located((By.ID, 'nc_1_n1z')))
        except TimeoutException:
            print('Load timeout')
            return False

