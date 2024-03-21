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


# Chrome options
options = Options()
# options.add_argument("--headless=new")
options.add_argument("start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("--user-data-dir=chrome-data") # save cookies

class Wellfound(Companies, Login):
    def __init__(self, **kwargs):
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()), options=options
        )

        Companies.__init__(self, **kwargs)
        Login.__init__(self, self.driver)

    def __del__(self):
        self.driver.quit()


__authors__ = ["jwc20"]
__source__ = "https://github.com/jwc20/wellfound_scraper_api"
