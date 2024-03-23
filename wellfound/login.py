import time
from .utils import *
from pprint import pprint

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Login:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def check_if_captcha_check(self):
        """Checks if the captcha check is required."""
        try:
            # check if there is this element in the page <body style="margin:0"><script data-cfasync="false">var dd={'rt':'c','cid':'AHrlqAAAAAMAgciZ7cjSuv4AAeEDHQ==','hsh':'BA3EB296E8BE96A496929870E20CD4','t':'fe','s':23648,'e':'452ac128343f6eacf7ce6135555a760ed001e0b8493f0b4de9b85d5b8f14291e','host':'geo.captcha-delivery.com'}</script><script data-cfasync="false" src="https://ct.captcha-delivery.com/c.js"></script><iframe src="https://geo.captcha-delivery.com/captcha/?initialCid=AHrlqAAAAAMAgciZ7cjSuv4AAeEDHQ%3D%3D&amp;hash=BA3EB296E8BE96A496929870E20CD4&amp;cid=Y9E8ysAOjhRZ82MYnVQOh4f1qZLnKNG1dQ9gAgD86C8XTz5NWVFQhOVIw6fvy65u~hUbWW9LxIKXPgHrNGKI38~QzMkl7B~LSVQJbaseJitkrRChl5~iQ6tIVRmlzlF3&amp;t=fe&amp;referer=https%3A%2F%2Fwellfound.com%2Flogin&amp;s=23648&amp;e=452ac128343f6eacf7ce6135555a760ed001e0b8493f0b4de9b85d5b8f14291e" width="100%" height="100%" style="height:100vh;" frameborder="0" border="0" scrolling="yes"></iframe></body>
            self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@data-cfasync="false"]')
                )
            )
            print("Captcha check required.")
            return True
        except TimeoutException:
            print("No captcha check required.")
            return False

    def check_login_status(self):
        """Checks if the user is logged in by checking the url."""
        # initial page: chrome://new-tab-page/
        # get the current url after redirect from chrome://new-tab-page/
        self.navigate_to_jobs_page()

        try:
            # wait until the element is loaded in the page where data-test="JobSearchPage"
            self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@data-test="JobSearchPage"]')
                )
            )
        except TimeoutException:
            print("Jobs page load timeout.")
            return False
        return True

    def navigate_to_jobs_page(self):
        """Navigates to the jobs page."""
        jobs_url = f"{Base.URL}/jobs"
        self.driver.get(jobs_url)
        time.sleep(5)

    def navigate_to_login_page(self):
        """Navigates to the login page."""
        login_url = f"{Base.URL}/login"
        # print(login_url)
        self.driver.get(login_url)
        time.sleep(5)

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
        time.sleep(5)

    def login(self, email, password):
        """Performs the complete login operation."""
        try:
            if self.check_login_status():
                print("Already logged in.")
                # pprint(self.driver.get_cookies())
                return
            else:
                print("Not logged in.")
                self.navigate_to_login_page()
                if self.check_if_captcha_check():
                    return
                self.fill_login_form(email, password)
                self.submit_login_form()

                if self.check_login_status():
                    print("Successfully logged in.")
                    pprint(self.driver.get_cookies())
                    return
                else:
                    print("Failed to log in.")
        except Exception as e:
            print(f"An error occurred during login: {e}")
            raise e
