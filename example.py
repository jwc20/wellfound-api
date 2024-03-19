import wellfound
import os
from dotenv import load_dotenv

load_dotenv()


username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

client = wellfound.Wellfound(username=username, password=password)
client.login()


# query = []
# client.get_companies(query=query)

client.get_companies()
