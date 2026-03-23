import os
from dotenv import load_dotenv

load_dotenv()

MY_MAIL = os.getenv("MY_MAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")
SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")
