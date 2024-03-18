from .utils import *
from .companies import Companies
from .login import Login


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-extensions")
options.add_argument("--disable-popup-blocking")


class Wellfound(Companies, Login):
    def __init__(self, **kwargs):
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        Companies.__init__(self, **kwargs)
        Login.__init__(self)

    def __del__(self):
        self.driver.quit()


__authors__ = ["jwc20"]
__source__ = "https://github.com/jwc20/wellfoundapi"
