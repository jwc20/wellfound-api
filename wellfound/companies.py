import csv
import time
import json
import sys
from .utils import *
from collections import namedtuple, defaultdict
from requests.models import PreparedRequest
from pprintpp import pprint
from datetime import datetime

from bs4 import BeautifulSoup

now = datetime.now()
date_time_format = now.strftime("%Y-%m-%d_%H-%M-%S")


class Companies:
    def __init__(self, query=[], **kwargs):
        self.query = query
        # self.companies = kwargs.get("companies", [])
        # self.data = self.get_companies()


    def make_companies_url(self, query):
        return

    def _load_page(self, url):
        return

    def _scrape_page(self, soup):
        return

    def get_companies(self, query):

        ############################################################
        ## Scroll all the way to the bottom
        ## Get scroll height
        #last_height = self.driver.execute_script("return document.body.scrollHeight")
        #scroll_delay = 5

        #while True:
        #    # Scroll down to bottom
        #    self.driver.execute_script(
        #        "window.scrollTo(0, document.body.scrollHeight);"
        #    )

        #    # Wait to load page
        #    time.sleep(5)

        #    # Calculate new scroll height and compare with last scroll height
        #    new_height = self.driver.execute_script("return document.body.scrollHeight")
        #    if new_height == last_height:
        #        break
        #    last_height = new_height

        #for remaining in range(scroll_delay, 0, -1):
        #    sys.stdout.write("\r")
        #    sys.stdout.write("{:2d} seconds remaining.".format(remaining))
        #    sys.stdout.flush()
        #    time.sleep(1)
        #sys.stdout.write("\rComplete!                       \n")
        ############################################################


        soup = BeautifulSoup(self.driver.page_source, "lxml")
        # pprint(soup.prettify())
        
        # save the soup to a file
        with open(f"companies_{date_time_format}.html", "w") as file:
            print("writing to file...")
            file.write(soup.prettify())

        print("sleeping for 10 seconds...")
        time.sleep(10)


        # results = self._scrape_companies(soup)

        # return self.companies
