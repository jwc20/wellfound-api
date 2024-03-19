from .utils import *
from .companies import Companies
from .login import Login


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# import pandas as pd
import time


# Chrome options
options = Options()
# options.add_argument("--headless=new")
# window size 500x500
options.add_argument("--window-size=900,1200")
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--disable-extensions")
# options.add_argument("--disable-popup-blocking")


# url = "https://www.wellfound.com/"

# driver = webdriver.Chrome(
#     service=ChromeService(ChromeDriverManager().install()), options=options
# )

# driver.get(url)


class Wellfound(Companies, Login):
    def __init__(self, **kwargs):
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()), options=options
        )
        Companies.__init__(self, **kwargs)
        Login.__init__(self)

    def __del__(self):
        self.driver.quit()


__authors__ = ["jwc20"]
__source__ = "https://github.com/jwc20/wellfound_scraper_api"
