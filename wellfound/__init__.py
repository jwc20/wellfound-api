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


options.add_argument('--no-sandbox')
options.add_argument('--disable-setuid-sandbox')
options.add_argument("--proxy-server='direct://'")
options.add_argument('--proxy-bypass-list=*')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-accelerated-2d-canvas')
options.add_argument('--disable-gpu')
options.add_argument('--disable-features=site-per-process')
options.add_argument('--enable-features=NetworkService')
options.add_argument('--allow-running-insecure-content')
options.add_argument('--enable-automation')
options.add_argument('--disable-background-timer-throttling')
options.add_argument('--disable-backgrounding-occluded-windows')
options.add_argument('--disable-renderer-backgrounding')
options.add_argument('--disable-web-security')
options.add_argument('--autoplay-policy=user-gesture-required')
options.add_argument('--disable-background-networking')
options.add_argument('--disable-breakpad')
options.add_argument('--disable-client-side-phishing-detection')
options.add_argument('--disable-component-update')
options.add_argument('--disable-default-apps')
options.add_argument('--disable-domain-reliability')
options.add_argument('--disable-extensions')
options.add_argument('--disable-features=AudioServiceOutOfProcess')
options.add_argument('--disable-hang-monitor')
options.add_argument('--disable-ipc-flooding-protection')
options.add_argument('--disable-notifications')
options.add_argument('--disable-offer-store-unmasked-wallet-cards')
options.add_argument('--disable-popup-blocking')
options.add_argument('--disable-print-preview')
options.add_argument('--disable-prompt-on-repost')
options.add_argument('--disable-speech-api')
options.add_argument('--disable-sync')
options.add_argument('--disk-cache-size=33554432')
options.add_argument('--hide-scrollbars')
options.add_argument('--ignore-gpu-blacklist')
options.add_argument('--metrics-recording-only')
options.add_argument('--mute-audio')
options.add_argument('--no-default-browser-check')
options.add_argument('--no-first-run')
options.add_argument('--no-pings')
options.add_argument('--no-zygote')
options.add_argument('--password-store=basic')
options.add_argument('--use-gl=swiftshader')
options.add_argument('--use-mock-keychain')


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
