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


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pprint import pprint


class Login:
    def __init__(self, driver):
        self.driver = driver

    # def check_login_status(self):
    #     """Checks if the user is logged in."""
    #     # self.driver.get(f"{Base.URL}/jobs")

    #     if self.driver.current_url == f"{Base.URL}/jobs":
    #         return True
    #     # return self.wait_for_login_to_complete()
    #     return False

    def navigate_to_login_page(self):
        """Navigates to the login page."""
        login_url = f"{Base.URL}/login"
        print(login_url)
        self.driver.get(login_url)

    def fill_login_form(self, email, password):
        """Fills in the login form with email and password."""
        email_input = self.driver.find_element(By.ID, "user_email")
        email_input.send_keys(email)

        password_input = self.driver.find_element(By.ID, "user_password")
        password_input.send_keys(password)

    def submit_login_form(self):
        """Submits the login form."""
        login_button = self.driver.find_element(By.NAME, "commit")
        login_button.click()

    def wait_for_login_to_complete(self):
        """Waits for the login process to complete by checking for a specific element on the next page."""
        wait = WebDriverWait(self.driver, 10)
        # print the current url
        print(self.driver.current_url)
        print(f"{Base.URL}/jobs")

        try:
            wait.until(EC.presence_of_element_located((By.ID, "nc_1_n1z")))
        except TimeoutException:
            print("Login page load timeout.")
            # if self.driver.current_url == f"{Base.URL}/jobs":
            #     return True

            return False
        return True

    def login(self, email, password):
        """Performs the complete login operation."""



        # from utils.py
        # if check_login_status(self):
        #     print("Already logged in.")
        #     return

        try:
            login_status = check_login_status(self)
            if login_status:
                print("Already logged in.")
                return
            # else login
            self.navigate_to_login_page()
            self.fill_login_form(email, password)
            self.submit_login_form()
            if self.wait_for_login_to_complete():
                print("Successfully logged in.")
                pprint(self.driver.get_cookies())
            else:
                print("Failed to log in.")
        except:
            print("Failed to check login status.")
            return


        # self.navigate_to_login_page()
        # self.fill_login_form(email, password)
        # self.submit_login_form()
        # if self.wait_for_login_to_complete():
        #     print("Successfully logged in.")
        #     pprint(self.driver.get_cookies())
        # else:
        #     print("Failed to log in.")
