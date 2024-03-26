import wellfound
import os
from dotenv import load_dotenv

load_dotenv()


email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

client = wellfound.Wellfound(email=email, password=password)
client.login(email=email, password=password)

client.get_companies(query=[])
