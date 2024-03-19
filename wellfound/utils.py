# import requests
from enum import Enum
# from bs4 import BeautifulSoup
# import sys
# import time


try:
    from urllib import urlencode, urlunsplit
except ImportError:
    from urllib.parse import urlunsplit, urlencode


class Base(str, Enum):
    URL = "https://www.wellfound.com"

    def __str__(self):
        return str(self.value)


class Header(str, Enum):
    PAYLOAD = {"Content-Type": "text/html; charset=UTF-8"}

    def __str__(self):
        return str(self.value)

# class LoginURL(object):
#     URL = "/login"

#     def __str__(self):
#         return str(self.URL)


print(Base.URL)
print(Header.PAYLOAD)
